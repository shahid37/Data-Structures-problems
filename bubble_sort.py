def bubble_sort(n_list):
    for num in range(len(n_list) - 1, 0, -1):
        for i in range(num):
            if n_list[i] > n_list[i + 1]:
                temp = n_list[i]
                n_list[i] = n_list[i + 1]
                n_list[i + 1] = temp


n_list = [14, 46, 43, 27, 57, 41, 45, 21, 70]
bubble_sort(n_list)
print(n_list)
