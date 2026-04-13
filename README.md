📊 Customer Sales Analysis – Week 5
📌 Project Overview

This project focuses on advanced data manipulation using Pandas to analyze customer purchasing behavior and sales performance. It combines multiple datasets to generate insights about customers, products, and business trends.

The main goal is to:

Understand customer behavior
Identify top-performing customers and products
Analyze sales patterns
Generate business insights
🎯 Objectives
Perform data cleaning and preprocessing
Merge multiple datasets
Apply grouping and aggregation
Create pivot tables for summarization
Analyze customer and sales trends
Generate insights and reports
📁 Project Structure
week5/
│
├── customer_analysis.py       # Main analysis script
├── sales_data.csv            # Sales dataset
├── customer_churn.csv        # Customer dataset
├── monthly_sales.png         # Visualization
├── product_analysis.png      # Visualization
├── region_analysis.png       # Visualization
├── analysis_report.pdf       # Final report
├── requirements.txt          # Dependencies
└── README.md                 # Documentation
⚙️ Setup Instructions
🔧 Install Dependencies
pip install pandas numpy matplotlib seaborn
▶️ Run the Project
python customer_analysis.py
🔍 Key Features & Analysis
📊 1. Data Loading & Exploration
Loaded datasets using Pandas
Checked structure, columns, and data types
Handled missing values
🧹 2. Data Cleaning
Removed duplicates
Filled missing values
Converted data types
🔗 3. Data Merging
Combined sales and customer datasets
Used pd.merge() for integration
📈 4. Data Aggregation
Grouped data by:
Customer
Product
Region
Calculated:
Total revenue
Average order value
Sales distribution
📊 5. Pivot Tables
Summarized sales data by:
Product vs Region
Customer vs Sales
📅 6. Time-Based Analysis
Extracted month from date
Analyzed monthly sales trends
📊 Sample Output
Total Revenue: 12,365,048
Total Customers: 100
Average Order Value: 123,650
Top Customer: CUST016 - 373,932
📈 Visualizations
📊 Monthly Sales Trend
📦 Product Performance
🌍 Region-wise Sales
🧠 Key Insights
Certain customers contribute significantly to revenue
Sales vary across regions
Some products outperform others
Seasonal trends observed in monthly sales
💼 Business Recommendations
Focus on high-value customers
Improve sales in low-performing regions
Promote best-selling products
Optimize inventory based on demand trends
🧪 Testing & Validation
Verified dataset merging
Validated calculations and aggregations
Ensured accurate visualizations
🏗️ Workflow
Data Loading → Cleaning → Merging → Analysis → Visualization → Insights
🚀 Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
🎓 Learning Outcomes
Advanced Pandas operations
Data merging and aggregation
Pivot table creation
Business data analysis
✅ Conclusion

This project demonstrates how advanced data manipulation techniques can be used to extract meaningful insights from real-world datasets.
