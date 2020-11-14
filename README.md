# CSE412DatabaseProject
Creating a music library database

# Setup Process
Install Python3: https://docs.python-guide.org/starting/install3/linux/

Install psycopg2: https://pypi.org/project/psycopg2/

Install Flask: https://flask.palletsprojects.com/en/1.1.x/installation/

Install PostgreSQL: https://www.postgresql.org/download/

Create a local database: https://www.liquidweb.com/kb/creating-and-deleting-a-postgresql-database/

Create a user role with admin: https://stackoverflow.com/questions/15008204/how-to-check-postgres-user-and-password

Test database locally: https://www.tutorialspoint.com/postgresql/postgresql_python.htm

# Required Setup In Code
In tableCreation line 6 database="YOURDBNAME", user="YOURUSER", password="YOURPW"

In sqlUtil.py line 6 database="YOURDBNAME", user="YOURUSER", password="YOURPW"

Change YOURDBNAME to the name of your local database

Change YOURUSER to the name of your local user that has superuser in your database

Change YOURPASSWORD to the password of your local user from the last step
