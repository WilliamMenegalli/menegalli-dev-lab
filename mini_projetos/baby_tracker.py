diapers = 0
feedings = 0
naps = 0

while True:
    print("\n=== Baby Tracker ===")
    print("1 - Add diaper")
    print("2 - Add feeding")
    print("3 - Add nap")
    print("4 - Show summary")
    print("5 - Exit")

    choice = input("Choose an option: ")
    if choice == "1" :
        diapers += 1
        print("Diaper added!")

    elif choice == "2" :
        feedings += 1
        print("Feeding added") 

    elif choice == "3" :
        naps += 1
        print("Nap added")

    elif choice == "4" :
        print("\n--- Daily Summary ---")
        print("Diapers:", diapers)
        print("Feedings:", feedings)    
        print("Naps:", naps)

    elif choice == "5":
        print("Exiting Baby Tracker...")
        break

    else:
        print("Invalid option. Try again.")
                       