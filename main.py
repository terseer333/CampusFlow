menu = """
========================================
          CAMPUSFLOW HELPDESK
========================================
 1. Create a new ticket
 2. List all tickets
 3. View one ticket
 4. Assign a ticket
 5. Change ticket status
 6. Reopen a resolved ticket
 7. Show work queue
 8. Show reports
 0. Exit
========================================
"""

while True:
    print(menu)
    choice = input("Pick (0 to 8): ")

    if choice == "1":
        print("Create a new ticket")
    elif choice == "2":
        print("List all tickets")
    elif choice == "3":
        print("View one ticket")
    elif choice == "4":
        print("Assign a ticket")
    elif choice == "5":
        print("Change ticket status")
    elif choice == "6":
        print("Reopen a resolved ticket")
    elif choice == "7":
        print("Show work queue")
    elif choice == "8":
        print("Show reports")
    elif choice == "0":
        print("Goodbye")
        break
    else:
        print("Invalid choice")