# 📊 Customer Spending & Segmentation Dashboard (GHN Dataset)

This project analyzes 1 million transaction records provided by GHN Express to understand customer spending patterns, identify key customer segments, and support data-driven decision-making.

## 🚀 Objectives

- Visualize overall spending and transaction KPIs
- Segment customers using RFM (Recency, Frequency, Monetary) model
- Identify potential, loyal, and at-risk customers
- Simulate a real-world customer analysis dashboard

## 🛠️ Tools & Technologies

- **Power BI** (Dashboard, DAX, Drill-through, Custom visuals)
- **Python** (Data preprocessing & transformation)
- **Excel** (Pre-analysis & metadata exploration)
- **Power Query** (Data cleaning and modeling)

## 📂 Data Overview

- Source: GHN-provided dataset with over **1,000,000 rows**
- Key fields: customer ID, amount, transaction date, transaction type
- Format: Original data in `.parquet`, processed using Python

## 📈 Dashboard Preview

<img width="1336" height="745" alt="image" src="https://github.com/user-attachments/assets/b726dbf0-0307-4c7e-a684-9daba58d22b4" />


> Note: This image shows key metrics, category-wise spending, and RFM segmentation visualizations.

## 📌 Key Insights

- Over 250 unique customers identified
- Spending peaks in Q4 with increased repeat orders
- Top 20% customers contribute over 60% of total revenue
- Customers segmented into 3 main RFM groups:
  - **Potential**: High frequency, moderate recency
  - **At Risk**: Low recency, used to spend a lot
  - **Need Attention**: Medium spenders, moderate frequency

## 🔍 RFM Heatmap (Interactive)

Includes an interactive heatmap to explore behavior by RFM score combinations with drill-through to customer profiles.

## 📁 Folder Structure

