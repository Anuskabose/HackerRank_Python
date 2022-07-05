if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    print(list([i,j,k] for i in range(a+1) for j in range(b+1) for k in range(c+1)  if i+j+k !=d))
    
    
    
    OUTPUT
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
