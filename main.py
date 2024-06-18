from mood_functions import happy, sad, angry, nervous, excited # Importing each of our functions from our mood_functions module.

def main():
    while True:
        user_mood = input('''
How are you feeling today? 
1. Happy
2. Sad
3. Angry
4. Nervous
5. Excited
6. Quit
''')
        if user_mood == '1':
            happy()
        elif user_mood == '2':
            sad()
        elif user_mood == '3':
            angry()
        elif user_mood == '4':
            nervous()
        elif user_mood == '5':
            excited()
        elif user_mood == '6':
            print("Thanks for using our mood app! Have a great day!")
            break
        else:
            print("Invalid entry. Please try again")
            continue

main()