# El código en este archivo implementa una lista doblemente encadenada
import typing

# Nota: typing es una librería que nos permite especificar mas sugerencias de tipos
# sobre nuestro código, aquí usamos 'typing.Any' como tipo para indicar
# que esperamos cualquier tipo.

# De manera similar, si el tipo para el retorno de una función/método es 'None',
# se asume que no debe retornar un valor. i.e. def func() -> None:

class Node():
    def __init__(self, key: typing.Any) -> None:
        self.prev: Node | None = None
        self.next: Node | None = None
        self.key: typing.Any = key

    def __str__(self) -> str:
        # Para pensar: ¿por que decidimos no imprimir 'self.prev'?
        return f"Node(key: {self.key}, next: {self.next})"

class LinkedList():
    def __init__(self) -> None:
        self.head: Node | None = None

    def __str__(self) -> str:
        """
        Retorna una representación imprimible de nuestra lista encadenada
        """
        repl = []
        x = self.head
        while x is not None:
            key = x.key
            repl.append(key)
            x = x.next

        return f"LinkedList(len: {len(repl)}, {repl})"

    def insert(self, x: Node):
        """
        Inserta un elemento al inicio de la lista
        """
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def delete(self, x: Node):
        """
        Borra un elemento de la lista
        Nota: Este código supone que 'x' hace parte de la lista
        """
        if x.prev is not None:
            # si el elemento 'x' tiene predecesor i.e. A <-> x <-> B
            # ponemos que el sucesor del predecesor de 'x' sea igual al sucesor de 'x'
            # i.e A -> B
            x.prev.next = x.next
        else:
            # si 'x' not tiene predecesor se asume que es la cabeza de la lista
            # i.e. Head -> x.next
            self.head = x.next

        if x.next is not None:
            # si el elemento 'x' tiene un sucesor, ponemos que el predecesor sea
            # sucesor de 'x'
            # i.e. A <-> x <-> B => A <- B
            x.next.prev = x.prev

        # Con estos dos pasos obtenemos que para un elemento 'x' de forma
        # A <-> x <-> B sea ahora A <-> B

    def search(self, key: typing.Any) -> Node | None:
        """
        Busca un elemento en la lista con valor de 'key'
        """
        x = self.head
        while x is not None and x.key != key:
            x = x.next
        return x

def ejemplo01():
    ll = LinkedList()
    ll.insert(Node(2))
    print(ll)
    ll.insert(Node(3))
    print(ll)
    ll.insert(Node(1))
    print(ll)
    ll.insert(Node(3))
    print(ll)

    # Buscamos el elemento con valor '1'
    e = ll.search(1)
    print(e)
    assert e is not None, "el elemento con valor '1' debe existir"

    ll.delete(e)
    print(ll)

def main():
    ejemplo01()

main()