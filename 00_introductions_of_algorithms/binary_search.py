# will be search from top to bottom / right to left
def search_iterative(list, item):
    low = 0
    high = len(list) - 1

    # narrowed it down to one element
    while low <= high:
        # check the middle element
        mid = low + high
        guess = list[mid]

        # print(f"before if: {list[mid]}")
        if guess < item:
            # if the guess is too low
            low = mid + 1
        else:
            # if the guess is too high
            high = mid - 1
        # found the item
        if guess == item:
            return mid

        # print(f"after if: {list[mid]}\n")
    return None


# will be search from bottom to top / left to right
def search_recursive(list, high, low, item):
    if high >= low:
        mid = low + high // 2
        guess = list[mid]

        # if element is present at the middle itself
        if guess == item:
            return mid

        # if element is smaller than mid, then it can only be present in left subarray
        elif guess > item:
            return search_recursive(list, low, mid - 1, item)

        # else the element can only be present in right subarray
        else:
            return search_recursive(list, mid + 1, high, item)

    else:
        # element is not present in the array
        return None


mylist = [1, 2, 3, 4, 5, 6]

print(search_iterative(mylist, 2))
print(search_iterative(mylist, -1))
