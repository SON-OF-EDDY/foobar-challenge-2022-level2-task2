def solution(input_array):

    from operator import itemgetter

    split_version_numbers = []
    original_split_version_numbers = []

    for version_number in input_array:
        split_version_numbers.append(version_number.split('.'))

    for version_number in input_array:
        original_split_version_numbers.append(version_number.split('.'))

    for i in range(len(split_version_numbers)):
        split_version_numbers[i] = list(map(lambda x:int(x),split_version_numbers[i]))

    for i in range(len(original_split_version_numbers)):
        original_split_version_numbers[i] = list(map(lambda x:int(x),original_split_version_numbers[i]))

    for i in range(len(split_version_numbers)):

        if len(split_version_numbers[i]) == 2:
            split_version_numbers[i].append(0)
        elif len(split_version_numbers[i]) == 1:
            split_version_numbers[i].append(0)
            split_version_numbers[i].append(0)

    mega_array = []

    for i in range(len(split_version_numbers)):
        mega_array.append([i,split_version_numbers[i][0],split_version_numbers[i][1],split_version_numbers[i][2],len(original_split_version_numbers[i])])


    result = sorted(mega_array,key=itemgetter(1,2,3,4))

    needed_order = []

    for element in result:
        needed_order.append(element[0])

    filtered_input_array = []

    for index in needed_order:
        filtered_input_array.append(input_array[index])

    return filtered_input_array