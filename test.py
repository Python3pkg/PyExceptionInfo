import PyExceptionInfo

def makeException():
    print("Trying to create an exception")
    try:
        # The first line causes NameError, second line ZeroDivision
        happy()
        print((8 / 0))
    except Exception as e:
        PyExceptionInfo.getInfo(e)

if __name__ == '__main__':
    makeException()
