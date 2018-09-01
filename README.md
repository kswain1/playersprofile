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


### Player Dashboard 

*** Definition ***

'Get /players/<id>'

***Response***

``` json

[
  {"id":01,
   "name":"Lebron James",
   "age":36,
   "profile_img":"www.bin.com/lebronjames",
   "injury_history":"Poor knees",
   "current_injury":"None available",
   "risk_score":3,
   "rightle":[
         {"tib_anterior":[{"max":50,"medium":60,"minimal":80}],
          "peroneals":[{"max":60,"medium":10,"minimal:30}],
          "med_gastro":[{"max":20,"medium":30,"minimal":50}],
          "lat_gastro":[{"max":30,"medium":50,"minimal":20}]
          }
            ],
   "leftle":[
          {"tib_anterior":[{"max":50,"medium":60,"minimal":80}],
          "peroneals":[{"max":60,"medium":10,"minimal:30}],
          "med_gastro":[{"max":20,"medium":30,"minimal":50}],
          "lat_gastro":[{"max":30,"medium":50,"minimal":20}],
          }
          ],
   "assessment":"Player is serious risk on injuring their tibular anterior",
   "treatment":"Soak and ice knee until, and go through plyo excersises"
   }]
   
  ```
  ### List all players
  
  *** Definition ***

'Get /players/'

### Definition
  
  ``` json 
  [
    {"id":01,
    "name":"Lebron James",
    "profile_img":"www.bin.com/lebronjames",
    "risk_score":3,
    },
     {"id":02,
    "name":"Lebron James",
    "profile_img":"www.bin.com/lebronjames",
    "risk_score":3,
    },
     {"id":03,
    "name":"Lebron James",
    "profile_img":"www.bin.com/lebronjames",
    "risk_score":3,
    },
     {"id":04,
    "name":"Kyle James",
    "profile_img":"www.bin.com/lebronjames",
    "risk_score":3,
    },
  ]
```
### Post players emg data 

*** Defintion ***

'Post /players/<id>'
  
### Definition

``` json
[
  {"name":"Kehlin Swain",
  "age":22,
  "profile_image":"www.hello.com/img",
  "tib_anterior_lle":[1,2,4,5,6,9],
  "tib_anterior_rle":[1,2,4,5,6,9],
  "peroneals_rle":[1,2,3,4,5,9],
  "peroneals_lle":[9,8,7,6,3],
  "med_gastro_rle":[8,9,0,1,7],
  "med_gastro_lle":[10,20,9,9,1],
  "lat_gastro_rle":[12,32,90,3,2],
  "lat_gastro_llt":[12,45,60,1,3],
  }
]
```

### Post players assessment data 

*** Defintion ***

'Post /assessment/<id>'
  
### Definition

``` json
[
  {"assessment":"Hello this is my assessment of how the athlete is doing in his trials"
   "treatment":"Your athlete will need to do x,y, and z to complete his next actions"
  }
]

