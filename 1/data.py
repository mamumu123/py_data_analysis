#初始操作，从数据中读出需要的东西
rFile=open("50万人名名单.txt","r",encoding="utf-8",errors="ignore")
nameContent=rFile.read()
rFile.close()
nameList=nameContent.split('\n')#将名字做分割，list中的每一项都是一个名字
########################第四题######################################
#4、	针对上述list数据，按姓名字数排序，将超过4字的姓名数据删除；
#
nameLessFive=[i for i in nameList if(len(i)<5)]#列表解析，将名字长度小于5个的都摘出来
nameSort=sorted(nameLessFive, key=lambda x: len(x))#排序 ，规则，按照长度
# print(nameSort)

nameLessFiveFile=open('第四题.txt','w',encoding="utf-8",errors="ignore")
for i in nameSort:
    print(i,file=nameLessFiveFile)#输出到文件
nameLessFiveFile.close()
########################第五题#######################################
#5、针对上述list数据，统计每个姓出现的次数，不考虑复姓问题(复姓视为单姓，第一个字为姓)，按降序排列；
nameFirst={}
#思路：for in 循环，对于每一个名字，如果在之前的dict中出现过，计数+1，否则，计数为1
for name in nameList:
    if name[0] in nameFirst:#如果在之前的dict中出现过，计数+1
        nameFirst[name[0]]+=1
    else:                   #否则，计数为1
        nameFirst[name[0]]=1
#print(nameFirst)

nameFirstSort=sorted(nameFirst.items(),key=lambda x:x[1],reverse=True)#排序，规则：按姓出现的数量，逆序
#print(nameFirstSort)

nameFirstSortFile=open('第五题.txt','w',encoding="utf-8",errors="ignore")
for i in nameFirstSort:
    print(i[0],i[1],file=nameFirstSortFile,sep="\t")
nameFirstSortFile.close()

##########################第六题###########################################
#6、	针对上述list数据，统计名(姓之外的字)中每个字出现次数，相当于统计名称常用字，
# 不考虑复姓问题，按降序排列；
nameNoFirst={}
for name in nameList:#为了避过姓，所以用while做循环。对于每一个名字
    lenName=len(name)#求出每个名字的长度
    num=1             #name为1，避过姓
    while num<lenName:#对于每个名字中的字，如果之前出现过，dict+1;否则，dict=1
        if name[num] in nameNoFirst:
            nameNoFirst[name[num]]+=1
        else:
            nameNoFirst[name[num]]=1
        num+=1

nameNoFirstSort=sorted(nameNoFirst.items(),key=lambda x:x[1],reverse=True)#排序，规则：按照字出现的次数，逆序
#print(nameNoFirstSort)

nameNoFirstSortFile=open('第六题.txt','w',encoding="utf-8",errors="ignore")

for i in nameNoFirstSort:
    print(i[0],i[1],file=nameNoFirstSortFile,sep="\t")
nameNoFirstSortFile.close()
#####################第七题#################################################
#7、针对上述list数据，统计出姓名中最后一个字出现的次数，按降序排列；
nameLast={}
for name in nameList:#for in 循环 ，对于每一个名字 name[-1]为最后一个字
        if name[-1] in nameLast:#处理同上
            nameLast[name[-1]]+=1
        else:
            nameLast[name[-1]]=1
#print(nameLast)

nameLastSort=sorted(nameLast.items(),key=lambda x:x[1],reverse=True)#排序
#print(nameNoFirstSort)

nameLastSortFile=open('第七题.txt','w',encoding="utf-8",errors="ignore")
for i in nameLastSort:
    print(i[0],i[1],file=nameLastSortFile,sep="\t")
nameLastSortFile.close()
####################第八题##################################################
#8、针对上述list数据，统计名中两字重复出现的次数，
# 相当于”丽丽”出现的次数，”萌萌”出现的次数；
nameDouble={}

for name in nameList:#for in 循环  name 为每一个名字
    lenName=len(name)#while 来处理每一个名字
    num=1           #num从一开始（即第二个字）
    while num<lenName:
        if name[num]==name[num-1]:#如果这个字和前一个字相同，即重字，放入字典
                if name[num] in nameDouble:
                    nameDouble[name[num]]+=1
                else:
                    nameDouble[name[num]]=1
        num+=1
#print(nameDouble)
nameDoubleSort=sorted(nameDouble.items(),key=lambda x:x[1],reverse=True)#排序
#print(nameNoFirstSort)

nameDoubleSortFile=open('第八题.txt','w',encoding="utf-8",errors="ignore")#输出

for i in nameDoubleSort:
    print(i[0],i[1],file=nameDoubleSortFile,sep="\t")
nameDoubleSortFile.close()


