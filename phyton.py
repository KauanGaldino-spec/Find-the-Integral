def find_integral(coefficient, exponent):
    
    new_exponent = exponent + 1
    
    
    new_coefficient = coefficient // new_exponent
    
    
    return f"{new_coefficient}x^{new_exponent}"


print(find_integral(3, 2))   
print(find_integral(12, 5)) 
print(find_integral(20, 1))  
print(find_integral(40, 3))  
print(find_integral(90, 2))  
