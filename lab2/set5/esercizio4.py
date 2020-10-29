#per passare da python a json e vuoi ordinare ci sta sort_keys
import json
j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
print('Original  String: ', j_str)
print('\nJSON  data: ')
print(json.dumps(j_str , sort_keys=True , indent =4))