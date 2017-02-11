def bubble(number_list):
    count = 0
    swap = True

    while swap:
        swap = False
        for element in range(len(number_list)-1):
            count += 1
            if number_list[element] > number_list[element + 1]:
                swap = True
                tmp = number_list[element]
                tmp1 = number_list[element + 1]
                number_list[element] = tmp1
                number_list[element + 1] = tmp
    print("Comparisons: %d" % count)
    return number_list


def linear(item_to_find, search_list):
    found = False

    for position in range(0, len(search_list)):
        if search_list[position] == item_to_find:
            found = True
            break
        elif position == len(search_list):
            answer = input("Would you like to add the word? (Y/N) ").lower()
            if answer == "y":
                search_list.append(item_to_find)
            else:
                break
        else:
            continue
    return found, search_list


def binary(item_to_find, number_list):
    found = False
    bottom = 0
    top = len(number_list) - 1

    while bottom <= top and not found:
        middle = (bottom + top) // 2
        if number_list[middle] == item_to_find:
            found = True
        elif number_list[middle] < item_to_find:
            bottom = middle + 1
        else:
            top = middle - 1
    return found

""" Not done yet
def quicksort(my_list, start, end):

    def partition():
            pass
"""

if __name__ == '__main__':
    print("bubble sort")
    print(bubble([10, 98, 11, 7, 26, 76]), end="\n\n")
    print("linear sort")
    print(linear("pie", ["apple", "banana", "carrot", "dogmatism", "epitaph", "frugal", "pie", "ganymede",
                         "hammer", "ingenious"]), end="\n\n")
