SELECT
    n.name,
    SUM(t.amount) AS balance
FROM Users n
JOIN Transactions t
    ON n.account = t.account
GROUP BY n.account, n.name
HAVING SUM(t.amount) > 10000;