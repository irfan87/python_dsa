def basic_binary_search(list, item):
    lowestNumber = 0
    highNumber = len(list) - 1

    while lowestNumber <= highNumber:
        midNumber = lowestNumber + highNumber

        guessNumber = list[midNumber]

        if guessNumber < item:
            lowestNumber = midNumber + 1
        if guessNumber > item:
            highNumber = midNumber - 1
        else:
            return midNumber

    return None


listItem = [1, 2, 3, 4, 5]

print(basic_binary_search(listItem, 2))
print(basic_binary_search(listItem, -1))
