def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    b=0
    while a<len(s):
        if s[a].isdigit():
            b+=1
        a+=1
    return b-(s.count("0")+s.count('2')+s.count('4')+s.count('6')+s.count('8'))
print(main("1234567890"))
