SELECT
    name
FROM
    SalesPerson
WHERE
    name NOT IN (
        SELECT
            SalesPerson.name
        FROM
            SalesPerson
            JOIN Orders ON SalesPerson.sales_id = Orders.sales_id
            JOIN Company ON Orders.com_id = Company.com_id
        WHERE
            Company.name LIKE 'RED'
    )