def addition(n1=0, n2=0):
    return n1 + n2


def subtraction(n1=0, n2=0):
    return n1 - n2

def multiplication(n1=0, n2=0):
    return n1 * n2

def division(n1=0, n2=0):
    return n1 / n2



if __name__ == "__main__":
    output = addition(1, 10)    
    print(f"Output {output}")
    
    print(f"Subtraction : {subtraction(10,5)}")
