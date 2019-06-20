#code
#Seriously, I ran out of ideas for reducing the TLE here. 
import timeit
def getLeader(array, array_size):
    integer = []
    for i in range(array_size):
        target = array[i]
        remain = sorted(map(int, array[i+1:]))
        if remain :
            if int(target) >= int(remain[-1]):
                integer.append(target)
    integer.append(array[-1])
        
        #boo = list(filter(lambda x: int(target) > int(x), remain))
        #if len(boo) == len(remain):
        #    integer.append(array[i])
    return integer

if __name__ == "__main__":
    test_cases = int("1")
    for _ in range(test_cases):
        array_size = int("6")
        s = timeit.timeit()
        array = "16 17 4 3 5 2".split()
        integer_leader = getLeader(array,array_size)
        e = timeit.timeit() - s
        #print(e)
        print(" ".join(integer_leader))
        
        