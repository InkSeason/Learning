favorite_languages = {
      'jen': 'python',
      'sarah': 'c',
      'edward': 'ruby',
      'phil': 'python',
      }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

names = ['jen', 'sarah', 'edward', 'phil']

for name in names:
    if name in favorite_languages:
        print(f"Thank you, {name.title()}, for taking the poll.")
    else:
        print(f"{name.title()}, please take our poll!")