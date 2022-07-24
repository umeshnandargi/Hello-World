def numbers():
    list = []
    while True:
        a = input("Enter nos. or type quit to stop: ")
        if a.lower() == 'quit':
            break
        else:
            try:
                list.append(int(a))
            except:
                print("enter valid input")

    return list


def minimum(num_list):
    m = num_list[0]
    for number in num_list:
        try:
            if number <= m:
                m = number
                return m
        except:
            break


def maximum(num_list):
    m = num_list[0]
    for number in num_list:
        try:
            if number >= m:
                m = number
                return m
        except:
            break

# y = numbers()
# print("minimum number is: ", minimum(y))
# print(f'maximum number is {maximum(y)}')
