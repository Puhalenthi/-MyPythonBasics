def getRectangle():
    bigx = 0
    bigy = 0
    x = 0
    y = 0
    lst = [(float(input('Enter x value:   ')), float(input('Enter y value:  '))) for i in range(5)]
    for i in lst:
        x += i[0]
        y += i[1]

        if bigx < i[0]:
            bigx = i[0]
        if bigy < i[0]:
            bigy = i[1]
    
    x /= 5
    y /= 5
    width = 2 * (bigx - x)
    height = 2 * (bigy - y)

    return 'The bounding rectangle\'s center ({}, {}), width {}, height {}'.format(x, y, width, height)


print(getRectangle())