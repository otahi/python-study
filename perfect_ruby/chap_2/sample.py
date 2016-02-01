#!/usr/bin/env python
def main():
    """
    sample main funcion
    """

    for i in range(1, 6):
        if i % 2 == 0:
            print("%s is even" % i)
        else:
            print("%s is odd" % i)

            
if __name__ == "__main__":
    """
    judge if run on command line or not
    """
    main()
