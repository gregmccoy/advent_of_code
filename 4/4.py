INPUT = "183564-657474"


def count_passwords(low, high):
    """
    Find the amount of unqiue values within certain parameters

    Args:
        low (int): Lowest value to check
        high (int): Highest value to check
    """
    count = 0
    all_passwords = [str(i) for i in range(int(low), int(high))]
    valid_passwords = []
    for password in all_passwords:
        valid = True
        previous_low = 0

        # Password is 6 characters
        if len(password) != 6:
            valid = False

        # Password must have a duplicate value
        if len(set(password)) == len(password):
            valid = False

        # Password always increments left to right
        for number in password:
            if int(previous_low) <= int(number):
                previous_low = number
            else:
                valid = False

        if valid:
            # Password has a 2 digit duplicate
            for i in range(len(password) - 1):
                valid = False
                if (password[i] == password[i+1]) and \
                        (i == 4 or password[i] != password[i+2]) and \
                        (password[i] != password[i-1]):
                    valid = True
                    break
        if valid:
            count += 1
            valid_passwords.append(password)
    return count


low, high = INPUT.split("-")
print(count_passwords(low, high))
