import sqlite3
#在这一道题中，我想要看一下每一类烟的平均单价与销售数量，看看有什么联系
##连接数据库
conn = sqlite3.connect('./db/saleData.db')

##对每个月的查询分开处理，先是8月##############################################
query_sql = '''
SELECT
openData_Order201608.BRAND_CODE,
Sum(openData_Order201608.PURCH_TAX_AMT)/Sum(openData_Order201608.PURCH_QTY),
Sum(openData_Order201608.PURCH_QTY)
FROM
openData_Order201608
GROUP BY
openData_Order201608.BRAND_CODE
ORDER BY
Sum(openData_Order201608.PURCH_TAX_AMT)/Sum(openData_Order201608.PURCH_QTY) DESC
'''
query = conn.execute(query_sql)

filename = './txt/t9.txt'
num = 0
fd = open(filename, 'w', encoding='utf-8')
print( '品牌', '单价', '数量', file=fd, sep=',')
for kind in query:
    if (kind[1] == 0):
        continue
    num += 1
    print( kind[0], kind[1], kind[2], file=fd, sep=',')
print(num)