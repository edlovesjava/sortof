def main():
    global write_count
    global read_count
    print ("Insert Sort")
    elements = [5, 9, 2, 1, 67, 34, 88, 34]
    print(elements)
    print(insert_sort(elements))
    print("Write Count:", write_count)
    print("Read Count:", read_count)
    write_count = 0
    read_count = 0
    print ("Insert Sort 1")
    elements = [5, 9, 2, 1, 67, 34, 88, 34]
    print(elements)
    print(insert_sort1(elements))
    print("Write Count:", write_count)
    print("Read Count:", read_count)


def insert_sort(elements):
    global write_count
    global read_count
    # look at each position in the list
    # compare with elements to the right and if one is smaller, insert it at the position

    for i in range(0, len(elements)):
        for j in range (i+1, len(elements)):
            read_count += 1
            if elements[i] > elements[j]:
                # make space for the element by shifting the elements
                temp = elements[j]
                for k in range(j, i, -1):
                    write_count += 1
                    elements[k] = elements[k-1]
                elements[i] = temp
    return elements


def insert_sort1(elements):
    global write_count
    global read_count
    # look at each position in the list
    # find smallest element to the right and if it is smaller, insert it at the position

    for i in range(0, len(elements)):
        smallest = i
        for j in range (i+1, len(elements)):
            read_count += 1
            if elements[smallest] > elements[j]:
                smallest = j
        read_count += 1
        if elements[i] > elements[smallest]:
            # make space for the element by shifting the elements
            temp = elements[smallest]
            for k in range(smallest, i, -1):
                write_count += 1
                elements[k] = elements[k-1]
            elements[i] = temp
    return elements


if __name__ == "__main__":
    write_count = 0
    read_count = 0
    main()