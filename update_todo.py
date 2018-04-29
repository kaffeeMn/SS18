if __name__ == '__main__':
    lines = None
    with open('todo.txt', 'r') as f:
        lines = f.readlines()
        f.close()
    lines_str = ''.join(lines)
    print(lines_str)
    vals = lines_str.split(':')[2::2]
    keys = lines_str.split(':')[1::2]
    tasks = {}
    for i in range(len(keys)):
        tasks[keys[i]] = [v.rstrip() for v in vals[i].split('*')]
    print(tasks)
