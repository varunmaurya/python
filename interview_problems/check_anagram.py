def is_anagram(s1,s2):
    if len(s1) != len(s2):
        print('Not Anagram')
        return

    s1_dict={}
    for c in s1:
        if c in s1_dict:
            s1_dict[c] = s1_dict[c]+1
        else:
            s1_dict[c] = 1

    s2_dict = {}
    for c in s2:
        if c in s2_dict:
            s2_dict[c] = s2_dict[c]+1
        else:
            s2_dict[c] = 1

    for i in s1_dict:
        if s1_dict[i]!=s2_dict[i]:
            return False

    return True

if __name__ == '__main__':
    print(is_anagram('asdfe','dsdfa'))