# Write your MySQL query statement below
select stock_name,
sum(case
when operation="Buy" then -price
when operation="Sell" then price
END )AS CAPITAL_GAIN_LOSS
FROM STOCKS
GROUP BY STOCK_NAME