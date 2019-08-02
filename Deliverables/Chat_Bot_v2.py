# --- Define your functions below! ---
def intro():
    print("Welcome to ChatBot!")

def process_name(answer):
    print("Hi there", answer)

##def How_do_you_feel(answer):
##    answer = input("How are you doing today?")
##    if feelingood():
##        answer = ("That's cool :)")
    
def feelingood(answer):
    if answer == "good" or answer == "cool" or answer == "fine" or answer == "ok":
        return True
    
def How_do_you_feel(answer):
    if feelingood(answer):
        print("That's cool :)")

# --- Put your main program below! ---
def main():
    intro()
    name = input("What's your name?")
    process_name(name)
    answer = input("How are you doing today?")
    How_do_you_feel(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
