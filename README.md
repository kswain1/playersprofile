# Playersprofile 
rest api for athletes player profiles data

## Starting an App
- django-admin.py startproject myfirstproject
- python manage.py startapp myfristappweb

## Key Notes Thus Far
- endpoint is going to be hello-view, and it's going to render the as_view
- Updating Admin site is very crucial 
- adding mulitple projects is another key lesson learned.

### Point of Serilizers 
- Serializers allow you to create a post and put to your database 

### APIVIEWS (Custom API Logic)
- setup for loading logic 
- different then a view set because it is based on custom logic

### Viewsets (Un-Customer API Logic)
- simple and quick for CRUD application
- viewset automagically saves the creates a template for your data page 
- Viewsets require you to go the specifc object in the data to do more specific commands such as update


### Login Authentication
- When working with Login profiles we noticed that there are key authorizaiton tokens that we have to be aware off 
- key learnings of adding authnetications and login information

