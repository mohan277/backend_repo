Find the top Actor - Directors pair.
The score for an Actor - Director pair 
is the average of ranks of movies which the director has directed 
and which the actor has acted. Consider only Actor - Director pair 
if they have worked together for at least 5 movies.

Your query should return fname of the actor, fname of the director and the score.

Your query should return first 100 such pairs when ordered in

descending order of score and then
ascending order of director fname and then
descending order of actor fname




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
ORDER BY score DESC,D.fname ASC,A.fname DESC
LIMIT 100;











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
ORDER BY score DESC,D.fname ASC,A.fname DESC
LIMIT 10;
"""