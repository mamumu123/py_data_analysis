import sqlite3

# 连接数据库
conn = sqlite3.connect('./db/saleData.db')
# 查询语句
query_sql = '''
SELECT
openData_Order201608.KIND,
openData_Order201608.AREA_NAME,
Sum(openData_Order201608.PURCH_TAX_AMT)
FROM
openData_Order201608
GROUP BY
openData_Order201608.KIND,
openData_Order201608.AREA_NAME
'''
##进行查询
query = conn.execute(query_sql)
##将查询结果写入
filename = './txt/areaKind.txt'
fd = open(filename, 'w', encoding='utf-8')
print('烟的种类', '县区', '销售利润', file=fd, sep=',')
for kind in query:
    print(kind[0], kind[1], kind[2], file=fd, sep=',')
fd.close()
# print(query[1][1])
