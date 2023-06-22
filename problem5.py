def find_smallest_multiple():
    multiple = 1

    for i in range(1, 10):
        if multiple % i != 0:
            j = 2
            while (j) <= 10:
                if (multiple * j) % i == 0:
                    multiple *= j
                    break
                print(multiple)
                j += 1

    return multiple

result = find_smallest_multiple()
print( result)
