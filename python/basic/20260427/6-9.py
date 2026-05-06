favorite_places = {
    'alice': ['paris', 'new york', 'tokyo'],
    'bob': ['london', 'sydney'],
    'charlie': ['rome', 'barcelona', 'amsterdam'],
}

for people, place in favorite_places.items():
    if len(place) == 1:
        print(f"\n{people.title()}'s favorite place is {place[0].
title()}.")
    else:
        print(f"\n{people.title()}'s favorite places are {', '.join([p
.title() for p in place])}.")