# Not a good practice because current implementation waste memory.
import timeit
def get_missing_number_in_array(array, array_size):
    l = len(array)
    lost_number = []
    while l != array_size:
        #check before
        if array[0] != "1":
            array.insert(0, "1")
            lost_number.append("1")
            l += 1
        # check middle
        for i, arr in enumerate(array):
            if i != len(array)-1:
                if (int(array[i]) + 1) != int(array[i+1]):
                    array.insert(i+1, str(int(array[i]) + 1))
                    lost_number.append(int(array[i]) + 1)
                    l += 1
                else:
                    continue
            else:
                continue
        # check final
        if len(array) != array_size:
            lost_number.append(str(int(array[len(array)-1]) + 1))
            array.append(int(array[len(array)-1]) + 1)
            l += 1
    return lost_number

if __name__ == "__main__":
    test_cases = "1"
    for _ in range(int(test_cases)):
        s = timeit.timeit()
        array_size = int("42") # 1 2 3 4 5 6 7 8 9
        array = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 \
        24 25 26 27 28 29 31 32 33 34 35 36 37 38 39 40 41 42".split()
        lost_number = get_missing_number_in_array(array, array_size)
        e = timeit.timeit()-s
        print("{}".format(e))
        print(" ".join(list(map(str, lost_number))))
