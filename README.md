# playersprofile
rest api for athletes player profiles data


## Key Notes Thus Far
- endpoint is going to be hello-view, and it's going to render the as_view
- Updating Admin site is very crucial 
- adding mulitple projects is another key lesson learned.

### List all players

*** Definition ***

'Get /players/<id>'

***Response***

'''json
[
  {"id":01,
   "name":"Lebron James",
   "age":46,
   "profile_img":'www.bin.com/lebronjames',
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
  '''
  
