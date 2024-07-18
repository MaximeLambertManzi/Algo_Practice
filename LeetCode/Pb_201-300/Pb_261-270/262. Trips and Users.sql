# Write your MySQL query statement below
WITH temp1 AS (
    SELECT
        id,
        client_id,
        driver_id,
        city_id,
        STATUS,
        request_at
    FROM
        Trips
        LEFT JOIN Users ON Trips.client_id = Users.users_id
    WHERE
        Users.banned LIKE "No"
        AND Trips.Request_at BETWEEN '2013-10-01'
        AND '2013-10-03'
),
temp2 AS(
    SELECT
        id
    FROM
        Trips
        LEFT JOIN Users ON Trips.driver_id = Users.users_id
    WHERE
        Users.banned LIKE "No"
        AND Trips.Request_at BETWEEN '2013-10-01'
        AND '2013-10-03'
)
SELECT
    request_at AS DAY,
    ROUND(
        SUM(
            CASE
                WHEN STATUS LIKE "%cancelled%" THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS "Cancellation Rate"
FROM
    temp1 t1
    JOIN temp2 t2 ON t1.id = t2.id
GROUP BY
    t1.request_at