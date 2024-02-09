import re

def detect_phone_numbers(text):
    phone_pattern = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
    phone_numbers = phone_pattern.findall(text)
    return phone_numbers

text = "Here are some phone numbers: (123) 456-7890, 123 456 7890, 123-456-7890, 123.456.7890, 123456789012"
phone_numbers = detect_phone_numbers(text)
print(phone_numbers)
