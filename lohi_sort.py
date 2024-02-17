def main():
    print(f'low hi recursive sort???')
    elements = [3,4,1,6,5,2]
    print(f'before sort {elements}')
    print(f'after sort {sort(elements)}')
    

def sort(elements):
    if len(elements) <= 1:
        return elements
    
    median = len(elements) // 2
    left = []
    right = []
    for i in range(len(elements)):
        if i != median:
            if elements[i] <= elements[median]:
                left.append(elements[i])
            else:
                right.append(elements[i])

    sorted = sort(left) + [elements[median]] + sort(right)
    return sorted


if __name__ == '__main__':
    main()

