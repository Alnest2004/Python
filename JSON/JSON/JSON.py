#
#load = когда мы считываем файл json
#loads= когда мы считываем строку в формате json
#dump = создаёт файл
#dumps = создаёт строку в виде json
import json
from random import randint
from datetime import datetime
'''
str_json ="""
{
"response":{
    "count": 5961878,
    "items": [{
        "first_name": "Елизавета",
        "id":620471795,
        "last_name": "Сопова",
        "can_access_closed": true
    }, {
        "first_name": "Роман",
        "id":614752515,
        "last_name": "Малышев",
        "can_access_closed": true
}]
}
}"""

data=json.loads(str_json)
for item in data['response']['items']:
    del item['id']
    item['likes'] = randint(100,200)
    item['a'] = None
    item['Now'] = datetime.now().strftime('%d/%m/%y')

print(data['response']['items'])
#Создаёт и записывает в json файл
#with open('my.json', 'w') as file:
    #json.dump(data, file, indent=3, ensure_ascii=False)
'''
#Считывает json файл
with open('my.json', 'r') as file:
    data = json.load(file)

print(data)


#new_json = json.dumps(data, indent=2, ensure_ascii=False)
#print(new_json)

#print(json.loads(new_json))