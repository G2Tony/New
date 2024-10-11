
def pincode(a):
    if (len(a) == 4 or len(a) == 6) and a.isdigit():
        return True
    else:
        return False


pin = input()
print(pincode(pin))