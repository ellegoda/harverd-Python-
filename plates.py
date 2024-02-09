
import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if len(plate)>= 2 and len(plate)<=6:
         if plate[0:2].isalpha():
            pattern = re.compile(r'[. ,;:"\'!?(){}[\]<>]')

            if bool(pattern.search(plate))== True:
                return False
            else:
                foundDigit = False
                i = 0
                for s in plate:
                    if s.isdigit():
                        i+=1
                        if s == "0" and i == 1:
                            return False

                        foundDigit = True
                    else:
                        if foundDigit:
                            return False

                return True
         else:
             False
    else:
        return False

main()
