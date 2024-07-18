SELECT
    customer_number
FROM
    (
        SELECT
            customer_number,
            COUNT(*) AS num_orders
        FROM
            Orders
        GROUP BY
            customer_number
        ORDER BY
            num_orders DESC
    ) AS temp
LIMIT
    1