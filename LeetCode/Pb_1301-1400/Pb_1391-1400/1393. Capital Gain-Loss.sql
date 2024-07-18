SELECT
    stock_name,
    SUM(capital_gain) AS capital_gain_loss
FROM
    (
        SELECT
            stock_name,
            CASE
                WHEN operation LIKE 'Buy' THEN - capital
                ELSE capital
            END capital_gain
        FROM
            (
                SELECT
                    stock_name,
                    operation,
                    SUM(price) AS capital
                FROM
                    Stocks
                GROUP BY
                    stock_name,
                    operation
                ORDER BY
                    stock_name
            ) t
    ) t2
GROUP BY
    stock_name