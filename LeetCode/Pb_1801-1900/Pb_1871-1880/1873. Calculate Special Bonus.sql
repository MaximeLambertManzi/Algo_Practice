SELECT
     employee_id,
     CASE
          WHEN employee_id % 2 != 0
          AND name not like 'm%' THEN salary
          ELSE 0
     END AS bonus
FROM
     employees
ORDER BY
     employee_id