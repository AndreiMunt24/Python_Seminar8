from random import *
import json
films=[]
films.append("Matrica")
films.append("solaris")
films.append("Vlastelin colec")
films.append("Resnia")
films.append("Barbara")


def save():
    with open("films.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print("Nasha biblioteca sohranena")

def load():
    with open("films.json","r",encoding="utf-8") as fh:
        films=json.load(fh)
    print("Filmoteca zagrujena")
    return films 

while True:
    command=input("Vvedite comand ")
    if command=="/start":
        print("Bot-filmoteka nachal rabotu")
    elif command=="/stop":
        save()
        print("Bot ostanovil raboty")
        break
    elif command=="/all":
        print("Tekushii spisok filmov")
        print(films)
    elif command =="/add":
        f=input("Vvedite nazvanie ")
        films.append(f)
        print("Film dobavlen v spisok")
    elif command=="/help":
        print("Manual")
    elif command=="/del":
        f=input("Vvedite nazvanie cotoroe ydalit ")
        '''   
        if f in films:
            films.remove(f)
            print("film ydalen")
        else:
            print("Tacogo filma net")    
        '''
        try:
            films.remove(f)
            print("film ydalen")
        except:
            print("Tacogo filma net")
    elif command=="/random":
        # rnd=randint(0, len(films) - 1)
        # print("slepoi grebii pokazal film - " + films[rnd])
        print("slepoi grebii pokazal film - " + choice(films) )
    elif command =="/save":
           save()
    elif command=="/load":
        load()
    else:
        print("Neopoznanai command")   
        