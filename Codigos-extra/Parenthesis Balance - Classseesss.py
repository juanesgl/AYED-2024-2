from sys import stdin


# Complejidad espacial: O(n)
class Stack:
    def __init__(self, n: int) -> None:
        assert n > 0
        self.top: int = -1
        self.S: list[str | None] = [None] * n

    def is_empty(self) -> bool: # T(n) = O(1)
        if self.top == -1:
            return True
        else:
            return False

    def is_full(self) -> bool: # T(n) = O(1)
        return self.top + 1 == len(self.S)

    def push(self, x: str): # T(n) = O(1)
        assert not self.is_full()

        self.top += 1
        self.S[self.top] = x

    def pop(self) -> str: # T(n) = O(1)
        assert not self.is_empty()

        self.top -= 1
        v =  self.S[self.top + 1]
        assert v is not None
        return v

    # en vez de crear un stack nuevo, podemos resetearlo para que sea vacio en O(1)
    def clear(self):
        self.top = -1

    def __str__(self) -> str:
        return f"Stack(top: {self.top} - array: {self.S[0: max(self.top+1, 0)]})"


def read() -> str:
    return stdin.readline().strip()


def solve(stack: Stack, pattern: str) -> bool:
    stack.clear()

    for char in pattern:
        if char in "([":
            stack.push(char)

        if char in "])":
            if stack.is_empty():
                return False

            v = stack.pop()
            if char == "]" and v != "[":
                return False

            if char == ")" and v != "(":
                return False

    return stack.is_empty()


def main():
    stack = Stack(130)
    n = int(read())
    for _ in range(n):
        s = read()
        print("Yes" if solve(stack, s) else "No")


main()