

tests = {

    1: {"Label": "Run Test A","Password": "Fortniteleaks49","locked": False},

    2: {"Label": "Run Test B","Password": "Valorantpro123","locked": False}

}


def run_tests(test_id):
    test = tests[test_id]

    if test["locked"]:
        print(f"{test['Label']} is locked")
        return
    retries = 3
    while retries > 0:
        attempt = input(f"Enter password for {test['Label']}")
        if attempt == test["Password"]:
            print(f"Access Granted, running {test['Label']}")
            break
        else:
            retries -= 1
            print(f"Acces Denied. You have {retries} retries left.")  
    if retries == 0:
        test["locked"] = True
        print(f"Retries used up, {test['Label']} is now locked")
        return


loop = True
while loop:
    print("\n===TESTING MODULE===")

#Displays menu options
#Checks for valid input
    for test_id, data in tests.items():
        print(f"{test_id}. {data['Label']}")
    print("3. Exit") 
    try:
        choice = int(input("Select an option (1 - 3): "))
    except ValueError:
        print("INVALID INPUT, please enter a number (1-3)")
        continue   
    if choice == 3:
        print("Bye")
        loop = False
    elif choice in tests:
        run_tests(choice)
    else:
        print("Invalid option, please restart.")
            


      










