def main():
    elements = [5,1,2,6,7,3,1]
    print(f'unsorted={elements}')
    result = merge_sort(elements)
    print(f'sorted={result}')


def merge_test():
    l = [3,6,8]
    r = [2,3,9]
    print(f'given left={l} and right={r}')
    m = merge(l, r)
    print(f'merged={m}')


def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        result = merge(left,right)
        return result
    return data


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1
    return result


if __name__ == "__main__":
    main()
