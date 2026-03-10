import os

def save_names(names):
    with open("names.txt", "w") as f:
        for n in names:
            f.write(n + "\n")

def main():
    names = []
    # Load existing names (Persistence)
    if os.path.exists("names.txt"):
        with open("names.txt", "r") as f:
            names = [line.strip() for line in f.readlines()]

    print("--- Hello App ---")
    new_name = input("Add a name to the list: ")
    names.append(new_name)

    save_names(names) # Save to file

    print("\nSaved Names:")
    for n in names:
        print(f"** {n} **") # Banner-ish format

if __name__ == "__main__":
    main()
