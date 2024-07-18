SELECT
    id,
    CASE
        WHEN id = (
            SELECT
                id
            FROM
                tree
            WHERE
                p_id IS NULL
        ) THEN 'Root'
        WHEN id IN (
            SELECT
                DISTINCT p_id
            FROM
                tree
        ) THEN 'Inner'
        ELSE 'Leaf'
    END AS TYPE
FROM
    tree
ORDER BY
    id ASC