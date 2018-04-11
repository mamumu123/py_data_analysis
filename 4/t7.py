import sqlite3
import numpy as np

# 连接数据库
conn = sqlite3.connect('./db/saleData.db')
#####   平均值      ##############################
query_sql = '''
SELECT
openData_Order201608.CUST_CODE,
Avg(openData_Order201608.PURCH_TAX_AMT)

FROM
openData_Order201608
GROUP BY
openData_Order201608.CUST_CODE
ORDER BY
openData_Order201608.CUST_CODE ASC
'''
query = conn.execute(query_sql)
######      方差              ############################
query_sql_per = '''
SELECT
openData_Order201608.CUST_CODE,
openData_Order201608.PURCH_TAX_AMT
FROM
openData_Order201608
ORDER BY
openData_Order201608.CUST_CODE ASC
'''
query_per = conn.execute(query_sql_per)

purch_per = []  # 用来保存每一个商家的销售额
fangcha = {}  # 用来保存每一个商家的销售额的方差
cust_code = 1  # 用来保存每一个商家的cust_code
last_custcode = 0  # 用来保存最后一个商家的cust_code
for i in query_per.fetchall():
    # 如果当前cust_code不等于之前的cust_code，则说明上一个商家的记录结束，进行处理
    if i[0] != cust_code:
        # print(purch_per)
        # 计算方差
        cust_fangcha = round(np.std(purch_per, ddof=1), 5)
        # print(cust_fangcha)
        # 用字典保存方差
        fangcha[cust_code] = cust_fangcha
        # 更新 cust_code
        cust_code = i[0]
        ##将这个[]清空
        purch_per = []
    # 保存销售额
    purch_per.append(i[1])
    last_custcode = i[0]
###在之前的操作中，没有计算最后一个商家的方差，这里加上
last_fangcha = round(np.std(purch_per, ddof=1), 5)
fangcha[last_custcode] = last_fangcha
############    写入      ##############################
filename = './txt/t7.txt'
fd = open(filename, 'w', encoding='utf-8')
print('商家', '平均', '方差', file=fd, sep=',')
# fnagchaNum=0
for kind in query:
    print(kind[0], round(kind[1], 5), fangcha[kind[0]], file=fd, sep=',')
    # fnagchaNum += 1
fd.close()
