import json
contact = {"дядя Ваня": {'phones': [1212121,5555555],
                           'email': '777@mail.com', 'birthday': '10.10.1990'},
             "дядя Вася": {'phones': [888888]}                         
            }
    
contact["Igor"] = {'phones':[440440, 2202220]}

def save():
    with open("films.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(contact,ensure_ascii=False))
    print("Nasha biblioteca sohranena")

def load():
    with open("films.json","r",encoding="utf-8") as fh:
        contact=json.load(fh)
    print("Filmoteca zagrujena")
    return contact


    
while True:
    command=input("Vvedite comand ")
    if command=="/start":
        print("spravochnic nachal rabotu")
    elif command=="/stop":
        save()
        print("spravochnic ostanovil raboty")
        break
    elif command=="/all":
        print("Tekushii spisok contactov")
        print(contact)
    elif command =="/add":
        f=input("Vvedite imia ")
        contact.append(f)
        print("contact dobavlen v spisok")
    elif command=="/find":
        name = input("Vvedite imia: ")
        print(contact[name]['phones']) 
        
        
