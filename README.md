# Personal Expense Tracker
A web-based personal expense tracking application that allows users to monitor their spending habits and visualize financial patterns. Built with Django, the app enables users to track daily expenses, categorize transactions, generate spending reports, and visualize monthly and yearly spending patterns.

## Project Overview
This project is designed to provide users with a streamlined way to record and analyze their expenses. With features like expense tracking, category-based visualizations, and monthly/yearly reports, users can gain insights into their spending habits and manage their finances effectively.

## Features
### Core Features
- **User Authentication**: Sign up and log in to securely access your expense data.
- **Daily Expense Tracking**: Track daily expenses by entering the amount, selecting a category, and adding optional comments.
- **Category-Based Visualizations**: View daily expenses in pie and bar charts categorized by spending types.
- **Monthly and Yearly Reports**: Access detailed reports of your expenses by month or by year, with visualizations for better insights.

### Reports Page
- **Yearly Report**: View total expenses for each month as a bar chart.
- **Monthly Report**: View daily expenses for a selected month as a stacked bar chart, categorized by spending types.
- **Dynamic Filtering**: Choose the desired year and month to generate specific reports.

## Tech Stack
- **Backend**: Django 
- **Frontend**: HTML, JavaScript
- **Visualization**: Plotly
- **Database**: SQLite (default, can be configured to other databases)

## Installation and Setup
### Prerequisites
- Python 3.8
- Git

### Setup Instructions
1. **Clone the repository**
    ```bash
    git clone git@github.com:Dheerajkumarbuchala/expense_tracker.git
    cd expense_tracker
    ```

2. **Create and activate a virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install required dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run database migrations**
    ```bash
    python manage.py migrate
    ```

5. **Start the development server**
    ```bash
    python manage.py runserver
    ```

6. **Access the application**
- Visit http://127.0.0.1:8000/ in your browser to access the homepage.

## Project Structure
<img width="249" alt="Screenshot 2024-11-10 at 3 37 56 PM" src="https://github.com/user-attachments/assets/987cf4c8-6c93-4877-a0ae-3dbcddb9ace4">

## Usage
1. **Register and LogIn**: Start by registering a new account and logging in.
2. **Dashboard**:
    - View a calendar on the left and a summary of expenses for the selected date on the right.
    - Click on any date to view or add expenses.
3. **Add Expense**:
    - Click "Add Expense" to enter a new expense for a selected date.
    - Choose a category, enter the amount, and add optional comments.
4. **View Reports**:
    - Access reports by clicking the "View Reports" button on the dashboard.
    - Select a year and a month (or "All" for monthly view) to generate the desired report.

## Reports and Visualizations
- **Daily Visualization on Dashboard**:
    - **Pie Chart**: Displays the distribution of expenses by category.
    - **Bar Chart**: Shows the total expenses for each category for the selected date.
- **Monthly and Yearly Reports**:
    -**Yearly Report**: Bar chart of total expenses per month.
    -**Monthly Report**: Stacked bar chart of daily expenses by category for the selected month.
