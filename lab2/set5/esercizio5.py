#siccome in questo caso prendi il json da file devi mettere load()
import json
with open('states.json','r') as f:
      py=json.load(f)
print(py)
for state in py['states']:
    del state['area_codes']
print(py)
with open('new_states.json','w') as f: #deve essere un nuovo file
     json.dump(py,f,indent=4) #indent ti dice solo lo spazio lasciato

