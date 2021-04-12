def paul(x):
    for i in range(len(x)):
        if x[i] == 'kata':
            x[i] = 5
        elif x[i] == 'Petes kata':
            x[i] = 10
        elif x[i] == 'life':
            x[i] = 0
        elif x[i] == 'eating':
            x[i] = 1
    if sum(x) in range(40):
        return 'Super happy!'
    elif sum(x) in range(40, 70):
        return 'Happy!'
    elif sum(x) in range(70, 100):
        return 'Sad!'
    else:
        return 'Miserable!'