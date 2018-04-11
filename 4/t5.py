import sqlite3

##连接数据库
conn = sqlite3.connect('./db/saleData.db')

##对每个月的查询分开处理，先是8月##############################################
query_sql = '''
SELECT
openData_Order201608.ITEM_CODE,
sum(openData_Order201608.PURCH_QTY),
sum(openData_Order201608.PURCH_TAX_AMT)/sum(openData_Order201608.PURCH_QTY)
FROM
openData_Order201608
GROUP BY
openData_Order201608.ITEM_CODE
'''
query = conn.execute(query_sql)

filename = './txt/t5.txt'
num = 0
fd = open(filename, 'w', encoding='utf-8')
print('月', '规格', '数量', '单价', file=fd, sep=',')
for kind in query:

    if (kind[1] == 0):
        continue
    num += 1
    print('8月', kind[0], kind[1], kind[2], file=fd, sep=',')
print(num)
####################   9月    ############################################
query_sql = '''
SELECT
openData_Order201609.ITEM_CODE,
openData_Order201609.PURCH_QTY,
openData_Order201609.PURCH_TAX_AMT/openData_Order201609.PURCH_QTY
FROM
openData_Order201609
GROUP BY
openData_Order201609.ITEM_CODE
'''
query = conn.execute(query_sql)

filename = './txt/t5.txt'
num = 0
fd = open(filename, 'a', encoding='utf-8')
# print('月','规格','数量','单价',file=fd,sep=',')
for kind in query:

    if (kind[1] == 0):
        continue
    num += 1
    print('9月', kind[0], kind[1], kind[2], file=fd, sep=',')
print(num)
#######################    10月  ##################################################
query_sql = '''
SELECT
openData_Order201610.ITEM_CODE,
openData_Order201610.PURCH_QTY,
openData_Order201610.PURCH_TAX_AMT/openData_Order201610.PURCH_QTY
FROM
openData_Order201610
GROUP BY
openData_Order201610.ITEM_CODE
'''
query = conn.execute(query_sql)

filename = './txt/t5.txt'
num = 0
fd = open(filename, 'a', encoding='utf-8')
# print('月','规格','数量','单价',file=fd,sep=',')
for kind in query:

    if (kind[1] == 0):
        continue
    num += 1
    print('10月', kind[0], kind[1], kind[2], file=fd, sep=',')
print(num)
fd.close()
