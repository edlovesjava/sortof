def main():
    print ("Hello World")
    elements = [5, 9, 2, 1, 5, 6, 7, 8, 9, 10]
    print ("Bubble Sort")
    print (elements)
    bubble_sort(elements)
    print (elements)


# continue going through a list until no more swaps are made
def bubble_sort(elements):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(elements) - 1):
            if elements[i] > elements[i + 1]:
                not_sorted = True
                # swap
                next_element = elements[i + 1]
                elements[i + 1] = elements[i]
                elements[i] = next_element


if __name__ == "__main__":
    main()