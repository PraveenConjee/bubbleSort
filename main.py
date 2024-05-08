def main(list):
    isItSorted = False
    while not isItSorted:
        isItSorted = True
        for i in range(len(list) - 1):
            tmp = list[i]
            if tmp > list[i + 1]:
                list[i] = list[i + 1]
                list[i + 1] = tmp
                isItSorted = False

    print(list)
    return list


list = [11, 2, 4, 1343, 134, 1, 34, 134, 21, 4, 14, 13, 41, 34]
main(list)
