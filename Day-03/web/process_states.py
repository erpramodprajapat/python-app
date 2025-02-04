''' JavaScript Object Notation '''
import json
#Deserialization
with open("C:\\py-tt\\Day-03\\web\\states.json") as f:
  data = json.load(f)

#Filtering
for state in data['states']:
  del state['area_codes']

#Serialization
with open("C:\\py-tt\\Day-03\\web\\new_states.json", 'w') as f:
  json.dump(data, f, indent=2)

print("new file created.. open new_states.json")