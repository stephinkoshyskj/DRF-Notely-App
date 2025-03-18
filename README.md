====================== DRF-Notely-App Setup Guide ======================


Follow these steps to set up and run the DRF-Notely-App on your local machine:

Prerequisites

Python (Ensure Python is installed on your system)

Git (For cloning the repository)

Installation Steps

1. Install Python

Ensure Python is installed by running:

python --version

If Python is not installed, download it from python.org.

2. Create a Virtual Environment (Recommended)

Create a virtual environment to manage project dependencies:

python -m venv venv

3. Activate the Virtual Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

4. Clone the Repository

Clone the project using Git:

https://github.com/stephinkoshyskj/DRF-Notely-App.git

5. Navigate to the Project Directory

cd DRF-Notely-App

6. Install Dependencies

Install all required dependencies from requirements.txt:

pip install -r requirements.txt

7. Apply Migrations

Generate and apply database migrations:

python manage.py makemigrations
python manage.py migrate

8. Run the Development Server

Start the Django development server:

python manage.py runserver

9. Access the Application

Visit http://localhost:8000 in your browser to view the app.


======================================================================
