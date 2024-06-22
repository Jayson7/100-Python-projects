def display_menu():
    print("Voting System")
    print("1. Vote for Candidate A")
    print("2. Vote for Candidate B")
    print("3. Vote for Candidate C")
    print("4. Show Results")
    print("5. Exit")

def cast_vote(votes):
    try:
        choice = int(input("Enter your vote (1-3): "))
        if choice == 1:
            votes['Candidate A'] += 1
        elif choice == 2:
            votes['Candidate B'] += 1
        elif choice == 3:
            votes['Candidate C'] += 1
        else:
            print("Invalid choice. Please vote for a valid candidate.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")

def show_results(votes):
    print("Voting Results:")
    for candidate, vote_count in votes.items():
        print(f"{candidate}: {vote_count} votes")

def main():
    votes = {'Candidate A': 0, 'Candidate B': 0, 'Candidate C': 0}
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1 or choice == 2 or choice == 3:
                cast_vote(votes)
            elif choice == 4:
                show_results(votes)
            elif choice == 5:
                print("Exiting the voting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
