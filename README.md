# Libraya
First you need to setup your database system (we use here postgres)then:
Create a user :
sudo -u postgres createuser -P username  //   create a user(username) and give it a password

Create a database :
sudo -u postgres createdb db -O username // to create a database (db) and assign it to username

then now we have to connect to our database :
sudo psql -h 127.0.0.1 -U username  db // connect to database db 

Second you should have python installed on your system. Then run `pip install -r requirements.txt` to download all packages needed for this project .
Then run `python manage.py makemigrations`  to commit the changes of your models 
then `python manage.py migrate` to translates your models into tables.

you must have superuser account to get access to admin  dashboard of django  
Run `python manage.py createsuperuser` and enter the required data.

After that run `python manage.py runserver` and head over to the browser to http://127.0.0.1:8000 and login.



There are two types of user one is admin (who adds students and books) and another is regular user(student).


 
Before adding new books , go to the http://127.0.0.1:8000/admin admin site and add the required genre and language manually  or through postgres shell .  
