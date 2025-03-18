def extract_numbers(text):
    numbers = []
    current_number = ''
    for char in text:
        if char.isdigit():
            current_number += char
        else:
            if current_number != '':
                numbers.append(int(current_number))
                current_number = ''
    if current_number != '':
        numbers.append(int(current_number))
    return numbers




print(extract_numbers("104 soldiers, 50 horses and 3 catapults!"))
print(extract_numbers("the 7 kingdoms and the 5 stark brothers"))
print(extract_numbers("zz23yy42tt678pp81"))