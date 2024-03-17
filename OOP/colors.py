class colorizer:

    def __init__(self, color):
        self.color = color

    def __enter__(self):
        if self.color == 'red':
            print("\033[91m", end='')
        elif self.color == 'green':
            print("\033[92m", end='')
        elif self.color == 'yellow':
            print("\033[93m", end='')
        elif self.color == 'blue':
            print("\033[94m", end='')
        elif self.color == 'purple':
            print("\033[95m", end='')
        elif self.color == 'cyan':
            print("\033[96m", end='')
        elif self.color == 'white':
            print("\033[97m", end='')

    def __exit__(self, exc_type, exc_value, traceback):
        print("\033[0m", end='')

with colorizer('red'):
    print('printed in red')
print('printed in default color')