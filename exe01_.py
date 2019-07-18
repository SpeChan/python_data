'''
    将字典存入数据库
    1.创建数据库 dict (utf8)
    2.创建数据表 words 将单词和单词解释分别存入不同的字点
    3.将单词存入words单词表 超过19500条即可
'''

import pymysql
import re

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

cur = db.cursor()

f = open('dict.txt')
while True:
    line = f.readline()
    if not line:
        break
    word = line.split(' ')[0]
    mean = ' '.join(line.split(' ')[1:])
    try:
        sql = 'insert into words(word,mean)' \
              'values(%s,%s)'
        cur.execute(sql,[word,mean])
        db.commit()
    except Exception as  e:
        db.rollback()
        print(e)



# print(word)
# print(mean.strip())
































































