Q1 ="""CREATE TABLE User(
    user_id INTEGER PRIMARY KEY,
    first_name VARCHAR(200) NOT NULL,
    last_name VARCHAR(200) NOT NULL,
    address VARCHAR(300) NOT NULL,
    phone_number INT
    );"""


Q2 ="""CREATE TABLE Post(
    user_id INT,
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_content VARCHAR(500) NOT NULL,
    FOREIGN KEY(user_id) REFERENCES User(user_id) ON UPDATE CASCADE ON DELETE CASCADE
    );"""
    

Q3 = "INSERT INTO User VALUES(1,'tony','stark','new york',1234567890);"

Q4 = "INSERT INTO User VALUES(2,'john','wick','la',987654321);"

Q5 = "INSERT INTO Post(user_id,post_content) VALUES(1,'my first post');"

Q6 = "SELECT * FROM User;"

Q7 = "SELECT first_name,last_name FROM User;"

Q8 = "UPDATE User SET first_name = 'thor', last_name = 'ragnarok' WHERE first_name = 'tony' AND last_name = 'stark';"

Q9 = "INSERT INTO Post(user_id,post_content) VALUES(2,'My Second Post');"

Q10 = "DELETE FROM User WHERE first_name = 'john' AND last_name = 'wick';"

Q11 = "DROP TABLE Post;"