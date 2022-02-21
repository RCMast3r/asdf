from curtsies import Input

def main():
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            print(repr(e))
            print(type(e))
            b=bytes(e,'utf-8')
            print(b)
if __name__ == '__main__':
    main()