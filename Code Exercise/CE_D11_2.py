# The function we wrote in exercise 1 returned 9.7. 
# Change the function so this time it returns 
# Max: 9.7, Min: 9.2 
# where 9.7 is the maximum and 9.2 is the minimum.

def get_min_max():
    grades = [9.6, 9.2, 9.7]
    max_local = max(grades)
    min_local = min(grades)
    min_max = [max_local, min_local]
    return min_max
    
    
min_max_list = get_min_max()
print(f"Max: {min_max_list[0]}, Min: {min_max_list[1]}")    

