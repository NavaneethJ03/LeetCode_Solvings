if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    b1 = set(arr)
    b2 =sorted(list(b1),reverse =True)
    print(b2[1])
    
