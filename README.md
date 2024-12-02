# research1

A Django webapp for creating and managing study groups. Users have CRUD abilities over these groups.

Steps to run:
1. Clone repository:
git clone https://github.com/whtate/researchtest.git  
cd researchtest

2. Create virtual environment:
Windows: python -m venv env  
env\Scripts\activate

Mac/Linux: python3 -m venv env  
source env/bin/activate

3. Install requirements/dependencies: pip install -r requirements.txt

4. Set up environment variables: 
Create a .env file in the root of the project and add these:  
DJANGO_SECRET_KEY=your-secret-key  
DJANGO_DEBUG=True  # Set to False for production  
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1  # Adjust for production

5. Apply migrations:
python manage.py migrate

6. Run localhost:
python manage.py runserver

7. Create superuser (admin):
python manage.py createsuperuser  
Follow prompts  
To view admin panel: http://127.0.0.1:8000/admin/
U p d a t e :   n e w   s e c t i o n   i n   R E A D M E  
 