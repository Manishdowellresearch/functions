from dowellpopulation import targeted_population
from dowellconnections import dowellconnection
from dowellevent import get_event_id


#call dowellconnection function for tp_reports
def tp_report_insert():
    field ={
        "eventId":get_event_id(),
        "company":"Dowell" ,
        "name":"Jobin",
        "location":"kerla"
        }
    inserted_id= dowellconnection("TP_Reports","tp_reports","Reports","Reports","1000001","ABCDE","insert",field)
    return inserted_id

#call dowellpopulation function for tp_reports
def tp_report_fetch():
    field = "company"
    time_period = "life_time"
    fetch_data= targeted_population("tp_reports","Reports",[field],time_period)
    return fetch_data

print(tp_report_insert())
print(tp_report_fetch())


