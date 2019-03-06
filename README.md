# telenor_bigdata

**telenor_bigdata** is a **django** project. This project is responsible for generatiing a dashboard based on the fact databse.
This fact database is a data wearhouse which is generated from sources of data.

Angularjs javascript framwork is used as front end technology and of course python based django in the backend.

# Installation

Install python in your machine. I used ubuntu os where python is installed by default.

open terminal in your computer and run the command below:

  ***git clone https://github.com/jahangir091/telenor_bigdata.git***
  
 This command will clone the project from github to your local machine.
 
 Now go to the directory **telenor_bigdata/telenor_health** and run the command below:
 
  ***pip install -r requirements.txt***
  
This command will install necessary python libraries in your computer.


# Run telenor_bigdata

Now run the project by the following command:

  ***python manage.py runserver***
  
This command will run your django project at **localhost:8000** 
So now go to the browser and got to this url : 

  ***http://localhost:8000***
  
You will see a dashboard named Tonic Dashboard.

On this dashboard you will see some graph which includes informations.
These informations are retriving from an API call from the django backend and this django backend is connected to 
the fact database.

AngularJs is responsible for fetching data by api call and binding data to the web page.
