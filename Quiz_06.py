def resident_number(number):
    number = number.replace('-', '')

    if len(number) != 13:
        return False

    front_12_digits = number[:12]

    coefficients = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    total = sum(int(front_12_digits[i]) * coefficients[i] for i in range(12))
    remainder = total % 11
    subtracted_value = 11 - remainder

    last_digit = int(number[-1])

    if subtracted_value == last_digit:
        return True
    else:
        return False

number = input("주민등록번호를 입력하세요 (예: 000000-0000000): ")

if resident_number(number):
    print("주민등록번호가 유효합니다.")
else:
    print("주민등록번호가 유효하지 않습니다.")

