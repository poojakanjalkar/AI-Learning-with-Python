def analyze_text():
    print("Welcome! Enter any text, and I'll analyze it for you.")
    print("Type 'exit' to quit the program.")
    
    while True:
        # Get input from the user
        user_input = input("Enter your text: ")
        
        # Exit condition
        # if user_input.lower() == 'exit':
        #     print("Goodbye! Have a great day!")
        #     break
        
        # Processing the input
        word_count = len(user_input.split())
        char_count = len(user_input)
        vowels = "aeiouAEIOU"
        vowel_count = sum(1 for char in user_input if char in vowels)
        
        # Displaying the analysis
        print("\nText Analysis:")
        print(f"1. Number of words: {word_count}")
        print(f"2. Number of characters (including spaces): {char_count}")
        print(f"3. Number of vowels: {vowel_count}")
        print("-" * 30)

# Call the function
analyze_text()
