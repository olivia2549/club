print('''You wake up one morning and find that you aren't in your bed; you aren't even in your room.\n You're in the
middle of a giant maze. A sign is hanging from the ivy: ''')
print("You have one hour. Don't touch the walls.\n There is a hallway to your right and to your left.")

user_input = input("Type 'left' to go left or 'right' to go right: ")

# if user_input != "right" and user_input != "left":
#     while user_input != "right" and user_input != "left":
#         user_input = input("Invalid response. Please try again: ")
#         if user_input == "right" or user_input == "left":
#             break

if user_input == "left":
    print("You decide to go left and...") # Update to match your story.
    human = input("You see a human. His eyes are blank and he's hiding something in his hand. Do you approach him? Type 'yes' or 'no' ")
    # if human != "yes" and human != "no":
    #     while human != "yes" and human != "no":
    #         human = input("Invalid response. Please try again: ")
    #         break
    if human == "yes":
        print("You approach him, but he runs away, frightened.")
    elif human == "no":
        print("You stand still, unable to move. But he looks just as scared as you are. You make eye contact briefly then slowly walk away.")

elif user_input == "right":
    print("You choose to go right and ...")  # Update to match your story.
    beast = input("You see a beast. He seems frightened but is three times your size. Do you approach him?")
