class MyCli():
    def __init__(self, name):
        self.name = name

    def call_check(self):
        print('name is {}'.format(self.name))