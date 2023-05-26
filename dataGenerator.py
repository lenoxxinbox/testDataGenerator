from random import randint
from russian_names import RussianNames


def test_data_write():
    phone = str(randint(79000000000, 79999999999))
    email = phone + '@test.mail'
    site = 'www.' + phone + '.site'

    name = RussianNames().get_person()
    first, two, last = str.split(name)

    with open('test_data.txt', 'a') as td:
        td.write(
            f"Name: {' '.join([last, first, two])}\n"
            f"Phone: {phone}\n"
            f"Email: {email}\n"
            f"Site: {site}\n"
            "________________________________________________________\n"
        )


def repeat_test_data_write(quantity, func):
    for i in range(quantity): func()


def clear_test_data_file(file):
    with open(file, 'w') as file:
        file.write("")


clear_test_data_file('test_data.txt')
repeat_test_data_write(5, test_data_write)
