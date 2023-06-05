'''
Є список contacts, елементи якого - словники контактів наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача, його email, телефонний номер та властивість - обраний контакт чи ні.

Створіть функцію get_favorites(contacts), яка повертатиме список, який містить лише обрані контакти. 
Використовуйте при цьому функцію filter, щоб відфільтрувати по полю favorite лише обрані контакти.
'''


contacts = [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}, 
            {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}, 
            {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038', 'favorite': True}, 
            {'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False}, 
            {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': True}]


def get_favorites(contacts):
    return [i for i in filter(lambda x: x['favorite'] == True, contacts)]
    

print(get_favorites(contacts))