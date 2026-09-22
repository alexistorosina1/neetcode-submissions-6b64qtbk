class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.fixed_array = [None] * capacity

    def get(self, i: int) -> int:
        return self.fixed_array[i]

    def set(self, i: int, n: int) -> None:
        self.fixed_array[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.fixed_array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
        return self.fixed_array[self.size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_fixed_arr = [None] * self.capacity
        for i in range(self.size):
            new_fixed_arr[i] = self.fixed_array[i]
        self.fixed_array = new_fixed_arr 

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
