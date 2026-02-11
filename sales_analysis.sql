--Q1.What is the total Revenue and number of orders?
Select Count(distinct invoice) as total_orders, 
Round(Sum(revenue)::decimal,2) as total_revenue
from sales_data

--Q2.Which countries generate the most revenue?
select country,
Round(Sum(revenue)::decimal,2) as total_revenue from sales_data
group by country
order by total_revenue DESC


--Q3.What are the top 10 products by revenue?
select description,
Round(Sum(revenue)::decimal,2) as total_revenue from sales_data
group by description
order by total_revenue DESC
Limit 10

--Q4.Who are the top 10 customers by revenue?
select customer_id,
Round(Sum(revenue)::decimal,2) as total_revenue from sales_data
group by customer_id
order by total_revenue DESC
Limit 10
--Q5.How does revenue trend over time?
select DATE_TRUNC('month', invoice_date) as month,
Round(Sum(revenue)::decimal,2) as total_revenue from sales_data
group by DATE_TRUNC('month', invoice_date)
order by month
