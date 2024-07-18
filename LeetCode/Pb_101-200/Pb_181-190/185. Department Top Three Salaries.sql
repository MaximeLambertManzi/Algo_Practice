SELECT
    Department,
    Employee,
    Salary
FROM
    (
        SELECT
            d.name AS Department,
            e.name AS Employee,
            e.salary AS Salary,
            DENSE_RANK() OVER (
                PARTITION BY d.name
                ORDER BY
                    e.salary DESC
            ) AS Rnk
        FROM
            Employee e
            JOIN Department d ON e.departmentId = d.id
        ORDER BY
            d.name,
            e.salary DESC
    ) AS temp
WHERE
    Rnk <= 3