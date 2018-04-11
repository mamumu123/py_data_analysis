import numpy
import sqlite3

# 连接数据库
conn = sqlite3.connect('./db/saleData.db')
##由于需要知道每一个商家的销售额占总销售额的比例，所以需要查询两次
# 第一次   每一个商家的销售额
query_sql = '''
SELECT
openData_Order201608.CUST_CODE,
Sum(openData_Order201608.PURCH_TAX_AMT)
FROM
openData_Order201608
GROUP BY
openData_Order201608.CUST_CODE
ORDER BY
Sum(openData_Order201608.PURCH_TAX_AMT) DESC


'''
query = conn.execute(query_sql)
# 第二次   总的销售额
query_sql_total = '''
SELECT
Sum(openData_Order201608.PURCH_TAX_AMT)
FROM
openData_Order201608
'''
query_total = conn.execute(query_sql_total)
total_sum = query_total.fetchone()[0]
##      写入     ####################################################
filename = './txt/t6.txt'
num_total = 0  # 总的商家数
fd = open(filename, 'w', encoding='utf-8')
print('商户', '销售金额', '占比', file=fd, sep=',')
zhanbi_rate = 0  # 销售收入占比率
flag_num = 0  # 当超过80时，商家的个数
flag = 0  # 用来标记第一次超过80%
for kind in query:
    num_total += 1
    zhanbi = round((kind[1]) / (total_sum) * 100, 5)
    # 百分比    保留五位小数
    zhanbi_rate += zhanbi
    if zhanbi_rate > 80 and flag == 0:
        flag_num = num_total
        print('当商户的销售占比率超过80%,商户的数量:    ', flag_num)
        flag = 1
    print(kind[0], kind[1], zhanbi, file=fd, sep=',')
print('总的商户数量   :', num_total)
print('商户占比率   ', round(flag_num / num_total, 5))
