# python3


def build_heap(n,data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(n-1,0,-1):
        ch=i
        par=(i-1)//2
        # print(i,par)
        while True:
            # print(data[ch],data[par],"-")
            if par>=0 and data[ch]<data[par]:
                data[ch],data[par]=data[par],data[ch]
                swaps.append([par,ch])
            else: break
            ch=par
            par=(ch-1)//2
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    i = input()
    if "i" in i.lower():
        n=int(input())
        data = list(map(int, input().split()))
    elif 'f' in i.lower(): 
        name=input()
        if 'a' not in name:
            with open("./tests/"+name, mode='r',encoding="utf8") as fail:
                n=int(fail.readline())
                s=fail.readline()
                data = list(map(int, s.split()))
    else: 
        print("Wrong format")
        return
    
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    swaps = build_heap(n,data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
