

def appendWithOrder(sortedList: list, el):
    l, r = 0, len(sortedList) - 1
    while l <= r:
        m = (l + r) // 2
        