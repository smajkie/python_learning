def card_hide(card):
    x = str(card)
    dig = (len(x)-4)*'#'+x[len(x)-4:len(x)]
    return dig
print(card_hide(12341299))