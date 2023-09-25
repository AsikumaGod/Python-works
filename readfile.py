def myfunc(a):
    if a == True:
        return 'Inside'
    elif a == False:
        return 'Outside'
    myfunc(True)
