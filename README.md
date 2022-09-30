# Documentation
    
1.  Details about the files

    - dowellconnection.py , has dowellconnection function.
    - dowellevent.py , has dowelleventcreation function.
    - dowellpopulation.py , has targeted population function. 
    - callfunction.py , has function call and database and collection details
2.  Dowellconnection function
   function call : ==dowellconnection(cluster,database,collection,document,team_member_ID,function_ID,command,field)==
    ```python
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
3. Dowellpopulation function
function call : ==targeted_population(database, collection, fields, period)==
    ```python
    def tp_report_fetch():
        field = "test_data"
        time_period = "life_time"
        fetch_data= targeted_population("tp_reports","Reports",[field],time_period)
        return fetch_data

    print(tp_report_fetch())
    ```
    - **field** is where you wnat to apply the dowellpopulation function.
    - **time_period** is for time interval you need data 
