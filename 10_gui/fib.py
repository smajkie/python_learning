def fibonacci():                            
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b                # przesuwa sie w prawo ladnie tylko yieldujac jeden element


