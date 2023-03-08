import math


def floatInput(prompt, min=-math.inf, max=math.inf):
    while True:
        try:
            val=float(input(prompt))
            if min<= val <=max:
                break
            else:
                print("o valor nao se encontra no intervalo entre", min," e ", max,"." )
        except:
            print("Não é um valor")
    return val


print(floatInput("Numero: ", 1))







def main():
    print("a) Try entering invalid values such as 1/2 or 3,1416.")
    v = floatInput("Value? ")
    print("v:", v)

    print("b) Try entering invalid values such as 15%, 110 or -1.")
    h = floatInput("Humidity (%)? ", 0, 100)
    print("h:", h)

    print("c) Try entering invalid values such as 23C or -274.")
    t = floatInput("Temperature (Celsius)? ", min=-273.15)
    print("t:", t)

    # d) What happens if you uncomment this?
    # impossible = floatInput("Value in [3, 0]? ", min=3, max=0)

    return

if __name__ == "__main__":
    floatInput()
    main()
    
4