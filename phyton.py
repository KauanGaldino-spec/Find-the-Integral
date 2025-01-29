def find_integral(coefficient, exponent):
    # Aumenta o expoente em 1
    new_exponent = exponent + 1
    
    # Divide o coeficiente pelo novo expoente
    new_coefficient = coefficient // new_exponent
    
    # Retorna o resultado como uma string no formato "ax^b"
    return f"{new_coefficient}x^{new_exponent}"

# Exemplos de uso
print(find_integral(3, 2))   # Saída: "1x^3"
print(find_integral(12, 5))  # Saída: "2x^6"
print(find_integral(20, 1))  # Saída: "10x^2"
print(find_integral(40, 3))  # Saída: "10x^4"
print(find_integral(90, 2))  # Saída: "30x^3"