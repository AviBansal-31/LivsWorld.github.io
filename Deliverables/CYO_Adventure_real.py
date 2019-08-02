start = '''
You are Monet, a young adventurer on your home planet. After weeks of boredom, you're looking for some excitement
'''
print(start)

user_input = input("I want to go on an adventure! Where should I go, dino land or fantasy land? ")
if user_input == "dino land":
    print("Ok! let's go!")

    print("You fly off in your rocketship and land in the heart of dino land. A blue dinosaur approaches you")
    
    user_input_dino = input("He says: Hello human! Would you like to meet the other dinos? yes or no?")

    if user_input_dino == "yes":
        print("Great they are right behind me!")
        print("You walk around meeting the other dinos and they all say hi!")
        print("THE END")

    elif user_input_dino == "no":
        print("Then I am going to have to eat you!!!")
        print("You make a quick getaway in your rocket ship, never to return again...")
        print("THE END")

elif user_input == "fantasy land":
    print("Sounds good, let's go!")

    print("You fly off in your rocketship and land deep in the forest of fantasy land. An old wizard approaches you.")

    user_input_fantasy = input("He says: Greetings muggle, would you like to become a magical creature? yes or no?")
        
    if user_input_fantasy == "yes":
          user_input_creature = input("Great would you like to become a unicorn or dragon?")
          if user_input_creature == "unicorn":
              print("You immediatly transform into a magestic unicorn forever")
              print("THE END")
          elif user_input_creature == "dragon":
              print("In the blink of an eye you transform into a ferocious dragon")
              print("THE END")

    elif user_input_fantasy == "no":
        print("Then I am going to have to shrink you!!")
        print("You quickly shrink until you cease to exist")
        print("OH NO!")
        print("THE END")

else:
    print("try again")
          

    


    
