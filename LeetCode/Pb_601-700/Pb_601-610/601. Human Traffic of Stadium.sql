# Write your MySQL query statement below
WITH cte1 AS (
    SELECT
        id,
        visit_date,
        people
    FROM
        (
            SELECT
                *,
                LEAD(people, 1) OVER w AS 'lead_1',
                LEAD(people, 2) OVER w AS 'lead_2'
            FROM
                Stadium window w AS (
                    ORDER BY
                        id
                )
        ) AS temp1
    WHERE
        people >= 100
        AND lead_1 >= 100
        AND lead_2 >= 100
),
cte2 AS(
    SELECT
        id,
        visit_date,
        people
    FROM
        (
            SELECT
                *,
                LAG(people, 1) OVER w AS 'lag_1',
                LAG(people, 2) OVER w AS 'lag_2'
            FROM
                Stadium window w AS (
                    ORDER BY
                        id
                )
        ) AS temp2
    WHERE
        people >= 100
        AND lag_1 >= 100
        AND lag_2 >= 100
),
cte3 AS (
    SELECT
        id,
        visit_date,
        people
    FROM
        (
            SELECT
                *,
                LEAD(people, 1) OVER w AS 'lead_1',
                LAG(people, 1) OVER w AS 'lag_1'
            FROM
                Stadium window w AS (
                    ORDER BY
                        id
                )
        ) AS temp3
    WHERE
        people >= 100
        AND lead_1 >= 100
        AND lag_1 >= 100
)
SELECT
    id,
    visit_date,
    people
FROM
    cte1
UNION
SELECT
    id,
    visit_date,
    people
FROM
    cte2
UNION
SELECT
    id,
    visit_date,
    people
FROM
    cte3
ORDER BY
    visit_date ASC