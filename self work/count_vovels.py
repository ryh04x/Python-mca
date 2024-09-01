# defining a function for this work

def count_vowels(s):
    
    
    # Defining vovels in a set (both upper case as well as lower case)
    vovels = set("aeiouAEIOU")
    
    
    # set vovel count in string to zero
    count = 0
    
#    loop to check each char in string
   
    for char in s:
        if char in vovels:
            count += 1
            
            
    return count
        
        
while True:
    # Take input from user
    input_string = input("Enter a string to check for vowels (or type 'exit' to quit): ")
    
    
    # Check if user wants to exit
    if input_string.lower() == 'exit':
        print("Exiting the program.")
        break
    
    
    print("Number of vowels:", count_vowels(input_string))