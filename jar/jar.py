class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        cookie_jar = []
        for _ in range(self._size):
            cookie_jar.append("🍪")
        return "".join(cookie_jar)

    def deposit(self, cookies):
        if cookies < 0 or self._size + cookies > self._capacity:
            raise ValueError("Too many cookies.")
        self._size += cookies

    def withdraw(self, cookies):
        if cookies < 0 or cookies > self._size:
            raise ValueError("Not enough cookies.")
        self._size -= cookies

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    print(Jar(int(input("Capacity: "))))

if __name__ == "__main__":
    main()
