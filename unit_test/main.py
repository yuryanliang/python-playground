class Hello:
    def hello(self):
        return "hello"

    def __double__(self):
        return 'hellohello'
    def __get__(self):
        return 'h'