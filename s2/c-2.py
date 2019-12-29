class selftest:
    def function1():
        print('function1 called')

    def function2(slef):
        print('function2 called')

f = selftest()

f.function2()
print(selftest.function1())
