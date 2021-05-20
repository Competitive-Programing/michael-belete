def main():
    print(sum(3,4))
def sum(a,b):
    while b != 0:
        c = a & b
        a = a ^ b #least number

        b = c << 1
    return a

main()