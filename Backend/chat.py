def greet(func):
    def internal():
        print('Abhishek Raj Pipal')
        func()
    return internal


@greet
def output():
    print('Abhishek Raj')

output()
