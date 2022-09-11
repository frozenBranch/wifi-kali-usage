FILENAME = 'fibertel_dict.txt'
m = 1000000

def main():
    """
    This execution may use around 500mb RAM
    Final file size is around 1.2gb

    Syntax supported on python>2.7 and python3
    """
    with open(FILENAME, 'a') as f:
        for x in range(20*m, 35*m):
            f.write("004"+str(x)+"\n014"+str(x)+"\n")
        for x in range(35*m, 45*m):
            f.write("004"+str(x)+"\n014"+str(x)+"\n")
        for x in range(10*m, 20*m):
            f.write("004"+str(x)+"\n014"+str(x)+"\n")
        for x in range(5*m, 10*m):
            f.write("004"+str(x)+"\n014"+str(x)+"\n")
        for x in range(45*m, 50*m):
            f.write("004"+str(x)+"\n014"+str(x)+"\n")
        for x in range(500000, 5*m):
            f.write("004"+str(x)+"\n014"+str(x)+"\n")

if  __name__ == '__main__':
    main()
