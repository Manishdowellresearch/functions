# Documentation
    
1.  Details about the files

    - dowellconnection.py , has dowellconnection function.
    - dowellevent.py , has dowelleventcreation function.
    - dowellpopulation.py , has targeted population function. 
    - callfunction.py , has function call and database and collection details
2.  Dowellconnection function `[dowellconnection(cluster,database,collection,document,team_member_ID,function_ID,command,field)]`
&nbsp;
    ```python
    from dowellconnections import dowellconnection
    from dowellevent import get_event_id

    def tp_report_insert():
    field ={
        "eventId":get_event_id(),
        "test_data":"test_data" 
        }
    inserted_id= dowellconnection("TP_Reports","tp_reports","Reports","Reports","1000001","ABCDE","insert",field)
    return inserted_id

    print(tp_report_insert())
    ```
    - **field** should be a json data and what you want to insert to the database.
    - You must call dowellevenctcreation function to generate eventId `get_event_id()`. What all attribute you want you can declare like a `{"key":"value"}` &nbsp;

    ==Note: key for eventId should be written like `evenId`== 
&nbsp;
3. Dowellpopulation function `[targeted_population(database, collection, fields, period)]`
&nbsp;
    ```python
    from dowellpopulation import targeted_population
    def tp_report_fetch():
        field = "test_data"
        time_period = "life_time"
        fetch_data= targeted_population("tp_reports","Reports",[field],time_period)
        return fetch_data

    print(tp_report_fetch())
    ```
    - **field** is where you want to apply the dowellpopulation function.
    - **time_period** is for time interval you need data 


## WorkflowAi Reports
```json
{
    "eventId":"eventId",
    "Reort_from_sheet":{
        "report":[
            "DOCUMENTATION","ADMIN","SIGN","TIME","MINUTE","DUPLI NO"
            ],
    "WorkflowAi_report":{
        "product_report":"product_report"
    }
}
```
```json
{
    "eventId":"eventId",
    "Reort_from_sheet":{
        "report":[
            "DOCUMENTATION","ADMIN","SIGN","TIME","MINUTE","DUPLI YES"
            ],
    "WorkflowAi_report":{
        "product_report":"product_report"
    }
}
```

## Hr Report
```json
{
    "eventId":"eventId",
    "Reort_from_sheet":{
        "report":[
            "DOCUMENTATION","ADMIN","SIGN","TIME","MINUTE","DUPLI NO"
            ],
    "HR_report":{
        "product_report":"product_report"
    }
}
```
```json
{
    "eventId":"eventId",
    "Reort_from_sheet":{
        "report":[
            "DOCUMENTATION","ADMIN","SIGN","TIME","MINUTE","DUPLI YES"
            ],
    "HR_report":{
        "product_report":"product_report"
    }
}
```




## Report for WOrkflowAi 

- let say WorkflowAi db has 3 collections
    1. document_creation
    2. sign_order
    3. template_creation
- targeted_popplation_function("workflowai","document_creation",['document'],"life_time") = "product_db"
- connection_function("TP_Reports","tp_reports","Reports","Reports","1000001","ABCDE","insert",field)

```json
field= {
"eventId":"eventId",
"Reort_from_sheet":{
    "report":[
        "DOCUMENTATION","ADMIN","SIGN","TIME","MINUTE","DUPLI NO"
    ]
},
"WorkflowAi_report":{
    "product_report":"whatever you got from the targeted population function in line number 2"
}
}   
```
