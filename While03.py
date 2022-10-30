def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Return
        int: return answer
    """
    a=0 
    b=0
    x=0
    y=0
    while a<len(s):
        if s[a].isalpha():
            b+=1
        a+=1
        if s[x].isdigit():
            y+=1
        x+=1
    return len(s)-(y+b)
print(main("123s67+_fgyug/*-+"))
