def is_balanced(text :str):
    stack = []
    openings = list('{[(')
    closings = list('}])')

    dct = dict(zip(openings, closings))

    for char in list(text):

        if char in openings:
            stack.append(char)

        if char in closings:
            closing = char
            opening = stack.pop()

            if not dct[opening] == closing:
                return False

    return True if len(stack) == 0 else False


assert is_balanced('a(bcd)d') == True, "should return true for %r" % 'a(bcd)d'
assert is_balanced('(kjds(hfkj)sdhf') == False, "should return false for %r" % '(kjds(hfkj)sdhf'
assert is_balanced('(sfdsf)(fsfsf') == False, "should return false for %r" % '(sfdsf)(fsfsf'
assert is_balanced('{[]}() ') == True, "should return true for %r" % '{[]}() '


def twoSum(nums, target):
    cache = {}
    
    for i, n in enumerate(nums):
        cache[n] = i
        
        if target - n in cache:
            return [cache[target - n], i]

    return []

print(twoSum([1,2,7,4,5,66,7,8], 9))

def addTwoNumbers(l1, l2):

    n1 = 0
    n2 = 0
    
    for i, n in enumerate(l1):
        n1 = n1 + n * 10**i
        
    for i, n in enumerate(l2):
        n2 = n2 + n * 10**i
        
    print(n1)
    print(n2)
