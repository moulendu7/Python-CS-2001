def list_summary(numbers):
    total = 0
    for n in numbers:
        total += n
    avg = total / len(numbers)
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return total, avg, max_val

print(list_summary([5, 12, 7, 20, 3]))