from dowellpopulation import targeted_population
from dowellconnections import dowellconnection
from dowellevent import get_event_id


"""#call dowellconnection function for tp_reports
def tp_report_insert():
    field ={
        "eventId":get_event_id(),
        "test_data":"test_data" 
        }
    inserted_id= dowellconnection("TP_Reports","tp_reports","Reports","Reports","1000001","ABCDE","insert",field)
    return inserted_id

#call dowellpopulation function for tp_reports
def tp_report_fetch():
    field = "test_data"
    time_period = "life_time"
    fetch_data= targeted_population("tp_reports","Reports",[field],time_period)
    return fetch_data

print(tp_report_insert())
print(tp_report_fetch())
"""

def login():
    field ={
        "Username":"Manish"
        }
    inserted_id= dowellconnection("login","login","registration","registration","10004545","ABCDE","fetch",field)
    return inserted_id

print(login())

#with session id
[{'_id': '6336ba226ff5ee25ad5c30a0', 'Username': 'ericmbuthia11', 
'OS': 'Windows10', 'Device': 'could not get device name', 'Browser': 'Chrome105',
 'Location': '12.9858675 77.7645428', 'Time': '9/30/2022, 3:09:06 PM', 
'SessionID': 'xvpvonurz5cgrse3ca2u4kk453la2rse', 'Connection': '', 'event_id': 'FB1010000000166453097356489968', 
'IP': '', 'user_id': 570}]

[{'_id': '6336b4cff35d9021cc5c3231', 'Username': 'rahulworkflowai', 
'OS': 'Windows6.2', 'Device': '', 'Browser': 'Firefox105', 'Location': '', 
'Time': '30/9/2022, 2:50:00 pm', 'SessionID': '40ye2koz7wa4bdv4lqi2cbpf3a8s5w8l',
 'Connection': '', 'event_id': 'FB1010000000166452961051784172', 'IP': '', 'user_id': 859}]

[{'_id': '6336bc136ff5ee25ad5c30b3', 'Username': 'rahulworkflowai', 'OS': 'Windows10',
  'Device': 'could not get device name', 'Browser': 'Chrome105', 'Location': '12.9858675 77.7645428', 
  'Time': '9/30/2022, 3:20:52 PM', 'SessionID': '30qcmob5qka9vfkjlcodonh2skxydqjr', 
 'Connection': '', 'event_id': 'FB1010000000166453147053763587', 'IP': '', 'user_id': 859}]

#with user name
[{'_id': '632c4e6964a57fb79795b441', 'Username': 'rahulworkflowai', 'Password': 'Abcd$1234',
  'Firstname': 'Rahul', 'Lastname': 'Documentation', 'Email': 'rahultadola@gmail.com', 'Role': 'User', 
 'Team_Code': '100084', 'phonecode': '+91', 'Phone': '8888444422',
  'user_id': 'userid', 'company_id': '6', 'profile_id': 100238}]

[{'_id': '62e421d67cb119927d3f0b00', 'Username': 'ericmbuthia11', 'Password': 'pass123456@PASS', 
'Firstname': 'Eric', 'Lastname': 'Mbuthia', 'Email': 'ericmbuthia11@gmail.com', 
'Role': 'User', 'Team_Code': '100025', 'phonecode': '+91', 'Phone': '0707097832', 'user_id': 'userid', 'profile_id': 100123}]

#new account
[{'_id': '6336ace2f35d9021cc5c3160', 'Username': 'ManishDash', 'Password': 'Q1e2r3s4$', 'Firstname': 'Manish dash', 'Lastname': '', 
'Email': 'mdashsharma95@gmail.com', 'Role': 'User', 'Team_Code': '', 'phonecode': '+91', 'Phone': '7008974795', 'user_id': 'userid'}]

