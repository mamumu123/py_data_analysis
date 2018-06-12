import sqlite3


# tbPerson tbLesson tbTeach tbChoice tbScore
def get_count_message():
    conn = sqlite3.connect('./db/course.db')
    nameTable = ['tbPerson', 'tbLesson', 'tbTeach', 'tbChoice', 'tbScore']
    tem = {}
    for i in range(5):
        sql = """
       SELECT COUNT(*) FROM %s
        """
        query = conn.execute(sql % nameTable[i])
        for coun in query:
            tem[nameTable[i]] = coun[0]
    # print(tem)
    conn.close()
    return tem


def get_all_message():
    conn = sqlite3.connect('./db/course.db')
    nameTable = ['tbPerson', 'tbLesson', 'tbTeach', 'tbChoice', 'tbScore']
    tem = {}
    for i in range(5):
        sql = """
       SELECT * FROM %s
        """
        query = conn.execute(sql % nameTable[i])
        tem[nameTable[i]] = query.fetchall()
    sql = """ SELECT * FROM tbPerson  WHERE  tbPerson.pType = 'T'  """
    query = conn.execute(sql)
    tem['teacher'] = query.fetchall()
    sql = """ SELECT * FROM tbPerson  WHERE  tbPerson.pType = 'S'  """
    query = conn.execute(sql)
    tem['student'] = query.fetchall()
    conn.close()
    # print(tem)
    return tem


def insert_teach(cID, pID):
    conn = sqlite3.connect('./db/course.db')
    nameTable = 'tbTeach'
    sql = """insert into tbTeach values(%d,%d)"""
    query = conn.execute(sql % (cID, pID))
    conn.commit()
    conn.close()


def insert_choice(cID, pID):
    conn = sqlite3.connect('./db/course.db')
    sql = """insert into tbChoice values(%d,%d)"""
    query = conn.execute(sql % (cID, pID))
    conn.commit()
    conn.close()


##get  lesson 学号 姓名 成绩
def select_lesson(lesson_id):
    conn = sqlite3.connect('./db/course.db')
    person = {}
    sql = """
SELECT
tbPerson.pID,
tbPerson.Name
FROM
tbPerson ,
tbChoice
WHERE
tbPerson.pID = tbChoice.pID AND
tbChoice.cID=%d """
    query = conn.execute(sql % lesson_id)
    for coun in query:
        person[coun[0]] = coun[1]
    # print(person)
    conn.close()
    return person


def query_all_stu():
    tem = {}
    conn = sqlite3.connect('./db/course.db')
    sql = """ SELECT * FROM tbPerson  WHERE  tbPerson.pType = 'S'  """
    query = conn.execute(sql)
    for i in query:
        tem[i[0]] = i
    conn.close()
    print(tem)
    return tem


def query_all_tea():
    tem = {}
    conn = sqlite3.connect('./db/course.db')
    sql = """ SELECT * FROM tbPerson  WHERE  tbPerson.pType = 'T'  """
    query = conn.execute(sql)
    for i in query:
        tem[i[0]] = i
    conn.close()
    print(tem)
    return tem


def query_name(name):
    print('query_name', name)
    tem = {}
    conn = sqlite3.connect('./db/course.db')
    sql = """ SELECT * FROM tbPerson  WHERE  tbPerson.name like '%s' """
    query = conn.execute(sql % name)
    for i in query:
        tem[i[0]] = i
    conn.close()
    print(tem)
    return tem


def query_stuto():
    tem = {}
    conn = sqlite3.connect('./db/course.db')
    sql = """SELECT
tbPerson.pID,
tbPerson.Name,
tbLesson.cID,
tbLesson.cName
FROM
tbPerson ,
tbLesson ,
tbChoice
WHERE
tbPerson.pType = 'S' AND
tbPerson.pID = tbChoice.pID AND
tbLesson.cID = tbChoice.cID"""
    query = conn.execute(sql)
    for i in query:
        tem[i[0]] = i
    conn.close()
    print(tem)
    return tem


def query_teato():
    tem = {}
    conn = sqlite3.connect('./db/course.db')
    sql = """SELECT
    tbLesson.cID,
    tbLesson.cName,
    tbPerson.pID,
    tbPerson.Name
    FROM
    tbPerson ,
    tbTeach ,
    tbLesson
    WHERE
    tbPerson.pID = tbTeach.pID AND
    tbTeach.cID = tbLesson.cID AND
    tbPerson.pType = 'T'"""
    query = conn.execute(sql)
    for i in query:
        tem[i[0]] = i
    conn.close()
    print(tem)
    return tem


def add_score(no, cID, dataForm):
    conn = sqlite3.connect('./db/course.db')
    for i in range(len(cID)):
        sql = """insert into tbScore (cID,pID,Score)
        values (%d,%d,%d)"""
        conn.execute(sql % (int(no), int(cID[i]), int(dataForm[i])))
        conn.commit()
    conn.close()
