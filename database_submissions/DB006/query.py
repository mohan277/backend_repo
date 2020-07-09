Q1="SELECT AVG(age) FROM Player;"

Q2="SELECT match_no, play_date FROM Match WHERE audience >50000 ORDER BY match_no ASC;"

Q3="""
SELECT
    team_id,COUNT(*) AS cnt
FROM
    MatchTeamDetails
WHERE win_lose='W'
GROUP BY team_id,win_lose
ORDER BY cnt DESC, team_id ASC;
"""

Q4="""
SELECT 
    match_no,
    play_date
FROM
    Match
WHERE stop1_sec > (SELECT AVG(stop1_sec) FROM Match)
ORDER BY match_no DESC;
"""

Q5="""
SELECT
    MC.match_no,T.name,P.name
FROM
    Team AS T
    INNER JOIN Player AS P
        ON T.team_id=P.team_id
    INNER JOIN MatchCaptain AS MC 
        ON MC.captain=P.player_id
ORDER BY MC.match_no ASC, T.name ASC;
"""

Q6="""
SELECT
    M.match_no,
    P.name,
    P.jersey_no
FROM
    Match AS M
    INNER JOIN Player AS P
        ON P.player_id=M.player_of_match
ORDER BY M.match_no ASC;
"""

Q7="""
SELECT
    T.name,
    AVG(P.age)
FROM
    Player AS P
    INNER JOIN Team AS T
        ON P.team_id=T.team_id
GROUP BY T.team_id HAVING AVG(P.age)>26
ORDER BY T.name;
"""

Q8="""
SELECT
    P.name,P.jersey_no,P.age,COUNT(GD.goal_id) AS cnt
FROM
    Player AS P
    INNER JOIN GoalDetails AS GD
        ON P.player_id=GD.player_id
WHERE P.player_id IN (SELECT player_id FROM Player WHERE age <= 27)
GROUP BY P.player_id
ORDER BY cnt DESC,P.name ASC;
"""

Q9="""
SELECT
    team_id,COUNT(goal_id)*100.0/(SELECT COUNT(goal_id) FROM GoalDetails)
FROM
    GoalDetails
GROUP BY team_id;
"""

Q10="SELECT AVG(cnt) FROM (SELECT COUNT(goal_id) AS cnt FROM GoalDetails GROUP BY team_id);"

Q11="""
SELECT
    player_id,
    name,
    date_of_birth
FROM
    Player
WHERE player_id NOT IN
    (SELECT
        player_id
    FROM
        GoalDetails
    )
ORDER BY player_id ASC;
"""

Q12="""
SELECT
    T.name,
    MTD.match_no,
    M.audience,
    M.audience -    (SELECT
                        team_avg
                    FROM
                        (SELECT
                            MTD.team_id AS t_id,
                            AVG(M.audience) AS team_avg
                        FROM
                            Match AS M
                            INNER JOIN MatchTeamDetails AS MTD
                                ON M.match_no=MTD.match_no
                        GROUP BY team_id                            
                    )AS avg
                    WHERE avg.t_id=T.team_id
                    ) AS diff
FROM
    Match AS M
    INNER JOIN MatchTeamDetails AS MTD
        ON M.match_no=MTD.match_no
    INNER JOIN Team AS T
        ON MTD.team_id=T.team_id;
"""
