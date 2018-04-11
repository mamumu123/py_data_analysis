import sqlite3
import pandas as pd

####   main       ##################################################
##分为两个步骤，先是对数据读取后进行处理
##然后将数据放入数据库
if __name__ == '__main__':
    ##三个文件路径
    ###########  对数据读取后进行处理   ############################################################
    fileName = ['./data/openData_Order201608_afterClear.csv', './data/openData_Order201609_afterClear.csv',
                './data/openData_Order201610_afterClear.csv']
    ##对每个文件进行处理
    for index in range(3):
        ##一行行处理数据，将所需要增加的都放在后面，不影响结果，但是操作更加方便
        rFile = open(fileName[index], "r")
        # 用来临时保存数据的文件，openData_Order201608.csv
        targetFile = fileName[index][7:27] + '.csv'
        wFile = open(targetFile, "w")
        # print(targetFile)
        lineCount = 0
        dataLine = rFile.readline()  # 读取一行数据
        while dataLine:
            lineCount += 1
            # 分割数据，用来接下来的处理
            dataList = dataLine.split(",")
            # print(dataList)
            ##对第一行，即header进行处理，增加所要求的内容
            if (lineCount == 1):
                dataList.append('MONTH')
                dataList.append('YEAR')
                dataList.append('AREA_NAME')
                dataList.append('BRAND_CODE')
                # print(dataList)
            else:
                # 对具体内容进行处理，增加所要求的内容
                MONTH = (dataList[0][4:6])
                #
                YEAR = (dataList[0][0:4])
                # print(YEAR)
                AREA_NAME = 'QX' + dataList[1][-3:]
                # print(AREA_NAME)
                BRAND_CODE = dataList[3][0:6]
                # print(BRAND_CODE)
                dataList.append(MONTH)
                dataList.append(YEAR)
                dataList.append(AREA_NAME)
                dataList.append(BRAND_CODE)

                # print(dataList)
            ##将内容整理好，放入临时文件
            lineContent = ""
            rolCount = 0
            for col in dataList:
                rolCount += 1
                if (rolCount == 1):
                    lineContent += col.strip()
                else:
                    lineContent += "," + col.strip()
            # 一行行写入
            wFile.write(lineContent + "\n")
            # print(lineContent)
            dataLine = rFile.readline()
        print("数据行数=", lineCount)
        rFile.close()
        wFile.close()

        ##########       将数据放入数据库             ###################################

        # 连接数据库
        conn = sqlite3.connect("./db/saleData.db")
        ##采用pandas 的一个函数，可以很方便的直接将数据从文件中写入到数据库
        df = pd.read_csv(targetFile)
        df.to_sql(fileName[index][7:27], conn, if_exists='append', index=False)
