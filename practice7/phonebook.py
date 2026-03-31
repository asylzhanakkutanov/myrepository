import csv
from connect import get_connection

conn = get_connection()
cur = conn.cursor()

#CREATE TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    phone VARCHAR(20)
);
""")
conn.commit()

#INSERT FROM CONSOLE
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO contacts (first_name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("✅ Added successfully")

#INSERT FROM CSV
def insert_from_csv(file_name="contacts.csv"):
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            cur.execute("INSERT INTO contacts (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("✅ CSV data inserted")

#UPDATE CONTACT
def update_contact():
    name = input("Enter name to update: ")
    new_name = input("New name (leave empty if no change): ")
    new_phone = input("New phone (leave empty if no change): ")

    if new_name:
        cur.execute("UPDATE contacts SET first_name=%s WHERE first_name=%s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE contacts SET phone=%s WHERE first_name=%s", (new_phone, name))
    conn.commit()
    print("✅ Updated successfully")

#SEARCH
def search_contacts():
    print("1 - Search by name")
    print("2 - Search by phone prefix")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("SELECT * FROM contacts WHERE first_name ILIKE %s", ('%' + name + '%',))
    elif choice == "2":
        prefix = input("Enter prefix: ")
        cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (prefix + '%',))
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

#DELETE
def delete_contact():
    print("1 - Delete by name")
    print("2 - Delete by phone")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM contacts WHERE first_name=%s", (name,))
    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM contacts WHERE phone=%s", (phone,))
    
    conn.commit()
    print("✅ Deleted successfully")

#MENU
def menu():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Add from console")
        print("2. Add from CSV")
        print("3. Update contact")
        print("4. Search")
        print("5. Delete")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            search_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            break

    cur.close()
    conn.close()


if __name__ == "__main__":
    menu()