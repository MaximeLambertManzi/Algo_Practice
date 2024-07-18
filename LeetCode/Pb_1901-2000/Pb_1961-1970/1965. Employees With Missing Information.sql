SELECT
    *
FROM
    (
        SELECT
            t1.employee_id
        FROM
            employees t1
            LEFT JOIN salaries t2 ON t1.employee_id = t2.employee_id
        WHERE
            t2.salary IS NULL
        UNION
        SELECT
            t2.employee_id
        FROM
            employees t1
            RIGHT JOIN salaries t2 ON t1.employee_id = t2.employee_id
        WHERE
            t1.name IS NULL
    ) AS res
ORDER BY
    employee_id ASC