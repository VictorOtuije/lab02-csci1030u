# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


def seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    leftover = total_seconds % 3600
    minutes = leftover // 60
    seconds = leftover %60
    return f"{hours}:{minutes:02d}:{seconds:02d}"

    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"
    pass


def admission_price(age):
    if age <5:
        return 0.0
    elif age <=12:
        return 8.00
    elif age <=64:
        return 15.00
    else:
        return 10.00


    # TODO (Part 2): return the ticket price (a number) for someone of this age
    pass


def sum_multiples(limit):
    total = 0
    for n in range(limit):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    return total


    # TODO (Part 3): return the sum of every whole number below `limit`
    #   that is a multiple of 3 or of 5
    pass


def total_of_positives(numbers):
    total = 0
    for x in numbers:
        if x >0:
            total += x
    return total

    # TODO (Part 4 - STRETCH, optional): return the sum of just the
    #   positive numbers in the list `numbers`
    pass


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    # print(seconds_to_hms(3661))            # 1:01:01
    # print(admission_price(10))             # 8
    # print(sum_multiples(10))               # 23
    # print(total_of_positives([1, -2, 3]))  # 4
    pass


if __name__ == "__main__":
    main()
