import pickle
import sys
import os.path

AB_DATA = 'address_book.data'
PATH_DATA = os.getcwd() + os.sep + AB_DATA


class Person:
    def __init__(self, first_name, last_name, address):
        self.person_id = iteration_id()
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def introduce_myself(self):
        #  print(f'ID: {self.person_id} Имя: {self.first_name} Фамилия: {self.last_name} Адрес: {self.address}')
        print(f'ID{self.person_id} {self.first_name} {self.last_name} Адрес: {self.address}')

    def edit(self, new_first_name, new_last_name, new_address):
        if new_first_name == '':
            self.first_name = self.first_name
        else:
            self.first_name = new_first_name

        if new_last_name == '':
            self.last_name = self.last_name
        else:
            self.last_name = new_last_name

        if new_address == '':
            self.address = self.address
        else:
            self.address = new_address

    def find_match(self, find_object):
        if find_object == self.first_name.lower() or find_object == self.last_name.lower():
            self.introduce_myself()

    def find_id(self, find_object):
        if int(find_object) == self.person_id:
            return self


def load_data():
    global AB_DATA
    with open(AB_DATA, 'rb') as f:
        data = pickle.load(f)
        return data


def iteration_id():
    if os.path.exists(PATH_DATA):
        data = load_data()
        if data != {}:
            list_keys = list(data.keys())
            list_keys.sort(reverse=True)

            return list_keys[0] + 1
        else:
            return 0
    else:
        return 0


def append_person_to_data(data, first_name, last_name, address):
    person = Person(first_name, last_name, address)
    data[person.person_id] = person
    with open(AB_DATA, 'wb') as f:
        pickle.dump(data, f)


def edit_person_in_data(data, person):
    data[person.person_id] = person
    with open(AB_DATA, 'wb') as f:
        pickle.dump(data, f)


def del_person_in_data(data, person):
    del data[person.person_id]
    with open(AB_DATA, 'wb') as f:
        pickle.dump(data, f)


def add_person():
    print('Режим добавления контакта')
    first_name = input('Введите имя:\n')
    last_name = input('Введите фамилию:\n')
    address = input('Введите адрес:\n')
    if os.path.exists(PATH_DATA):
        data = load_data()
        append_person_to_data(data, first_name, last_name, address)
    else:
        data = {}
        append_person_to_data(data, first_name, last_name, address)
    print()
    print('Контакт добавлен')


def show_person():
    if os.path.exists(PATH_DATA):
        data = load_data()
        if data != {}:
            for value in data.values():
                value.introduce_myself()
        else:
            print('У вас нет контактов.')
    else:
        print('У вас нет контактов.')


def edit_person():
    if os.path.exists(PATH_DATA):
        data = load_data()
        if data != {}:
            find_person('Введите имя или фамилию контакта, который хотите изменить:\n')
            find_object = int(input('Введите ID:'))
            person = data.get(find_object)
            if person is not None:
                new_first_name = input(f'Введите новое имя контакта(старое имя: {person.first_name}):  ')
                new_last_name = input(f'Введите новую фамилию контакта(старая фамилия: {person.last_name}):  ')
                new_address = input(f'Введите новый адрес контакта(старая адрес: {person.address}):  ')
                person.edit(new_first_name, new_last_name, new_address)
                edit_person_in_data(data, person)
            else:
                print(f'Контакта с ID{find_object} не существует.')
        else:
            print('У вас нет контактов.')
    else:
        print('У вас нет контактов.')


def how_many_person():
    if os.path.exists(PATH_DATA):
        data = load_data()
        if data != {}:
            print(f'У вас {len(data)} контактов.')
        else:
            print('У вас нет контактов.')
    else:
        print('У вас нет контактов.')


def find_person(search_phrase):
    if os.path.exists(PATH_DATA):
        data = load_data()
        if data != {}:
            find_object = input(search_phrase).lower()
            for value in data.values():
                value.find_match(find_object)
        else:
            print('У вас нет контактов.')
    else:
        print('У вас нет контактов.')


def del_person():
    if os.path.exists(PATH_DATA):
        data = load_data()
        if data != {}:
            find_person('Введите имя или фамилию контакта, который хотите удалить:\n')
            find_object = int(input('Введите ID:'))
            person = data[find_object]
            if person is not None:
                del_person_in_data(data, person)
                print(f'Контакт {person.first_name} {person.last_name} удален.')
            else:
                print(f'Контакта с ID{find_object} не существует.')
        else:
            print('У вас нет контактов.')
    else:
        print('У вас нет контактов.')


#  person1 = add_person('Игорь', 'Верник', 'ул. Маршала бирюзова д.8 кв. 147')
#  person2 = add_person('Владимир', 'Курчатов', 'ул. Малого Синяка д.3 кв. 35')
#  person3 = add_person('Денис', 'Ткаченко', 'ул. Третьяка д.24 кв. 97')
#  person4 = add_person('Виктор', 'Жардиев', 'ул. Сезонная д.1 кв. 4')
#  person1.introduce_myself()

#  edit_person()

if sys.argv[1] == 'add':
    add_person()

if sys.argv[1] == 'show':
    show_person()

if sys.argv[1] == 'how_many':
    how_many_person()

if sys.argv[1] == 'find':
    find_person('Введите слово для поиска:\n')

if sys.argv[1] == 'edit':
    edit_person()

if sys.argv[1] == 'del':
    del_person()
