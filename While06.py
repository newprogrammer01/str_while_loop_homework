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
        if s[a].isalpha() and s[a]!=a and s[a]!=e and s[a]!=i and s[a]!=o and s[a]!=u:
            b+=1
        a+=1
    return b
print(main("CodeschoolUz"))
