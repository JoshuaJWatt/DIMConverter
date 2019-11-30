while True:
    print('What is your DIM reading?')
    dimreading = input(':' )
    dimlen = len(dimreading)
    outputval = 0

    for i in range(dimlen):
        # Take the value of the first digit
        digitval = int(dimreading[0])
        # If it's a 1 we do maths
        if digitval == 1:
            decimalval = 2**i
            outputval += decimalval
        dimreading = dimreading[1:]

    print('The DIM value is %i' % outputval)

    # Take first digit of string, do 2^ of it, add it to a value. Loop for length of string and final value will be our result