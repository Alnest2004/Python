
#key:value

#a= {word:len(word) for word in ['hello', 'hi', 'www']}
#print(a)

#data ={
#    'Джефф Безос': '177',
#    'ИлоН МаСк': '126',
#    'бернар АрнО': '150',
#    'БиЛл ГейтС': '124',
#    }
#.title делает все буквы маленькие за исключением первых
#new_data = {key.title():int(value) for key,value in data.items()}
#print(new_data)

users = [
    [0, "Bob", "password"],
    [1, "code", "python"],
    [2, "Stack", "overflow"],
    [3, "username", "1234"],   
    [51, "qwerty", "1234"], 
    ]

new_users = {user[0]:user for user in users}
print(new_users[51])