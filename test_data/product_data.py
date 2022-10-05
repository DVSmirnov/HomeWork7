import random

adding_products = [

    {
        'product_name': 'Seimens',
        'meta_tag_title': 'mobile',
        'description': 'test111',
        'model': 'A35'
    },
    {
        'product_name': 'Nokia',
        'meta_tag_title': 'smartphone',
        'description': 'test222',
        'model': 'N-Gage QD'
    },
    {
        'product_name': 'HTC',
        'meta_tag_title': 'communicator',
        'description': 'test333',
        'model': '7 Pro'
    }

]


def add_product():
    return random.choice(adding_products)
