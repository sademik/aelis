#THIS VERSION IS TRASH, ONLY HERE FOR LEARNING EXPERIENCE
#I REALIZED IT WAS A BAD IDEA TO TRY TO DO THIS WITH IF/ELSE STATEMENTS AND ABANDONED THIS VERSION

answer_one = ["1", "One", "one", "ONE"]
answer_two = ["2", "Two", "two", "TWO"]
answer_three = ["3", "Three", "three", "THREE"]
answer_four = ["4", "Four", "four", "FOUR"]

print("""
WELCOME TO AELIS

How did you sleep last night?

1 - Well, 2 - Fine, 3 - Poorly, 4 - Horribly
""")

ans1 = input(">>")

if ans1 in answer_one:
    print("\nGood to hear. What position to did you fall asleep in? \n \n1 - On my back, 2 - On my side, 3 - On my stomach, 4 - Cannot remember\n")

    ans2 = input(">>")

    if ans2 in answer_one:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    elif ans2 in answer_two:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    elif ans2 in answer_three:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    elif ans2 in answer_four:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    else:
        print("\nPlease enter a correct value.")

elif ans1 in answer_two:
    print("\nNothing wrong with some average sleep. What position to did you fall asleep in?\n \n1 - On my back, 2 - On my side, 3 - On my stomach, 4 - Cannot remember\n")

    ans2 = input(">>")

    if ans2 in answer_one:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    elif ans2 in answer_two:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    elif ans2 in answer_three:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    elif ans2 in answer_four:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    else:
        print("\nPlease enter a correct value.")

elif ans1 in answer_three:
    print("\nWell, at least you fell asleep.. What position to did you fall asleep in?\n \n1 - On my back, 2 - On my side, 3 - On my stomach, 4 - Cannot remember\n")

    ans2 = input(">>")

    if ans2 in answer_one:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    elif ans2 in answer_two:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    elif ans2 in answer_three:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    elif ans2 in answer_four:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    else:
        print("\nPlease enter a correct value.")

elif ans1 in answer_four:
    print("\nI'm really sorry to hear that. What position to did you fall asleep in?\n \n1 - On my back, 2 - On my side, 3 - On my stomach, 4 - Cannot remember\n")

    ans2 = input(">>")

    if ans2 in answer_one:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    elif ans2 in answer_two:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    elif ans2 in answer_three:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    elif ans2 in answer_four:
        print("\nI see. Was there much light in the room when you fell asleep? \n \n1 - Yes (Fairly bright), 2 - Some here and there (Warm glow), 3 - Only tiny light sources (Subtle glow), 4 - No (Pitch-black)\n")
   
        ans3 = input(">>")

        if ans3 in answer_one:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_two:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_three:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        elif ans3 in answer_four:
        print("\nI see. Were you listening to anything? \n \n1 - Yes (Livestream or video), 2 - Yes (Ambient music), 3 - Yes (White noise or natural sounds), 4 - No (Nothing)\n")

        else:
        print("\nPlease enter a correct value.")

    else:
        print("\nPlease enter a correct value.")

else:
    print("\nPlease enter a correct value.")