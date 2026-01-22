# Sales-Data-Cleaning-and-Analysis-using-Pandas
📊 Sales Data Cleaning and Analysis using Pandas
📌 Project Overview

This project focuses on cleaning, processing, and analyzing real-world sales data using Python and Pandas.
The dataset was intentionally messy to simulate real business scenarios, including missing values, duplicates, inconsistent text, and mixed date formats.

The goal of this project is to demonstrate:

Strong data cleaning skills

Feature engineering

Business-oriented data analysis

Use of Pandas for real-world datasets

🧠 Skills & Tools Used

Python

Pandas

Datetime handling

Data Cleaning

Exploratory Data Analysis (EDA)

📂 Dataset Description

The dataset contains sales-related information such as:

Order_ID

Order_Date

Product

Category

Region

Quantity

Price

Salesperson

Data Issues Handled:

Missing values

Duplicate records

Inconsistent text casing and spacing

Mixed date formats

Invalid quantities

Null prices

🧹 Data Cleaning Steps

Removed duplicate rows

Standardized text columns (Product, Category, Region, Salesperson)

Filled missing values for categorical columns

Removed rows with missing prices

Removed invalid orders (Quantity ≤ 0)

Converted Order_Date to datetime safely

Verified cleaned dataset integrity

⚙️ Feature Engineering

New columns created to enhance analysis:

Revenue = Quantity × Price

Order_Year

Order_Month

Is_valid_Order

📈 Sales Analysis Performed

The following business questions were answered:

Total revenue generated

Revenue by product

Revenue by category

Revenue by region

Monthly revenue trends

Top-selling products

Average order value

Best and least performing salespersons

🧠 Key Insights

Certain products contribute significantly more to total revenue

Sales performance varies across regions

A small number of salespersons generate most of the revenue

Monthly trends help identify high-performing periods

📁 Project Structure
sales-data-cleaning-analysis/
│
├── messy_sales_data.csv
├── sales_analysis.py
├── README.md

🚀 Future Improvements

Add data visualization using Matplotlib

Perform deeper time-series analysis

Export cleaned data for reporting

Combine with SQL for advanced querying

🏁 Conclusion

This project demonstrates the ability to work with messy real-world datasets, apply Pandas best practices, and extract meaningful business insights.
It is suitable for showcasing data analysis skills on GitHub and resumes.
