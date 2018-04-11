import sqlite3

# 连接数据库
conn = sqlite3.connect('./db/saleData.db')
# 查询语句
query_sql = '''
SELECT
openData_Order201608.CUST_CODE,
Sum(openData_Order201608.PURCH_TAX_AMT)
FROM
openData_Order201608
GROUP BY
openData_Order201608.CUST_CODE
ORDER BY
SUM(PURCH_TAX_AMT) DESC
'''
# 查询
query = conn.execute(query_sql)

# 遍历一遍，计算商家数量
num_cust = 0
for kind in query:
    num_cust += 1
# 一个很有趣的现象，如果查询结果被遍历一边，然后query就为[],所以需要再遍历一遍
query_again = conn.execute(query_sql)
numAgain = 0
# 每个等分中 商家的销售额
sumPer = [0 for i in range(5)]
# print(query.fetchall())
for Per in query_again:
    index = int(numAgain / (num_cust / 5))
    # print(index)
    sumPer[index] += Per[1]
    # print('-'*16)
    numAgain += 1
# 保存所要求的倍数
rate = []
for index in range(5):
    # 计算倍数，写入list
    rate.append(round(sumPer[0] / sumPer[index], 3))
    print(rate[index])
# print(sumPer)

##写入
filename = './txt/t8.txt'
fd = open(filename, 'w', encoding='utf-8')
print('等分', '比值', file=fd, sep=',')
for index in range(5):
    print(index, rate[index], file=fd, sep=',')
fd.close()
