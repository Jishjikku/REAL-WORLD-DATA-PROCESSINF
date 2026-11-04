# Task 4: Real-world Data Project: Retail Sales Analysis

## Objective
Apply analysis skills to a retail business scenario and give practical recommendations.

## Files
- `task4_retail_analysis.py`: analysis and reporting script
- `Task4_Report.docx`: report to complete and submit
- Input: `../retail_sales_raw.csv`

## Business Questions
- Which product categories contribute most to sales?
- How do sales vary by region and by month?
- How can customer ratings support business decisions?

## Method
- Remove duplicates, fill missing values, and drop rows with missing date or sales
- Group by category, region, and month
- Calculate total sales, units sold, and average rating per category

## How to Run
```bash
pip install pandas matplotlib
cd Task4_Real_World_Retail
python task4_retail_analysis.py
```

## Outputs
- `retail_category_performance.png`: total sales by category
- `retail_monthly_sales.png`: monthly sales trend
- `category_summary.csv`: category totals, units, and average rating
- `region_summary.csv`: sales by region
- Console output: category, regional, and monthly tables plus four recommendations

## Limitations
The dataset is synthetic and only demonstrates the workflow. A real deployment would need an approved, documented dataset and validation with domain stakeholders.

## Submission
Add the outputs and recommendations to `Task4_Report.docx`, fill in the student name, and upload the files listed in the task's Submit Work page on the Thiranex website.
