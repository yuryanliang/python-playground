def main():
    a=1
    try:
        some()
    except(KeyError):
        raise KeyError("main")
    except(Exception):
        raise Exception
    # some()


def some():
    b=2
    try:
        if b==2:
            raise KeyError
    except KeyError:
        raise KeyError("some")


if __name__=="__main__":
    main()