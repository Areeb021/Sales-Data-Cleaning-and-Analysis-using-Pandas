📊 Sales Data Analysis & Revenue Insights
📌 Project Overview

This project focuses on cleaning, analyzing, and visualizing a messy real-world sales dataset using Python, Pandas, and Matplotlib.
The goal is to uncover revenue trends, evaluate product and salesperson performance, and answer key business questions through exploratory data analysis (EDA).

🛠️ Tools & Technologies

Python

Pandas – data cleaning, transformation, and analysis

Matplotlib – data visualization

📂 Dataset Description

The dataset (messy_sales_data.csv) contains sales transaction data with the following key fields:

Product

Category

Region

Salesperson

Quantity

Price

Order_Date

🧹 Data Cleaning & Preparation

Removed extra spaces and standardized text columns

Handled missing values for category and region

Removed invalid records (missing price, zero or negative quantity)

Converted order dates to datetime format

Created new features:

Revenue (Quantity × Price)

Order_Year

Order_Month

Is_Valid_Order

📈 Exploratory Data Analysis (EDA)
🔹 Revenue Analysis

Total revenue calculation

Revenue by:

Product

Category

Region

Month

🔹 Product Insights

Identified top 3 products by revenue

Analyzed product sales frequency

🔹 Salesperson Performance

Best-performing salesperson by total revenue

Least-performing salesperson

Sales distribution by salesperson using a pie chart

🔹 Order Analysis

Average order value

Monthly revenue trends

📊 Visualizations

Bar charts for revenue and sales comparisons

Line plot showing monthly revenue trends

Scatter plot for order value analysis

Pie chart representing salesperson revenue contribution

🧠 Business Questions Answered

Which products generate the most revenue?

Which category and region perform best?

Who is the top-performing salesperson?

How does revenue trend over time?

What is the average order value?

🚀 Key Insights

Revenue is concentrated among a few top-performing products

Certain regions and categories consistently outperform others

Sales performance varies significantly between salespersons

Monthly trends highlight seasonal revenue patterns

📁 Project Structure
├── messy_sales_data.csv
├── sales_analysis.py
└── README.md

✅ Conclusion

This project demonstrates end-to-end data analysis skills, including data cleaning, feature engineering, visualization, and business insight generation.
It reflects practical, real-world data handling suitable for entry-level data analyst roles.
