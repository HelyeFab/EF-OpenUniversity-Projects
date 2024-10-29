
def reverse_in_place(values):
    left = 0
    right = len(values) - 1
    
    while left < right:
        # Swap elements at left and right indices
        values[left], values[right] = values[right], values[left]
        
        # Move the pointers towards the center
        left += 1
        right -= 1
        
# Test the function
test_str = [1, 2, 3, 4, 5]
test_str_1 = ["h","e","l","l","o"]

reverse_in_place(test_str_1)
print(test_str_1)  # Expected output: [5, 4, 3, 2, 1]



#Reversing a string in place
def reverse_string_in_place(s):
    # Convert string to a list of characters
    char_list = list(s)
    
    # Initialize two pointers
    left = 0
    right = len(char_list) - 1
    
    # Reverse in place
    while left < right:
        # Swap characters
        char_list[left], char_list[right] = char_list[right], char_list[left]
        
        # Move pointers towards the center
        left += 1
        right -= 1
    
    # Join the list back into a string
    return ''.join(char_list)

# Reverse a string  in a one-liner
def reverse_string(s):
    return s[::-1]

print(sorted([1, 4, 3, 2, 5], reverse=True) ) # Expected output: [5, 4, 3, 2, 1]

