import requests
import re
####  获取网页内容    ############################
url = 'http://www.pku.edu.cn'#定义url
res = requests.get(url)
res.encoding = "utf-8"  # 设置网页编码
###将网页内容整合为一行
strTxt=res.text.replace('\n','')

###       开始处理字符串    ########################
#找到所有的链接
allFind=re.findall(r"<a .*?</a>",strTxt)
#用来保存最后的链接
dictA={}
#对每个含有链接的字符串进行处理
for include_a in allFind:
    ##分割字符串，则split_a[2]为名称，split_a[1]为含有href的字符串
    split_a=re.split('>|<',include_a)
    #print(con[2], con[1], sep="   $$$$$  ")
    #保存名称
    name=split_a[2]
    #只处理名字不为空且含有href的字符串
    if len(name)>0 and 'href' in split_a[1]:
        #print(con[1])
        #正则表达式，将href匹配出来
        match_include_href=re.search(r'href=".*?"',split_a[1])
        #处理一些奇怪的异常，
        if match_include_href is None:
            continue
        #截取""的东西
        match_include_yinhao = re.search(r'".*?"', match_include_href.group())
        #去掉左右两边的引号
        strHref=match_include_yinhao.group().strip('"')
        # 做一些判断 按照要求，href开头不能为#，href中不能含有javascript/vbscript，有一些图片，直接删除
        if (strHref !='') and (strHref[0]!='#')and ('javascript' not in strHref )and ('vbscript'  not in strHref):
            # 做一些优化，如果连接不完整，则补上前缀
            if strHref[0:4] != 'http':
                strHref = 'http://www.pku.edu.cn/' + strHref
            dictA[name] = strHref
            #print('------------------------------------')
#######                输出保存           ##########################################################
numA=0

for i in dictA:
    print(i,dictA[i],sep="    ")
    numA+=1

print(numA)

fd=open('./txt/2.txt','w',encoding='utf-8')
for i in dictA:
    print(i,dictA[i],file=fd,sep="\t")
fd.close()