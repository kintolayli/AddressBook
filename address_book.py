import pickle
import sys
import os

AB_DATA = 'address_book.data'
PATH_DATA = os.getcwd() + os.sep + AB_DATA
MESSAGE = '''when you first run this program, you must add one command-line argument:

add - add new contact
show - show all contacts, which you have
how_many - how many contacts you have
find - find contact by first name, or last name
edit - edit contact
del - delete contact

for example: (run in command prompt) - python3 address_book add  
'''


class Person:
    def __init__(self, first_name, last_name, address):
        self.person_id = iteration_id()
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def introduce_myself(self):
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
    first_name = input('Enter first name:\n')
    last_name = input('Enter last name:\n')
    address = input('Enter address:\n')
    if os.path.exists(PATH_DATA):
        data = load_data()
        append_person_to_data(data, first_name, last_name, address)
    else:
        data = {}
        append_person_to_data(data, first_name, last_name, address)
    print()
    print('Contact added')


def show_person():
    if os.path.exists(PATH_DATA):
        data = load_data()
        if data != {}:
            for value in data.values():
                value.introduce_myself()
        else:
            print('You don\'t have any contacts.')
    else:
        print('You don\'t have any contacts.')


def edit_person():
    if os.path.exists(PATH_DATA):
        data = load_data()
        if data != {}:
            find_person('Enter contact\'s first name, or last name, which you will want to change:\n')
            find_object = int(input('Enter ID:'))
            person = data.get(find_object)
            if person is not None:
                new_first_name = input(f'Enter new first name (old first name: {person.first_name}):  ')
                new_last_name = input(f'Enter new last name (old last name: {person.last_name}):  ')
                new_address = input(f'Enter new address (old address: {person.address}):  ')
                person.edit(new_first_name, new_last_name, new_address)
                edit_person_in_data(data, person)
            else:
                print(f'Contact with ID{find_object} not exist.')
        else:
            print('You don\'t have any contacts.')
    else:
        print('You don\'t have any contacts.')


def how_many_person():
    if os.path.exists(PATH_DATA):
        data = load_data()
        if data != {}:
            print(f'You have {len(data)} contacts.')
        else:
            print('You don\'t have any contacts.')
    else:
        print('You don\'t have any contacts.')


def find_person(search_phrase):
    if os.path.exists(PATH_DATA):
        data = load_data()
        if data != {}:
            find_object = input(search_phrase).lower()
            for value in data.values():
                value.find_match(find_object)
        else:
            print('You don\'t have any contacts.')
    else:
        print('You don\'t have any contacts.')


def del_person():
    if os.path.exists(PATH_DATA):
        data = load_data()
        if data != {}:
            find_person('Enter contact\'s first name, or last name, which you will want to delete:\n')
            find_object = int(input('Enter ID:'))
            person = data[find_object]
            if person is not None:
                del_person_in_data(data, person)
                print(f'Contact {person.first_name} {person.last_name} was deleted.')
            else:
                print(f'Contact with ID{find_object} not exist.')
        else:
            print('You don\'t have any contacts.')
    else:
        print('You don\'t have any contacts.')


def main():
    if len(sys.argv) == 1:
        print(MESSAGE)

    elif sys.argv[1] == 'add':
        add_person()

    elif sys.argv[1] == 'show':
        show_person()

    elif sys.argv[1] == 'how_many':
        how_many_person()

    elif sys.argv[1] == 'find':
        find_person('Enter a search term:\n')

    elif sys.argv[1] == 'edit':
        edit_person()

    elif sys.argv[1] == 'del':
        del_person()


if __name__ == '__main__':
    main()
