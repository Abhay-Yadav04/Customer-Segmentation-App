# 🛒 Retail Customer Segmentation Flask App
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/) [![Flask](https://img.shields.io/badge/Flask-1.1.2-orange?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)  [![Docker](https://img.shields.io/badge/Docker-20-blue?logo=docker&logoColor=white)](https://www.docker.com/)  [![Gunicorn](https://img.shields.io/badge/Gunicorn-server-green)](https://gunicorn.org/)  
[![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24-blue?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)

[🌐 Live Demo on Render](https://customer-segmentation-app-4ifa.onrender.com)

## 📋 Project Overview

This project is a **Flask-based web application** that implements a customer segmentation model to classify retail customers based on their behavior. The app utilizes key customer metrics to segment customers, enabling businesses to tailor marketing strategies and improve customer engagement. You can use **synthetic_customer_segments** file in repository as input because input file compulsarily requires **Customer ID, Recency, Frequency, Monetary** features. 

---

## ✨ Features

- 🖥️ Interactive web interface for inputting customer data  
- ⚡ Real-time prediction of customer segments using a machine learning model  
- 🎨 Clean and user-friendly UI  
- 🐳 Dockerized for simple deployment and environment consistency  

---

## 🤖 Model Description

The customer segmentation model classifies customers into distinct groups based on the following features:

| Feature    | Type    | Description                            |
|------------|---------|------------------------------------|
| **CID**       | Integer | Unique identifier for each customer   |
| **Recency**   | Integer | Days since the customer's last purchase |
| **Monetary**  | Float   | Total amount spent by the customer    |
| **Frequency** | Integer | Number of purchases made by the customer |

The model uses these features to segment customers into meaningful groups such as loyal, at-risk, or new customers, helping businesses optimize marketing efforts.

---

## 🚀 Usage

### Input Requirements

The app requires the following inputs through the form or API:

| Input     | Type    | Description                              |
|-----------|---------|----------------------------------------|
| **CID**       | Integer | Customer ID                            |
| **Recency**   | Integer | Days since last purchase               |
| **Monetary**  | Float   | Total spending amount                  |
| **Frequency** | Integer | Number of purchases                    |

### How to Use

1. Open the app URL in your web browser  
2. Enter the customer details (CID, Recency, Monetary, Frequency) in csv format
3. Submit the form to get the predicted customer segment  
4. Use the segmentation results to guide marketing strategies and customer engagement  

---

## 🛠 Technologies Used

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/Flask-1.1.2-orange?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)  
[![Docker](https://img.shields.io/badge/Docker-20-blue?logo=docker&logoColor=white)](https://www.docker.com/)  
[![Gunicorn](https://img.shields.io/badge/Gunicorn-server-green)](https://gunicorn.org/)  
[![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24-blue?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)  

---

##  Contributing

Contributions, issues, and feature requests are welcome! Please check the issues page or submit a pull request.

---



