def check_number(num):
    if num > 10 and num < 20:
        return "Between 10 and 20"
    elif num == 10 or num == 20:
        return "Exactly 10 or 20"
    else:
        return "Outside range"

print(check_number(15))  # Between 10 and 20
print(check_number(10))  # Exactly 10 or 20
print(check_number(5))   # Outside range
