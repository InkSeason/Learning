dining_count = input("How many people dining now? ")
dining_count = int(dining_count)
if dining_count > 8:
    print("Sorry, you have to wait for a table.")
else:
    print("Your table is ready.")