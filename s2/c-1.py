class userinfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print('-------------')
        print(self.name)
        print(self.phone)
        print('-------------')

user1 = userinfo('kim', '010-0000-0000')
user2 = userinfo('park', '010-1111-1111')

user1.print_info()
user2.print_info()
