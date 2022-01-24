import sqlite3
from student import *

s = Students("moris","zerach", 25, 85)
s2 = Students("tal", "baz", 27, 90)
s3 = Students("alan", "tzipim", 25 , 100)
sq = sqlite3.connect("Students_db.db")
c = sq.cursor()

c.execute("""CREATE TABLE students (
            "first name" text,
            "last name" text,
            age integer ,
            grade integer )
            """)

c.execute("INSERT INTO students VALUES ('{}', '{}', {}, {})".format(s.get_name(),s.get_lname(),s.get_age(),s.get_grade()))

c.execute("INSERT INTO students VALUES ('{}', '{}', {}, {})".format(s2.get_name(),s2.get_lname(),s2.get_age(),s2.get_grade()))

c.execute("INSERT INTO students VALUES ('{}', '{}', {}, {})".format(s3.get_name(),s3.get_lname(),s3.get_age(),s3.get_grade()))

c.execute("SELECT * FROM students")
print(c.fetchall())

sq.commit()

sq.close()