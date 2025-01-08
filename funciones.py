def find_volume(depth: int, length: int = 1, width: int = 1) -> list:
    '''Retornando multiples valores'''
    return length * width * depth, 'otro valor', 'uno más'


def run():
    print(find_volume(12));


if __name__ == '__main__':
    run()