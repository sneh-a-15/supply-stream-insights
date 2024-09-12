# Supply Stream Insights
Supply Stream Insights is a comprehensive supply chain management dashboard designed to monitor inventory levels, predict supply chain disruptions, and optimize stock management. The dashboard utilizes Celery for task scheduling, Redis for message brokering, and PostgreSQL for data storage.

## Features
- **Inventory Management:** View and manage inventory levels.
- **Automated Stock Reduction:** Periodically reduce stock levels to simulate real-world scenarios.
- **Data Visualization:** Graphs and charts to visualize inventory and sales data.

## Requirements
Ensure you have the following Python packages installed:
```
- django
- celery
- redis
- psycopg2 (PostgreSQL adapter for Python)
- django-environ (for environment variable management)
```

## Installation
To run Supply Stream Insights locally, follow these steps:

1. Clone the repository: git clone https://github.com/sneh-a-15/supply-stream-insights.git

2. Navigate to the project directory: cd supply-stream-insights

3. Set up your environment:
Create a .env file in the project root with the following content:
```
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

4. Install dependencies: `pip install -r requirements.txt`

5. Run migrations: `python manage.py migrate`

6. Start Redis (using Docker): `docker run -d -p 6379:6379 redis`

7. Start Celery worker: `celery -A myproject worker --loglevel=info`

8. Start Celery Beat (for scheduled tasks): `celery -A myproject beat --loglevel=info`

9. Start the Django development server: `python manage.py runserver`

## APIs Used

- [Google Books API](https://developers.google.com/books)
- [Spoonacular API](https://spoonacular.com/food-api)
- [Ecommerce API](https://ecommerceapi.io/)

# Troubleshooting
- **Redis Connection Error:** Ensure that Redis is running and accessible at localhost:6379.
- **Celery Task Issues:** Verify that Celery is correctly configured and running.
