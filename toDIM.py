print('how long is your DIM?')
dimsize = int(input(': '))

while True:
    print('What value would you like to input into your DIM?')
    inputval = int(input(':' ))
    diminput = [] # This will read backwards

    newval = inputval
    newsize = dimsize
    for i in range(dimsize):
        # print('newsize = ', newsize, '& newval = ', newval)
        # print((((newval) - (2**(newsize - 1)))))
        if (((newval) - (2**(newsize - 1))) >= 0):
            newval = (newval) - (2**(newsize - 1))
            # print('newval = ', newval)
            diminput.append(1)
        else:
            diminput.append(0)
        
        # print(diminput)
        newsize -= 1

    if newsize == 0 and newval > 0:
        print('Sorry, that number is too large for a DIM of this size')
    else:  
        diminput.reverse()
        print('Your DIM input should be: ')
        print(diminput) # This currently prints HSB to LSB


