'''
If all the char are present in 2 string , no matter in what order, they are called anagram
We have to determine how many char need to be removed to make 2 strings anagram
'''

def is_anagram(s1,s2):

    rem=0
    s2_dict = {}
    s1_dict = {}

    for c in s2:
        if c in s2_dict:
            s2_dict[c]+=1
        else:
            s2_dict[c]=1

    for ch in s1:
        if ch in s1_dict:
            s1_dict[ch]+=1
        else:
            s1_dict[ch] = 1

    key1 = set(s1_dict.keys())
    key2 = set(s2_dict.keys())

    remove_keys1 = key1-key2
    remove_keys2 = key2-key1

    common_keys = key1.intersection(key2)

    for k in common_keys:
        if s1_dict[k] != s2_dict[k]:
            rem=rem+ abs(s1_dict[k] - s2_dict[k])

    for k in remove_keys1:
        rem = rem + s1_dict[k]

    for k in remove_keys2:
        rem = rem + s2_dict[k]

    print(rem)


if __name__ == '__main__':
    is_anagram('xxyypzz','xxyrz')


