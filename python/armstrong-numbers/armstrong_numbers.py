def is_armstrong_number(number):
    str_number = str(number)
    number_length = len(str_number)
    sum = 0
    
    for digit in str_number:
        sum += int(digit) ** number_length
    return sum == number
    
