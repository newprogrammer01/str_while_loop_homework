def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
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
    return b -(s.count('1')+s.count('3')+s.count('5')+s.count('7')+s.count('9'))
print(main("1515"))