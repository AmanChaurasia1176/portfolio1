import json

# File to store user data
DATABASE_FILE = "user_data.json"

def load_data():
    """Load user data from the file."""
    try:
        with open(DATABASE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_data(data):
    """Save user data to the file."""
    with open(DATABASE_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_user(name, age, address):
    
    data = load_data()
    data[name] = {
        "age": age,
        "address": address
    }
    save_data(data)
    print(f"User {name} added successfully.")

def get_user(name):
    """Retrieve user information by name."""
    data = load_data()
    user = data.get(name)
    if user:
        print(f"Name: {name}\nAge: {user['age']}\nAddress: {user['address']}")
    else:
        print(f"User {name} not found.")

def main():
    while True:
        print("\nOptions:")
        print("1. Add user")
        print("2. Get user")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            address = input("Enter address: ")
            add_user(name, age, address)
        elif choice == "2":
            name = input("Enter name to retrieve: ")
            get_user(name)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
