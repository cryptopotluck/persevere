##Presevere Dynamic Site

I built this site in regards to my application at Presevere, regardless of my application I grant all rights to use this site & everything created to the non-profit Presevere.

##How to Install/Setup
This is a Dynamic Django web application so to get started you will need to download the file and open it within a virtual environment.

I've included a requirements.txt file so you can ``pip install requirments``

I am using postgress as the database so make sure you go into the persevere/settings.py file and direct to a locally hosted postgres database.

After setting that up you can run ``python manage.py collectstatic`` to bring in a static folder into the application

Make sure you run migrations ``python manage.py makemigrations`` & ``python manage.py migrate``

I'd also suggest looking through the persevere/settings.py file as you can change the email hosting

Finally you are setup to run the application locally with ``python manage.py runserver``

##Issues? Contact

Contact me if you have any issues setting up the project and I'll be more than happy to trouble shoot and help.