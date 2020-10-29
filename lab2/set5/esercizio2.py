#from python dictionary to json file
import json
py_dict={'name':'David','class':'I','age':6}
json_obj=json.dumps(py_dict)
print(json_obj)