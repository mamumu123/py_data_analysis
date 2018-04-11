import requests
from bs4 import BeautifulSoup
####  获取网页内容
url = 'http://www.pku.edu.cn'#定义url
res = requests.get(url)
res.encoding = "utf-8"  # 设置网页编码

####       开始处理网页内容   ########################
soup = BeautifulSoup(res.text, "html.parser")

#print(soup)
#查找带有href的链接
a_include_href=soup.select('a[href]')
#用来保存链接
dictA={}
#对每一个链接进行处理
for include_a in a_include_href:
    #name 就是include_a.get_text()，href=include_a.attrs['href']
    name=include_a.get_text()
    href=str(include_a.attrs['href'])
    # 做一些判断 按照要求，href开头不能为#，href中不能含有javascript/vbscript，有一些图片，直接删除
    if  (href !='') and (href[0]!='#')and ('javascript' not in href )and ('vbscript'  not in href )and (name!="")and( 'img' not in name ):
        # 做一些优化，如果连接不完整，则补上前缀
        if href[0:4] != 'http':
            tem = 'http://www.pku.edu.cn/' + href
            dictA[name] = tem
        else:
            dictA[name]=href
#######                输出保存           ##########################################################
num_A=0
for i in dictA:
    if(i.strip(' ')!='' ):
        print(i, dictA[i],sep="   ")
        num_A+=1
print("num_ral   :",num_A)
#print(dictA[''])

fd=open('./txt/3.txt','w',encoding='utf-8')
for i in dictA:
    print(i,dictA[i],file=fd,sep="\t")
fd.close()