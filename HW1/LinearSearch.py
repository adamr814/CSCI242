array = [1, 2, 4, 8, 16, 32, 64, 128, 256]
i = 0
x = 64
while(i <= len(array)):
    if array[i] == x:
        print("Value Was Found")
        print("Checked Value:\n", array[i])
        break
    else:
        print("Value Was Not Found")
        print("Checked Value:\n", array[i])
    i += 1
