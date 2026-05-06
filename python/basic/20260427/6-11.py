cities = {
    'New York': {
        'country': 'USA',
        'population': 8419000,
        'fact': 'The Statue of Liberty is located in New York.',
    },
    'Beijing': {
        'country': 'China',
        'population': 21540000,
        'fact': 'The Great Wall of China is located near Beijing.',
    },
    'ChangSha':{
        'country': 'China',
        'population': 8000000,
        'fact': 'ChangSha is known for its spicy food.',
    },
}

for city,info in cities.items():
    print(f"\nCity: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
