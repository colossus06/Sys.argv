import sys



try:
    print("Hi, my name is", sys.argv[1])
except IndexError:
    print("Feed me a more value")
    