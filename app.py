from RData import RDataStore

ds = RDataStore()
while(True):
    print("R-DATASTORE BY RAHUL HEGDE")
    print("1. Create\n 2. Read\n 3. Delete\n 4. Print")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("CREATE OPERATION")
        key = input("Enter key: ")
        json_object = input("Enter value(JSON object): ") #{"firstName":"John", "lastName":"Doe"}
        ttl = int(input("Enter time to live: "))
        print(ds.create(key, json_object, ttl))

    elif choice == 2:
        print("READ OPERATION")
        key = input("Enter key: ")
        print(ds.read(key))

    elif choice == 3:
        print("DELETE OPERATION")
        key = input("Enter key: ")
        print(ds.delete(key))

    elif choice == 4:
        print("DATA STORED AS data_store.json")
        ds.print_data()

    else:
        print("Invalid choice")
