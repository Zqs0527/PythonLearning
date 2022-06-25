cheese = 'cheddar' # this is a global variable

def make_omelete():
    # if one wants to change the value of the global within a function
    # global modifier should be used to tell python to change the value of
    # global variabl
    global cheese
    cheese = 'swiss'
    omelette = 'a tasty {} omellete'.format(cheese)
    return omelette