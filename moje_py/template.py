import platform

def main():
    message()

def message():
    print(f'This platform runs {platform.processor()} system with release  on processor ')

#if __name__ == '__main__': main()