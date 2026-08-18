print("lengh of a list without using len function")

def get_length(list1):    
    
    counter = 0
    
    for position in list1:
        counter += 1
    return counter    

list_sample =[2,3,5,4,3,2,5,4,6,"yam","maize","potatoes","plantain"]

    
length = get_length(list_sample)

print(length) 


