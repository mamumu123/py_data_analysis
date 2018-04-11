import sqlite3

# 连接数据库
conn = sqlite3.connect('./db/saleData.db')
###############################################
##对每个月的查询分开处理，先是8月
# 查询语句
query_sql = '''
SELECT
openData_Order201608.CUST_CODE,AVG(PURCH_TAX_AMT)
FROM
openData_Order201608
GROUP BY
openData_Order201608.CUST_CODE
'''
##查询
query = conn.execute(query_sql)
##将查询结果进行写入
filename = './txt/t4.txt'
num = 0
fd = open(filename, 'w', encoding='utf-8')
print('月份', '商家', '销售利润', file=fd, sep=',')
for kind in query:
    num += 1
    print('8月', kind[0], kind[1], file=fd, sep=',')
print('8月商户数量：', num)
###################     9月     ######################################
query_sql = '''
SELECT
openData_Order201609.CUST_CODE,AVG(PURCH_TAX_AMT)
FROM
openData_Order201609
GROUP BY
openData_Order201609.CUST_CODE
'''
query = conn.execute(query_sql)

filename = './txt/t4.txt'
num = 0
fd = open(filename, 'a', encoding='utf-8')
# print('月份','商家','销售利润',file=fd,sep=',')
for kind in query:
    num += 1
    print('9月', kind[0], kind[1], file=fd, sep=',')
print('9月商户数量：', num)
###################       10月    ####################################
query_sql = '''
SELECT
openData_Order201610.CUST_CODE,AVG(PURCH_TAX_AMT)
FROM
openData_Order201610
GROUP BY
openData_Order201610.CUST_CODE
'''
query = conn.execute(query_sql)

filename = './txt/t4.txt'
num = 0
fd = open(filename, 'a', encoding='utf-8')
# print('月份','商家','销售利润',file=fd,sep=',')
for kind in query:
    num += 1
    print('10月', kind[0], kind[1], file=fd, sep=',')
print('10月商户数量：', num)

fd.close()
