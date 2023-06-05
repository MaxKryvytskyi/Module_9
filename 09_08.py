'''
Є список contacts, елементи якого - словники контактів наступного виду:

{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача, його email, телефонний номер та властивість - обраний контакт чи ні.

Розробіть функцію get_emails, яка отримує у параметрі список list_contacts та повертає список, 
який містить електронні адреси всіх контактів зі списку list_contacts. 
Використовуйте функцію map.
'''

contacts = [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}, 
{'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}, 
{'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038', 'favorite': False}, 
{'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False}, 
{'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': False}]


def get_emails(list_contacts):
    return list(map(lambda x : x['email'], list_contacts))

print(get_emails(contacts))
