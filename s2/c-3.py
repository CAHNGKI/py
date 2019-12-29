class warehouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        warehouse.stock_num += 1

    def __del__(self):
        warehouse.stock_num -= 1

user1 = warehouse('kim')
user2 = warehouse('park')

print(user1.name)
print(user1.__dict__)
print(warehouse.__dict__)
print(user1.stock_num)
