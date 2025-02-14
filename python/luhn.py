# luhn algorithm
# Computes the checkdigit of a string if digits
# Used to validate swedish SSN and credit card numbers

# 1. Drop last digit, its the check digit
# 2. Reverse the payload
# 3. Double every second digit in the payload left to right, if result > 9 substract 9
# 4. Sum all results including the once not doubled
# 5. Calculate check digit from sum, check digit = (10 - (sum mod 10)) mod 10
# 6. Verify against check digit from droppped last digit

def luhn_algorithm(digits: str):
    def calculate_sum(payload: str, sum=0, multiplier=2):
        if len(payload) == 0: return sum

        head = int(payload[:1])
        tail = payload[1:]

        result = head * multiplier
        if result > 9: result -= 9

        return calculate_sum(payload=tail, sum=sum+result, multiplier=2 if multiplier == 1 else 1)

    checkdigit = int(digits[-1])
    payload = digits[:-1][::-1] # drop last, reverse

    sum = calculate_sum(payload)
    newcheckdigit = (10 - (sum % 10)) % 10

    if checkdigit == newcheckdigit:
        print('valid payload')
    else:
        print('invalid payload')


luhn_algorithm('17893729974')

