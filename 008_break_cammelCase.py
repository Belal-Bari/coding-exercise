# Complete the solution so that the function will break up camel casing, using a space between words.

def solution(s):
    res = [(' ' + l) if l.isupper() else l for l in s[:]]
    return ''.join(res)

print(solution('cammelCaseString'))