pets = [
    {'kind': 'golden retriever',
        'owner': 'Alice',
    },
    {'kind': 'Chinese Rural Dog',
     'owner': 'Bob',
    },
    {'kind': 'Persian Cat',
     'owner': 'Charlie',
    },
]

for pet in pets:
    print(f"\nKind: {pet['kind']},\nOwner: {pet['owner']}")