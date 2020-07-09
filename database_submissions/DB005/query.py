Q1="SELECT COUNT(name) FROM Movie WHERE year < 1980;"

Q2="SELECT AVG(rank) FROM Movie WHERE year = 1991;"

Q3="SELECT MIN(rank) FROM Movie WHERE year = 1991;"

Q4="SELECT fname,lname FROM Actor WHERE id IN (SELECT pid FROM Cast WHERE mid = 1002);"

Q5="SELECT COUNT(mid) FROM Cast WHERE pid IN (SELECT id FROM Actor WHERE fname = 'Orlando' AND lname = 'Galindo');"

Q6="SELECT name FROM Movie WHERE (year BETWEEN 2006 AND 2008) AND name LIKE 'Harry Potter%';"

Q7="SELECT DISTINCT fname,lname FROM Director WHERE id IN (SELECT did FROM MovieDirector WHERE mid IN (SELECT id FROM Movie WHERE name LIKE 'Harry Potter%'));"

Q8="SELECT name FROM Movie WHERE id IN (SELECT mid FROM MovieDirector WHERE did IN (SELECT id FROM Director WHERE fname = 'Jackie (I)' AND lname = 'Chan')) AND id IN(SELECT mid FROM Cast WHERE pid IN (SELECT id FROM Actor WHERE fname = 'Jackie (I)' AND lname = 'Chan')) ORDER BY name ASC;"

Q9="""
SELECT
    fname,lname
FROM 
    Director AS D 
    INNER JOIN MovieDirector AS MD
        ON D.id = MD.did
    INNER JOIN Movie AS M
        ON MD.mid = M.id
WHERE year = 2001
GROUP BY D.id HAVING COUNT(M.id)>=4 
ORDER BY fname ASC,lname DESC;
"""

Q10="SELECT * FROM Actor WHERE id NOT IN (SELECT pid FROM Cast WHERE mid IN (SELECT id FROM Movie WHERE year BETWEEN 1990 AND 2000))ORDER BY id DESC  LIMIT 100;"

Q11="SELECT gender,(COUNT(gender) * 100.0)/(SELECT COUNT(*) FROM Actor)FROM Actor GROUP BY gender ORDER BY gender DESC;"

Q12="""
SELECT
    m1.name,m2.name,m1.rank,m1.year
FROM
    Movie AS m1
    INNER JOIN Movie AS m2
        ON m1.year=m2.year AND m1.rank=m2.rank
WHERE m1.id > m2.id
LIMIT 100;
"""


Q13="""
SELECT
    A.fname,
    M.year,
    AVG(M.rank)
FROM
    Actor AS A 
    INNER JOIN Cast AS C
        ON A.id=C.pid
    INNER JOIN Movie AS M
        ON M.id=C.mid
GROUP BY M.year,A.id
ORDER BY A.fname ASC, M.year DESC
LIMIT 100;
"""


Q14="""
SELECT
    d_name,m_name
FROM(
    SELECT
        sq_d.fname AS d_name,sq_m.name AS m_name
    FROM 
        Movie AS sq_m
        INNER JOIN MovieDirector AS sq_md
            ON sq_md.mid=sq_m.id
        INNER JOIN Director AS sq_d
            ON sq_d.id=sq_md.did
    GROUP BY sq_md.did HAVING MAX(sq_m.rank)
    ORDER BY sq_m.name ASC
    )
LIMIT 100;
"""


Q15="""
SELECT 
    D.id,
    D.fname
FROM 
    Director AS D
    INNER JOIN MovieDirector AS MD
        ON D.id=MD.did
    INNER JOIN Movie AS M
        ON M.id=MD.mid
WHERE m.year >2005 AND d.id NOT IN
        (SELECT
            D.id 
        FROM
            Director AS D
            INNER JOIN MovieDirector AS MD
                ON D.id=MD.did
            INNER JOIN Movie AS M
            ON M.id=MD.mid
        WHERE year < 2005);
"""


Q16="""
SELECT
    A.fname,
    D.fname,
    AVG(M.rank) AS score
FROM
    Director AS D
    INNER JOIN MovieDirector AS MD
        ON MD.did=D.id
    INNER JOIN Movie AS M
        ON M.id=MD.mid
    INNER JOIN Cast AS C
        ON M.id=C.mid
    INNER JOIN Actor AS A
        ON A.id=C.pid
GROUP BY D.id,A.id HAVING COUNT(*) >= 5
ORDER BY score DESC,D.fname ASC,A.fname DESC LIMIT 100;
"""















# USING JOINS

# Q4="SELECT fname,lname FROM Actor AS A INNER JOIN Cast AS C ON A.id=C.pid WHERE C.mid=1002;"

# Q8="""SELECT name FROM Movie AS M INNER JOIN Cast AS C ON M.id = C.mid
# INNER JOIN Actor AS A ON A.id = C.pid
# INNER JOIN MovieDirector AS MD ON MD.mid = C.mid
# INNER JOIN Director AS D ON D.id = MD.did
# WHERE A.fname = 'Jackie (I)' AND A.lname = 'Chan' AND D.fname = 'Jackie (I)' AND D.lname = 'Chan'
# ORDER BY name ASC;
# """