def main():
    print('selection sort')
    elements = [3,4,1,7,8,6]
    print(f'unsorted {elements}')
    print(f'sorted {selection_sort(elements)}')


def selection_sort(elements):
    # for all positions in elements -1
    #    find smallest value to the right of the current position
    #    if smaller than current value, swap
    
    for i in range(len(elements)):
        smallest = i
        for j in range(i + 1, len(elements)):
            if elements[i] > elements[j]:
                smallest = j
        if smallest != i:
            # swap i with smallest
            temp = elements[i]
            elements[i] = elements[smallest]
            elements[smallest] = temp    
    return elements


if __name__ == '__main__':
    main()

