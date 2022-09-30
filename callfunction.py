from dowelpopulation import targeted_population
from dowellconnections import dowellconnection
from dowellevent import get_event_id


#call dowellconnection function
def insert_id():
    field ={
        "eventId":get_event_id(),
        "test_data":"test_data" 
        }
    inserted_id= dowellconnection("TP_Reports","tp_reports","Reports","Reports","1000001","ABCDE","insert",field)
    return inserted_id

#call dowellpopulation function
def fetch_data():
    field = "test_data"
    time_period = "life_time"
    fetch_data= targeted_population("tp_reports","Reports",[field],time_period)
    return fetch_data

print(insert_id())
print(fetch_data())
