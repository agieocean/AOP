# AOP
AOP (Abuse of Power) is a reporting system for abuses of power.
This provides an additional route along with traditional routes to keep people in power to account.i
In addition this is hosted in somewhat of a decentralized manner. The intake is hosted seperately from the frontend and the database is hosted on backblaze. This way any attackers would need to take down 3 different hosts to take AOP offline.

# What's in this repo
## frontend.html + static/
This is the front end html/js/css code to display and search the database
## Other code
The rest of the code provides the backend for intake of reports of abuse of power

# Pre-requisites
A machine with docker and docker-compose on it
A backblaze account

# How to run
## Front end
Copy the frontend.html and static directory to your host of choice. We host the front end on neocities currently. Change the dbFile location to match your backblaze location for the file.
## Intake
Copy the code to a host with docker and docker compose on it. Before you bring the code up make sure to configure it. You'll want to edit manage.py, docker-compose.yml, and intake/utils.py. After you're done just docker-compose (or docker compose) up and go to your host ip:8000/intake/ to see intake. To get to the admin interface first set a superuser using docker exec and then go to your host ip:8000/admin.