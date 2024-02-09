def extract_digits(s):
    return ''.join(filter(str.isdigit, s))

def is_valid_phone_number(s):
    digits = extract_digits(s)
    return len(digits) >= 10

def find_phone_numbers(text):
    numbers = []
    current_number = ""
    for char in text:
        if char.isdigit() or char in ['+', '-', '(', ')', ' ']:
            current_number += char
        else:
            if is_valid_phone_number(current_number):
                numbers.append(current_number)
            current_number = ""
    if is_valid_phone_number(current_number):
        numbers.append(current_number)
    return numbers

# Example usage:
text = "You can call me at +1 (555) 123-4567 or 555-9876. My other number is 1234567890."
phone_numbers = find_phone_numbers(text)
print("Phone numbers found:", phone_numbers)






(?:\+?\d[- (]*\d[- )]*\d[- )]*(?:\d[- )]*){10}

import re

def detect_phone_numbers(text):
    phone_pattern = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
    phone_numbers = phone_pattern.findall(text)
    return phone_numbers

text = "Here are some phone numbers: (123) 456-7890, 123 456 7890, 123-456-7890, 123.456.7890, 123456789012"
phone_numbers = detect_phone_numbers(text)
print(phone_numbers)
