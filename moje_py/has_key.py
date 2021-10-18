def has_key(dictionary, key):

    if key in dictionary:
        x = True
    else:
        x = False
    return(print(x))

dictionary = dict(ala = 'kot', jola = 'pies', ciocia = 'papuga')
has_key(dictionary,'ala')