print("Helloworld")
def main():
    # Your existing code here (e.g., print("Hello, World!"))

    # Get the current date and time
    #now = datetime.datetime.now()

    # Write to the text file
    with open("output.txt", "a") as file:
        file.write("Hello, World!")

if __name__ == "__main__":
    main()
