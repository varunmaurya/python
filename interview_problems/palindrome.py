#Check if given string is palindrome, Take only alphabets and numbers in consideration, Ignore special character

def check_palindrome(string):
    return string == string[::-1]

def check_palindrome2(string):
    str_len = len(string)
    for i in range(0,str_len//2):
        if string[i] != string[(str_len-1)-i]:
            return False
    return True

if __name__ == '__main__':
    print(check_palindrome('madam'))
    print(check_palindrome2('madam'))

