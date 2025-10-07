first = 30.5

def huinya():
    global first
    first = 'blyat`'
    print(first)
    countries = ['Ukraine', 'Poland', 'USA']
    age_groups = ['under 18', '18-25', '26-40', '41-60', 'over 60']


    country = input(f"Choose your country {countries}: ")
    age = int(input("Enter your age: "))
    name = input("Enter your name: ")

    if age >= 18 and age <= 60:
        print("Welcome to the site!")
    else:
        print("Sorry, you are not allowed to enter the site.")

huinya()

print(first)