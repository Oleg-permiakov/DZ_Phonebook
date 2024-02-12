# Дополнить телефонный справочник возможностью изменения и удаления данных (по выбору). Пользователь так же может
# ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.


def input_surname():
    return input("Введите фамилию контакта: ").title() #  .title - Позволяет не учитывать регистр при вводе

def input_name():
    return input("Введите имя контакта: ").title()

def input_patronymic():
    return input("Введите отчество контакта: ").title()


def input_phone():
    return input("Введите телефон контакта: ")

def read_file():
    with open('Phonebook.txt', 'r', encoding='utf-8') as file:
        return file.read()


def edit_contact():
    print('Введите полную запись контакта, который хотите изменить.')
    contact = create_contact()
    data = read_file()
    if contact in data:
        print("Введите новую запись: ")
        new_contact = create_contact()
        with open('Phonebook.txt', 'w', encoding='utf-8') as file:
            data = data.replace(contact, new_contact)
            file.write(data)
    else:
        print("нет такой записи")


def del_contact():
    print('Введите полную запись контакта, который хотите удалить.')
    print()
    contact = create_contact()
    data = read_file()
    if contact in data:
        with open('Phonebook.txt', 'w', encoding='utf-8') as file:
            data = data.replace(contact, "")
            file.write(data)
    else:
        print("Контакт не найден")   
        

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f"{surname} {name} {patronymic}: {phone}\n{address}\n\n" # Выводим в строку все наши данные



def input_address():
    return input("Введите город контакта: ").title()



def add_contakt(): # Создаём контакт в виде строки
    contact = create_contact()
    with open("phonebook.txt", 'a', encoding="utf-8") as file: # as file - Файловый дескриптор. С помощью его прописывают команды в файл
        file.write(contact)

def print_contakts(): # Выводим все контакты
    with open("phonebook.txt", 'r', encoding="utf-8") as file:
        contact_sstr = file.read()
        contact_list = contact_sstr.rsstrip().split("\n\n")
        # for contact in enumerate(contact_list, 1): # Пример использования enumerate
        #     print(*contact)
        for n, contact in enumerate(contact_list, 1): # Пример использования enumerate, нумерация начинается с 1
            print(n, contact) # Альтернативный вариант без звёздочки если понадобится нумерация

 
def search_kontakt():
    print(
            "Возможные варианты поиска:\n"
            "1. Фамилия\n"
            "2. Имя\n"
            "3. Отчество\n"
            "4. По телефону\n"
            "5. По адресу (город)"
            )  #\n - Это ставится что бы был перенос и начиналось с новой строки
    var = input("Выберите вариант поиска: ")
    while var not in ("1", "2", "3", "4", "5"):
        print("Не корректный ввод")
        var = input("Выберите вариант поиска: ")
    i_var = int(var) - 1
    search = input("Введите данные для поиска: ").title()
    with open("phonebook.txt", 'r', encoding="utf-8") as file:
        contact_sstr = file.read()
        contact_list = contact_sstr.rsstrip().split("\n\n")
        for sstr_contact in contact_list:
            lst_contact = sstr_contact.replace(":", "").split() # Пример как работать с replace
            if search in lst_contact[i_var]:
                print(sstr_contact)
              
        



def interface():
    with open("phonebook.txt", 'a', encoding="utf-8"): 
        pass            
    var = 0
    while var != "6":
        print(
            "Возможные варианты:\n"
            "1. Добавить контакт\n"
            "2. Вывести на экран \n"
            "3. Поиск контактам\n"
            "4. Редактировать данные\n"
            "5. Удалить контакт\n"
            "6. Выход"
             )  
        print()
        var = input("Выберите вариант действия: ")
        while var not in ("1", "2", "3", "4", "5", "6"):
            print("Не корректный ввод")
            var = input("Выберите вариант действия: ")
        print()

        if var == "1":
            add_contakt()
        if var == "2":
            print_contakts()
        if var == "3":
            search_kontakt()
        if var == "4":
            edit_contact()
        if var == "5":
            del_contact()
        if var == "6":
            print("До свидание")
    print()    


if __name__ == "__main__": 
    interface()  
    