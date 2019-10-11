class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


if __name__ == '__main__':
    with ManagedFile('hello.txt') as f:
        f.write('hello, world!')
        f.write('bye now')
