
print("count number of string and return first & last character")

def get_count_of_string(count_string):

    same_first_and_last_char_strings = [] 
    
    for word in count_string:
    
        if len(word) >= 2 and word[0] == word[-1]:
        
            same_first_and_last_char_strings.append(word)
    
            
    
    return same_first_and_last_char_strings
    
items = ["aja","1971","liar","ole","first"]

output =  get_count_of_string(items)

print(output)
    
    
