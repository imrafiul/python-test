import random
mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here

# print(mobile_data['data'][0].get('name'))

# name1 = mobile.get('name')

# total_usd = mobile_data['data'][0].get('price')
# total_rate = mobile_data['exchnage_rate']
# print(type(total_usd))

# bdt = total_usd * total_rate
# print(bdt)

for mobile in mobile_data['data']:
    name_1 = mobile.get('name')
    price_1 = mobile.get('price')
    made_1 = mobile.get('made')

    text = [f'The {name_1} is made in {made_1}. You can buy the mobile in Bangladesh is {price_1}.',
            f'{made_1} is the manufacturing country for {name_1}. In Bangladesh, the mobile price is {price_1}.']

    print(random.choice(text))





# print(name)

