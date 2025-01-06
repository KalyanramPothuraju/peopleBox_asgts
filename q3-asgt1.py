
def multiply_and_add_to_b(a, b):
    # Multiply a and b, then add b to the result
    product = a * b
    sum_with_b = product + b
    return sum_with_b

def calculate_sum_and_multiplication_result(a, b):
    # Calculate the sum of a and b
    sum_of_a_and_b = a + b
    
    # Call the function to multiply a and b, then add b to the result
    multiplication_result = multiply_and_add_to_b(a, b)
    
    # Return both the sum and the calculated result
    return sum_of_a_and_b, multiplication_result
