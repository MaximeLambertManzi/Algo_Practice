SELECT
    Users.name,
    CASE
        WHEN SUM(Rides.distance) IS NULL THEN 0
        ELSE SUM(Rides.distance)
    END travelled_distance
FROM
    Users
    LEFT JOIN Rides ON Users.id = Rides.user_id
GROUP BY
    Users.id
ORDER BY
    travelled_distance DESC,
    Users.name