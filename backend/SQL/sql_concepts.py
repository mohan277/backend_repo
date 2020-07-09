def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor()
	crsr.execute("PRAGMA foreign_keys=on;")
	crsr.executescript(sql_query)
	connection.commit()
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor()
	crsr.execute(sql_query)
	ans= crsr.fetchall()
	connection.close()
	return ans


class Student:
	def __init__(self, name, age, score):
		self.name = name
		self.student_id = None
		self.age = age
		self.score = score


	def save(self, name=None, age=None, score=None, student_id=None):
		pass
	def get(self, name=None, age=None, score=None, student_id=None):
		pass












	# def get(self, name=None, student_id=None, age=None, score=None):
	# 	sql_query = '''

	# def get_info(self):
	# 	query1 = """
	# 	SELECT * FROM Student;
	# 	"""
	# 	info1 = read_data(query1)
	# 	print(info1)




















# def create_table():
# 	query1 = """
# 	CREATE TABLE Student(
# 		student_id INT,
#     	name VARCHAR(100),
#     	age INT
#     )
#     """
# 	query2 = """
# 	CREATE TABLE College(
# 		branch VARCHAR(100),
#     	uni VARCHAR(100),
#     	loc VARCHAR(100)
#     )
#     """
# 	write_data(query1)
# 	write_data(query2)


# def insert_data():
# 	query1 = """
# 	INSERT INTO Student VALUES(101, 'sairam', 19);
# 	INSERT INTO Student VALUES(102, 'mohan', 20);
# 	INSERT INTO Student VALUES(103, 'child', 32);
# 	INSERT INTO Student VALUES(104, 'srinu', 30);
# 	"""

# 	query2 = """
# 	INSERT INTO College VALUES('EEE', 'IIT', 'KGP');
# 	INSERT INTO College VALUES('ECE', 'IIT', 'MADRAS');
# 	INSERT INTO College VALUES('CSE', 'IIT', 'DELHI');
# 	INSERT INTO College VALUES('MT', 'IIT', 'BOMBAY');
# 	"""
# 	write_data(query1)
# 	write_data(query2)

# def update():
# 	query ="""
# 	UPDATE Student SET student_id=277,name='krish',age=15 WHERE student_id = 104;
# 	"""
# 	write_data(query)

# def get_info():
# 	query1 = """
# 	SELECT * FROM Student;
# 	"""
# 	query2 = """
# 	SELECT * FROM Student;
# 	"""

# 	info1 = read_data(query1)
# 	info2 = read_data(query2)

# 	return info1, info2

# def delete():
# 	query1 = """
# 	ALTER TABLE Student DROP COLUMN age;
# 	"""
# 	write_data(query1)


# # CREATE TABLE Student(
# # 		sid INT,
# # 		name VARCHAR(100),
# # 		login VARCHAR(100),
# # 		age INT,
# # 		gpa FLOAT
# #     );

# # INSERT INTO Student VALUES(53666,'Kanye','kayne@cs',39,4.0);
# # INSERT INTO Student VALUES(53688,'Bieber','jbieber@cs',22,3.9);
# # INSERT INTO Student VALUES(53655,'Tupac','shakur@cs',26,3.5);


# # CREATE TABLE enrolled
# # (sid INT,cid VARCHAR(100),grade VARCHAR(100))

# # INSERT INTO enrolled VALUES(53666,'15-445','C');
# # INSERT INTO enrolled VALUES(53688,'15-721','A');
# # INSERT INTO enrolled VALUES(53688,'15-826','B');
# # INSERT INTO enrolled VALUES(53666,'15-721','C');
# # INSERT INTO enrolled VALUES(53655,'15-445','B');

# # CREATE TABLE course(
# # 		cid VARCHAR(100),
# # 		name VARCHAR(100)
# #     )

# # INSERT INTO course VALUES('15-445','Database Systems');
# # INSERT INTO course VALUES('15-721','Advanced Database Systems');
# # INSERT INTO course VALUES('15-826','Data Mining');
# # INSERT INTO course VALUES('15-823','Advanced Topics in Databases');


# # SELECT COUNT(login) AS cnt
# # FROM student WHERE login LIKE '%@cs'

# # SELECT Student.sid, Student.name, enrolled.grade, Student.gpa
# # FROM Student JOIN enrolled ON Student.sid=enrolled.sid;

# # SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
# # FROM Orders
# # INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;


# SELECT * FROM Student
# RIGHT JOIN enrolled ON Student.sid=enrolled.sid;
# SELECT * FROM Student WHERE ROWNUM <= 3;
# SELECT sid FROM Student UNION SELECT  sid FROM enrolled;



# SELECT COUNT(login) AS cnt FROM Student WHERE login LIKE '%@cs';
# SELECT AVG(gpa), COUNT(sid) FROM Student WHERE login LIKE '%@cs';
# SELECT COUNT(DISTINCT login) FROM Student WHERE login LIKE '%@cs';
# SELECT AVG(s.gpa), e.cid FROM enrolled AS e, Student AS s WHERE e.sid = s.sid;