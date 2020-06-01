# django_multi_db
Django multi database application.


# Create databases

# Create postgres database
create database database1;
create database database2;

GRANT ALL PRIVILEGES ON DATABASE "database1" to postgres_user;
GRANT ALL PRIVILEGES ON DATABASE "database2" to postgres_user;

# Create mysql database
create database database3;
create database database4;
create database database5;

GRANT ALL PRIVILEGES ON DATABASE "database3" to mysql_user;
GRANT ALL PRIVILEGES ON DATABASE "database4" to mysql_user;
GRANT ALL PRIVILEGES ON DATABASE "database5" to mysql_user;

# Create an virtualenv & install all requirements present in requirements.txt
pip install -r requirements.txt 

# Update database access username & password in settings.py file

# Run following commands
python manage.py migrate
python manage.py migrate dashboard --database='database1'
python manage.py migrate dashboard --database='database2'
python manage.py migrate dashboard --database='database3'
python manage.py migrate dashboard --database='database4'
python manage.py migrate dashboard --database='database5'

# Create superuser & set username & password for ex. username=admin & password=admin@123
python manage.py createsuperuser

# Now do runserver 
# For Admin & User Login Use: localhost:8000/login
# Here if you login you will be redirected to /account/profile 
