from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

class AbstractClass(ABC):

    @abstractmethod
    def print_message(message: str):
        print(message)


class AbstractClassSon(AbstractClass):

    def print_message(self, message: str):
        print(f"{message}")

# ===========================================================================

@runtime_checkable
class ProtocolBaseClass(Protocol):

    def print_message(self, message: str):
        ...


class MyClass():
    def print_message(self, message: str):
        print(message)

    def addition(self, num1: int, num2: int) -> int:
        return num1 + num2


abstract_o = AbstractClassSon()
abstract_o.print_message(message="Testing abstract class inheritance")
is_AbstractClassSon = isinstance(abstract_o, AbstractClassSon)
print(f"Is abstract_o an AbstractClassSon class: {is_AbstractClassSon}")
is_AbstractClass = isinstance(abstract_o, AbstractClass)
print(f"Is abstract_o an AbstractClass class: {is_AbstractClass}")


protocol_o = MyClass()
protocol_o.print_message("Testing protocol class")
is_my_class = isinstance(protocol_o, MyClass)
print(f"Is protocol_o an MyClass class: {is_my_class}")
is_protocolbaseclass = isinstance(protocol_o, ProtocolBaseClass)
print(f"Is protocol_o a ProtocolBaseClass class: {is_protocolbaseclass}")


'''
Concepto clave: "Duck Typing"
"Si camina como un pato y hace cuac como un pato, entonces es un pato."

En Python:

"Si tiene los métodos que define el Protocol, entonces cumple el Protocol."
'''
