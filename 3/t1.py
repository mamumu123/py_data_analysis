import requests
###  获取网页内容
url = 'http://www.pku.edu.cn'#定义url
res = requests.get(url)
res.encoding = "utf-8"  # 设置网页编码
###将网页内容整合为一行
strTxt=res.text.replace('\n','')

###       开始处理字符串    ##############
#分割字符串
allFind=strTxt.split(r"</a>")
#用字典来保存链接
dictA={}
#对每一个含有链接的str做处理
for include_a in allFind:
    #寻找链接的开始位置
    if('<a' in include_a ):
        #找到<a,并把之前的（没用的）都截断
        index_a=include_a.index('<a ')
        tem=include_a[index_a:]
        #找到’>‘，这样>后面的就是链接名称
        if ('href' in tem and '>' in tem ):
            #print(tem)
            #这样一分割，nameList[1]就是名称
            nameList = tem.split('>')
            name=nameList[1]
            #print(name[1])
            ##再次分割，href的后“之前的就是需要的东西
            index_href=nameList[0].index('href')
            ##+6直接去掉    href="
            hrefList=nameList[0][index_href+6:].split("\"")
            #href就是  hrefList[0]
            href=hrefList[0]
            #print(href[0])
            #做一些判断 按照要求，href开头不能为#，href中不能含有javascript/vbscript，有一些图片，直接删除
            if (href != '') and (href[0]!= '#') and ('javascript' not in href) and (
                'vbscript' not in href) and 'img'not in name and name!="":
                #做一些优化，如果连接不完整，则补上前缀
                if href[0:4]!='http':
                    href='http://www.pku.edu.cn/'+href
                dictA[name]=href
            #print('------------------------------')
#######                输出保存           ##########################################################
numA=0
for i in dictA:
    print(i,dictA[i],sep="    ")
    numA+=1
print(numA)

fd=open('./txt/1.txt','w',encoding='utf-8')
for i in dictA:
    print(i,dictA[i],file=fd,sep="\t")
fd.close()