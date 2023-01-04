def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if n>= len(s):
        ans = False
    else: 
        ans = s[n]
    return ans 

