#from json to python dictionary
#siccome in questo caso ti prendi una stringa ci vuole il loads()
import json
json_obj='{"Name":"David","Class":"I","Age":6}'
py_dict=json.loads(json_obj)
print(py_dict["Name"])
