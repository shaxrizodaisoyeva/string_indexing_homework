def main(s):
    """
    A string variable consisting of several characters is given. Add and return the first and last character.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    a = len(s)
    b = s[0]+s[a-1]
    return b 
