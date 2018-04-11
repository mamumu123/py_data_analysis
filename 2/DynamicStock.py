import requests
import  re
#from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
####           第六题   ################################################
##循环输入，直到-1结束
key=int(input("请输入你想要的查询的股票代码：如果没有其他需求，-1结束\n"))
while(key!=-1):
    ##根据输入，组合url
    url='http://quotes.money.163.com/0'+str(key)+'.html'
    #try:
    ##获取网页内容
    res = requests.get(url)
    res.encoding = "utf-8"  # 设置网页编码
    #print(r.status_code)
    ##如果股票代码错误，那么将会提示找不到，需要重新输入
    if(res.status_code==404):
        key = int(input("你输入的股票代码查询不到，请重新输入，如果没有其他需求，-1结束\n"))
        #continue可以直接结束下面的内容，跳转到while
        continue
    # 用bs4处理网页结构
    soup = BeautifulSoup(res.text, "html.parser")
    table = soup.select(".corp_info")
    table_child = []

    for child in table[0].strings:
        table_child.append(child)
    ##用正则表达式找到“上市日期”
    mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", (table_child[19]))
    print('首次上市的时间:\n',mat.group())#
    date=mat.group()
    mat = re.search(r"(\d+)", (date))
    ##得到 year
    year = int(mat.group())

    ##将得到的数据都保存到txt中，用excel打开
    filename = './txt/'+str(key)+'.txt'
    fd = open(filename, 'w', encoding='utf-8', errors='ignore')
    print('正在下载，请稍等')
    ##做循环，year和season的二重循环，将所有数据得到
    while(year<=2017):
        #print('year:   ',year)
        for season  in  range(1,5):
            #print('season:   ', season)
            #得到url
            newUrl = 'http://quotes.money.163.com/trade/lsjysj_'+str(key)+'.html?year='+str(year)+'&season='+str(season)
            #print(newUrl)
            #得到网页内容
            newRes = requests.get(newUrl)
            newRes.encoding = "utf-8"  # 设置网页编码
            ##处理网页结构
            soup = BeautifulSoup(newRes.text, "html.parser")
            ##找到有数据的table
            table_data = soup.select(".table_bg001")[0]
            #print("table_data:    ",table_data)

            table_data_child = table_data.children
            tchild = [i for i in table_data_child]
            ####根据特征，所有tr都大于200，所以可以根据这个特点，将需要的数据摘出来
            list_tr = [i for i in tchild if len(str(i)) > 200]
            ##将子节点全部取出来,每一个tr就是一条数据
            tr = [[i for i in list_tr[j].strings] for j in range(len(list_tr))]
            ###将每一条数据都输入到文本中，以\t分割
            for dataPerTime in tr:
                for ind in range(len(dataPerTime)):
                    print(dataPerTime[ind],file=fd,end='\t')

                print(file=fd,end='\n')
        ##year累计，直到2017
        year+=1
    fd.close()
    #600795
    #1997 - 03 - 18
    #print(r.text)
    print('你需要的数据已经存入')
    key = int(input("请输入你想要的查询的股票代码：如果没有其他需求，-1结束\n"))
