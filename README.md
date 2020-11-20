# CSE412DatabaseProject
Creating a music library using PostgreSQL and Python3. We created the frontend with Flask and interacted with the database through psycopg2. All of the initial data that is stored into the database is scraped from the SpotifyAPI.

MusicLibary contains the application. 

SpotifyDataCollection contains the code for scraping the SpotifyAPI.

# Setup Process
User Guide: https://drive.google.com/file/d/1zNDRlyCN6J_tJXnEk0biRH2NSESajnkH/view?usp=sharing

Install Python3: https://docs.python-guide.org/starting/install3/linux/

Install psycopg2: https://pypi.org/project/psycopg2/

Install Flask: https://flask.palletsprojects.com/en/1.1.x/installation/

Install PostgreSQL: https://www.postgresql.org/download/

Create a local database: https://www.liquidweb.com/kb/creating-and-deleting-a-postgresql-database/

Create a user role with admin: https://stackoverflow.com/questions/15008204/how-to-check-postgres-user-and-password

Test database locally: https://www.tutorialspoint.com/postgresql/postgresql_python.htm

# If You Did Not Follow User Guide Credentials
In tableCreation line 6 database=database="musicLibrary", user = "musicLib", password = "musicPass"

In sqlUtil.py line 6 database=database="musicLibrary", user = "musicLib" password = "musicPass"

Change musicLibrary to the name of your local database

Change musicLib to the name of your local user that has superuser in your database

Change musicPass to the password of your local user from the last step

# Member Contributions
Preston Mott: Scraped the SpotifyAPI for initial data. Created the database tables and inserted scraped data into them. Created backend functionality of website interface by performing SQL queries with given user input. Connected the backend to the front end. 

Daniel Waltman: Drafted SQL functions in PostgreSQL that ended up not being used in the final product. Created the front end templates and a draft of the connection between the front end and backend so Preston could have all input data accessible before he integrated the SQL queries. Also worked with Preston Mott to connect the backend to the front end through the transfer of data from queries to result templates. Error checked and style/consistency checked with Preston as well.

Andrew Coughlin: Helped with scraping the Spotify API for data to fill the database with. Also helped with front/backend connection.

Kristian Avila:Helped write the User Guide and wrote the User manual on how to use the website.
