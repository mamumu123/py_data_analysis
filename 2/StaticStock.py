import requests
import re
from bs4 import BeautifulSoup

####   第一题   ######################################
#调用requests来爬取网页
url = 'http://quotes.money.163.com/0600795.html'#定义url
res = requests.get(url)
res.encoding = "utf-8"  # 设置网页编码
# 字符串处理，得到   0600795.html
filename = url.split('/')[-1]
#保存网页
fd = open(filename, 'w', encoding='utf-8', errors='ignore')
print(res.text, file=fd)
fd.close()
##########    第二题   ###########################
##调用BeautifulSoup来处理网页
soup = BeautifulSoup(open(filename, encoding='utf-8'), "html.parser")
##找到类名为 corp_info 的table
tag1 = soup.select(".corp_info")
ch = []
for child in tag1[0].strings:
    ch.append(child)
##正则匹配，得到日期
mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", (ch[19]))
##输出日期
print('这一只股票首次上市的时间:\n',mat.group())
#############   第三题       ################################
##调用requests来爬取网页
url = 'http://quotes.money.163.com/trade/lsjysj_600795.html?year=2016&season=1'
res = requests.get(url)
res.encoding = "utf-8"  # 设置网页编码
##正则表达式得到股票代号  年   季度
filename = url.split('/')[-1].split('?')
tem = filename[1].split('&')
##正则匹配
mat = re.search(r"(\d+)", (filename[0]))
##no  股票代号
no = mat.group()

mat = re.search(r"(\d+)", (tem[0]))
##year  年
year = mat.group()
mat = re.search(r"(\d+)", (tem[1]))
##season  季度
season = mat.group()
# print('year:',year,'\nsession',session,'\nno',no)
#根据题目要求，将这些分别连接起来，组成filename
filename = no + '_' + year + '_' + season + '.html'
##将数据存入文件
fd=open(filename,'w',encoding='utf-8',errors='ignore')
print(res.text,file=fd)
fd.close()
##调用BeautifulSoup来处理网页
soup = BeautifulSoup(open(filename, encoding='utf-8'), "html.parser")
##利用class得到表格及其内容
table = soup.select(".table_bg001")[0]
table_child = table.children
table_content = [i for i in table_child]
##根据特征，所有tr都大于200，所以可以根据这个特点，将需要的数据摘出来

list_tr = [i for i in table_content if len(str(i)) > 200]
##将子节点全部取出来,每一个tr就是一条数据
tr = [[i for i in list_tr[j].strings] for j in range(len(list_tr))]
#print(tr)
##利用列表解析和切片，得到规定要求的数据格式
dataPerTime = [(i[0], tuple(i[1:])) for i in tr]

import pickle
##将最后得到的数据有pickle保存，用eval还原即可使用
fd = open('./dataPerTime.txt', 'wb')
pickle.dump(str(dataPerTime), fd)
fd.close()
#########   第四题   #################################################################3
##循环读入，直到-1结束
##然后会在命令行输出想要的排序结果
key=int(input("请输入你想要的排序顺序：\n1:以日期为序\n2：以成交量为序\n3：以成交金额为序\n.......\n如果没有其他需求，-1结束\n"))
#当输入一个数，且不是-1
while(key!=-1):

#处理边界
    if(key>11):#上界
        key=1
    if(key<-1 or key==0):#下界
        key=1
    ###根据输入的值，进行排序
    dataSort=sorted(tr,key=lambda x:x[key-1])
    ##按照规定格式进行输出
    dataPerTimeSort = [(i[0], tuple(i[1:])) for i in dataSort]
    for item in dataPerTimeSort:
        print(item)
    key=int(input("请输入你想要的排序顺序：\n1:以日期为序\n2：以成交量为序\n3：以成交金额为序\n.......\n如果没有其他需求，-1结束\n"))
