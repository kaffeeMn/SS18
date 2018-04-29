if __name__ == '__main__':
    lines = None
    with open('todo.txt', 'r') as f:
        lines = f.readlines()
        f.close()
    lines_str = ''.join(lines)
    print(lines_str)
    tasks = lines_str.split(':')[::2]
    print(tasks)
