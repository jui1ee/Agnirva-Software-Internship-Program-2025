# Converts Celsius to Fahrenheit
def c_to_f(c):
    return (c * 9/5) + 32  # Formula: F = C × 9/5 + 32

# Converts Celsius to Kelvin
def c_to_k(c):
    return c + 273.15  # Formula: K = C + 273.15

# Main program
celsius = float(input("Enter temperature in Celsius: "))
print("Fahrenheit:", c_to_f(celsius))
print("Kelvin:", c_to_k(celsius))
