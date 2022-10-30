def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    a=0
    b=0
    while a<len(s):
        if s[a].isalpha():
            b+=1
        a+=1
    return b-(s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u'))
print(main("Codeschooluz"))
