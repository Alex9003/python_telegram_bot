import json
from io import text_encoding

data = {
    'name' : 'Mike',
    'city': 'K-P',
    'hobbies': ['reading', 'walking']
}

with open('json.txt','w') as file:
    json.dump(data, file)

data_time = dict()
with open('json.txt', 'r') as file:
    data_time = json.load(file)
    print(data_time)

print(data_time['name'])