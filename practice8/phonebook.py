
from connect import get_connection

def add_or_update_contact(name, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Added/Updated successfully")

def search_contacts():
    conn = get_connection()
    cur = conn.cursor()
    pattern = input("Enter name or phone pattern: ")
    cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def delete_contact():
    conn = get_connection()
    cur = conn.cursor()
    query = input("Enter name or phone to delete: ")
    cur.execute("CALL delete_contact(%s)", (query,))
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Deleted successfully")

def menu():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Add/Update contact")
        print("2. Search contacts")
        print("3. Delete contact")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            add_or_update_contact(name, phone)
        elif choice == "2":
            search_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "0":
            break

if __name__ == "__main__":
    menu()