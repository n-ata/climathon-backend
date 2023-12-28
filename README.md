login
register,
create-post

ishleya

pip install -r requirements.txt

python manage.py runserver


database postgresql:
CREATE DATABASE yourdatabase;
CREATE USER myprojectuser WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
