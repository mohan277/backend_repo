Q1="SELECT fname,lname FROM Actor WHERE id IN (SELECT pid FROM Cast WHERE mid = 1000);"

Q2="SELECT COUNT(mid) FROM Cast WHERE pid IN (SELECT id FROM Actor WHERE fname = 'Harrison (I)' AND lname = 'Ford');"

Q3="SELECT DISTINCT pid FROM Cast WHERE mid IN (SELECT id FROM Movie WHERE name LIKE '%Harry Potter%');"

Q4="SELECT COUNT(DISTINCT pid) FROM Cast WHERE mid IN (SELECT id FROM Movie WHERE year >= 1990 AND year <= 2000);"


# Using JOINS

# Q1="SELECT fname,lname FROM Actor AS A INNER JOIN Cast AS C ON C.pid = A.id WHERE C.mid = 1000;"
# Q2="SELECT COUNT(C.mid) FROM Cast As C INNER JOIN Actor AS A ON A.id = C.pid WHERE A.fname = 'Harrison (I)' AND A.lname = 'Ford';"