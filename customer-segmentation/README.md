Customer Segmentation using RFM and Clustering
Overview

This project focuses on segmenting customers based on their purchasing behavior using RFM analysis and multiple clustering techniques. The goal is to identify meaningful customer groups that can help businesses design targeted marketing, retention, and growth strategies.

The project transforms raw transactional data into behavioral features and applies unsupervised machine learning algorithms to discover hidden customer segments.

Business Objective
Identify high value and loyal customers
Detect inactive or churn risk customers
Understand purchasing patterns across customer groups
Enable targeted marketing and personalized campaigns
Dataset

The project uses transactional retail data containing:

CustomerID
InvoiceNo
InvoiceDate
Quantity
UnitPrice

From these, total transaction value is derived.

Feature Engineering: RFM Analysis

RFM stands for:

Recency: Number of days since the last purchase
Frequency: Number of transactions per customer
Monetary: Total spend per customer

These features capture customer engagement and value.

Data Preprocessing
Removed missing CustomerID values
Filtered out negative quantities and invalid prices
Converted date fields into datetime format
Created total transaction value

To prepare data for clustering:

Applied log transformation to reduce skewness
Used feature scaling to normalize feature ranges
Clustering Techniques Used

The following clustering algorithms were implemented and compared:

K Means

Partitions customers into k clusters based on distance from centroids.

Hierarchical Clustering

Builds clusters by iteratively merging similar data points.

DBSCAN

Density based clustering that identifies clusters and outliers.

Gaussian Mixture Model

Probabilistic clustering that allows overlapping clusters.

Model Selection

The optimal number of clusters for K Means was selected using the Elbow Method.

K Means was chosen as the final model because it achieved the highest silhouette score, indicating better cluster separation and cohesion compared to other models.

Evaluation Metric

Silhouette Score was used to evaluate clustering quality.

K Means: 0.316
Hierarchical Clustering: 0.242
Gaussian Mixture Model: 0.174

Higher score indicates better defined clusters.

Results: Customer Segments

The final clustering identified distinct customer groups such as:

High value loyal customers
Active regular customers
At risk customers
Low value occasional customers
Inactive customers

Each segment shows clear differences in recency, frequency, and monetary behavior.

Business Insights
High value customers can be targeted with loyalty programs and premium offerings
At risk customers can be re engaged through discounts and campaigns
Low engagement customers can be nurtured through onboarding strategies
Frequent moderate customers can be upsold using personalized recommendations
Technologies Used
Python
Pandas
NumPy
Scikit learn
Matplotlib
How to Run
Clone the repository
Install required libraries
Run the notebook
Future Improvements
Add more behavioral features such as average order value and product diversity
Compare additional clustering techniques
Build a dashboard using Streamlit or Power BI
Automate segmentation pipeline
Key Takeaway

This project demonstrates how raw transactional data can be transformed into actionable customer insights using RFM analysis and clustering techniques, enabling data driven business decisions.
