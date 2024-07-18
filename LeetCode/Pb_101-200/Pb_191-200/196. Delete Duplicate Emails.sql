DELETE FROM
    person
WHERE
    id NOT IN (
        SELECT
            *
        FROM
            (
                SELECT
                    MIN(id)
                FROM
                    person p1
                GROUP BY
                    email
            ) AS Tmp
    )