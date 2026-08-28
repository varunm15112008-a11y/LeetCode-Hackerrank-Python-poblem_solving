if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    new=()
    for i in integer_list:
        new1=(i,)
        new=new+new1
    print(hash(new))
