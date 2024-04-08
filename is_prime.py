import unittest

def is_prime(value):
    if value <= 1:
        return False 
    elif value <= 3:
        return True
    elif value % 2 == 0 or value % 3 == 0:
        return False
    else:
        divisor = 5
        while divisor * divisor <= value:
            if value % divisor == 0 or value % (divisor + 2) == 0:
                return False
            divisor += 6
        return True
            

if __name__ == "__main__":
    unittest.main()