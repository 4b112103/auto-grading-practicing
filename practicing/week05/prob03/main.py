def main(R,C):
    num = 1
    matrix = [[0] * C for _ in range(R)]

    for i in range(C):
        for j in range(R):
            matrix[j][i] = num
            num+=1 

    return matrix

def print_m(matrix):
    for i in matrix:
        for num in i:
            print(num,end=" ")
        print()

if __name__=="__main__":
    R, C =map(int, input().split())
    print_m(main(R,C))