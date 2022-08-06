import sys
import cowsay

print(len(sys.argv))
print(sys.argv)

if len(sys.argv) == 2:
    print(f"Now I am going to duplicate {sys.argv}")
    cowsay.cow("hi,"+ sys.argv[1])
    sys.exit("Few args")
elif len(sys.argv) ==3:
    print(sys.argv)
    cowsay.trex("hi " + sys.argv[2])

    

