import json

contact = {
    "дядя Ваня": {'phones': [1212121, 5555555], 'email': '777@mail.com', 'birthday': '10.10.1990'},
    "дядя Вася": {'phones': [888888]},
}

contact["Igor"] = {'phones': [440440, 2202220]}

def save():
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(contact, ensure_ascii=False))
    print("Наша библиотека сохранена")

def load():
    global contact
    with open("films.json", "r", encoding="utf-8") as fh:
        contact = json.load(fh)
    print("Фильмотека загружена")
    return contact

while True:
    command = input("Введите команду ")
    if command == "/start":
        print("Справочник начал работу")
    elif command == "/stop":
        save()
        print("Справочник остановил работу")
        break
    elif command == "/all":
        print("Текущий список контактов:")
        print(contact)
    elif command == "/add":
        name = input("Введите имя ")
        phones = input("Введите телефоны через запятую ").split(",")
        phones = [int(phone.strip()) for phone in phones]
        email = input("Введите email ")
        birthday = input("Введите дату рождения (дд.мм.гггг) ")
        contact[name] = {'phones': phones, 'email': email, 'birthday': birthday}
        print(f"Контакт {name} добавлен в список")
    elif command == "/find":
        name = input("Введите имя: ")
        if name in contact:
            print(f"Телефоны: {contact[name]['phones']}")
            if 'email' in contact[name]:
                print(f"Email: {contact[name]['email']}")
            if 'birthday' in contact[name]:
                print(f"Дата рождения: {contact[name]['birthday']}")
        else:
            print("Контакт не найден")
    elif command == "/update":
        name = input("Введите имя контакта для изменения: ")
        if name in contact:
            field = input("Что вы хотите изменить (phones, email, birthday)? ")
            if field in contact[name]:
                new_value = input(f"Введите новое значение для {field}: ")
                if field == "phones":
                    new_value = [int(phone.strip()) for phone in new_value.split(",")]
                contact[name][field] = new_value
                print(f"Контакт {name} обновлен")
            else:
                print(f"Поле {field} не найдено у контакта {name}")
        else:
            print("Контакт не найден")
    elif command == "/delete":
        name = input("Введите имя контакта для удаления: ")
        if name in contact:
            del contact[name]
            print(f"Контакт {name} удален")
        else:
            print("Контакт не найден")
