SELECT
    u.user_id AS buyer_id,
    u.join_date,
    COUNT(order_date) AS orders_in_2019
FROM
    Users u
    LEFT JOIN(
        SELECT
            o.buyer_id,
            u.join_date,
            o.order_date
        FROM
            Users u
            LEFT JOIN Orders o ON u.user_id = o.buyer_id
        WHERE
            YEAR(o.order_date) = 2019
    ) t ON u.user_id = t.buyer_id
GROUP BY
    u.user_id,
    t.join_date