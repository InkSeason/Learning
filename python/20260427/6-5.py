rivers = {
    'Nile': 'The longest river in the world, flowing through '
    'northeastern Africa.',
    'Amazon': 'The largest river by discharge volume of water, flowing '
    'through South America.',
    'Yangtze': 'The longest river in Asia, flowing through China.',
    'Mississippi': 'A major river in the United States, flowing from '
    'Minnesota to the Gulf of Mexico.',
}
for river, profile in rivers.items():
    print(f"{river}:\n\t {profile}")
