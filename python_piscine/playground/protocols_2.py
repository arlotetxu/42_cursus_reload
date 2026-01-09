from typing import Protocol, runtime_checkable

@runtime_checkable
class Uno(Protocol):

    def printing(self):
        print("Impresion desde la clase Uno")


class Dos:

    def printing(self):
        print("Impresion desde la clase Dos")

    def sum(num1, num2):
        return num2 + num1

example = Dos()
example.printing()
# example.sum(12, 2)

assert isinstance(example, Uno) #No genera salida por lo que es True
