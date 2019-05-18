def bubble_sort(l):
    for num in range(len(l) - 1, 0, -1):
        for i in range(num):
            if l[i] > l[i + 1]:
                temp = l[i]
                l[i] = l[i + 1]
                l[i + 1] = temp


my_list = [14, 46, 43, 27, 57, 41, 45, 21, 70]
bubble_sort(my_list)
print(my_list)
