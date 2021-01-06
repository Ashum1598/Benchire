import json
user_dict ={"Emp_Name":"Ashutosh","Emp_Id":121,"salary":25000}

json_dict=json.dumps(user_dict,indent=4)
print(json_dict)
