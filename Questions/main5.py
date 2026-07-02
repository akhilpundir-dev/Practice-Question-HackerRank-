def swap_case(s):
    string=""
    for i in s:
        if 65<= ord(i) <= 90:
            string+=i.lower()
        elif 97<= ord(i) <=122:
            string+=i.upper()
        else:
            string+=i
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)