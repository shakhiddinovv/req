import requests
from collections import namedtuple

response = requests.get('https://dummyjson.com/users')
json_data = response.json()

Person = namedtuple('Person', ['id', 'name', 'email'])
Product = namedtuple('Product', ['id', 'name', 'price'])

persons = []
products = []

for data in json_data:
    person = Person(data['id'], data['name'], data['email'])
    persons.append(person)
    
    product = Product(data['id'], data['product'], data['price'])
    products.append(product)

for person in persons:
    print(f"ID: {person.id}, Name: {person.name}, Email: {person.email}")

for product in products:
    print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}")