# global-retail-sales-analysis
Project Overview
This project analyzes global retail transaction data to uncover sales trends, customer behavior, and revenue drivers. The goal is to transform raw transactional data into actionable business insights using a complete end-to-end data analysis workflow.
The project demonstrates core data analyst skills, including:
Data cleaning with Python
Feature engineering
SQL business analysis
Data visualization with Power BI
Business insights and recommendations
Business Problem
Retail companies need to understand:
Which products generate the most revenue
Who their top customers are
How sales change over time
Which countries drive the most revenue
This project answers these questions using real transactional data.
Dataset
Online Retail Dataset (2009–2011)
Rows: ~800,000 transactions after cleaning
Columns:
Invoice
StockCode
Description
Quantity
InvoiceDate
UnitPrice
CustomerID
Country
Project Workflow
Phase 1: Data Understanding
Explored structure of the dataset
Combined two yearly sheets into one dataset
Checked data types and column meanings
Phase 2: Data Cleaning (Python)
Key cleaning steps:
Removed missing customer IDs
Removed cancelled orders
Removed negative quantities and prices
Removed non-product stock codes
Final dataset:
~800,000 clean transaction rows
Phase 3: Feature Engineering
Created new columns:
Revenue = Quantity × UnitPrice
Year from InvoiceDate
Month from InvoiceDate
Also created a customer summary table with:
Total orders
Total revenue
Average order value
Phase 4: Data Loading (PostgreSQL)
Connected Python to PostgreSQL using SQLAlchemy
Loaded cleaned dataset into database
Created a structured sales table for analysis
Phase 5: SQL Business Analysis
Answered key business questions using SQL:
Total revenue and total orders
Revenue by country
Top 10 products by revenue
Top customers by revenue
Monthly revenue trends
Phase 6: Power BI Dashboard
Built an interactive dashboard showing:
Total revenue
Total orders
Total customers
Average order value
Monthly revenue trend
Revenue by country
Top products
Top customers
Orders by month
Features:
Dark modern theme
Interactive country and year slicers
Business-focused visuals
Key Insights
The United Kingdom generates the majority of revenue.
A small number of products drive most sales.
A few customers contribute significantly to total revenue.
Sales increase toward the end of the year, indicating seasonal demand.
Business Recommendations
Expand marketing to other high-potential countries.
Ensure top-selling products never go out of stock.
Introduce a loyalty program for high-value customers.

Increase inventory before peak sales months.
Tools & Technologies
Python (Pandas, NumPy)
PostgreSQL
SQL
Power BI
Git & GitHub

What I Learned
End-to-end data analysis workflow
Real-world data cleaning challenges
Writing business-driven SQL queries
Designing professional dashboards
Turning data into actionable insights
Author
Alex Benstowe 
Aspiring Data Analyst
