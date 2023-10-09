def main():
    while True:
        cmd = input("Enter command: ")
        if cmd == ".exit":
            print("Shutting down...")
            return
        else:
            print("Unrecognized command, please try again")


if __name__ == "__main__":
    main()
