def merge_sort(lst):
    # Initialise
    result = []

    if len(lst) < 2:
        return lst
    mid = int(len(lst) / 2)

    # Recursion
    y = merge_sort(lst[:mid]) # First half
    z = merge_sort(lst[mid:]) # Second half

    # Initialise
    a = 0
    b = 0
    while a < len(y) and b < len(z):
        if y[a] > z[b]:
            result.append(z[b])
            b += 1
        else:
            result.append(y[a])
            a += 1

    result += y[a:]
    result += z[b:]

    return result

if __name__ == '__main__':
