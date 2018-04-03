#!/usr/bin/env python
import os
import os.path as path

def gen_page(li):
    return '''
<header>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"/>
</header>
<body>
    <div class="mx-3 my-3">
        <H1>MODULES</H1>
        <ul>{}</ul>
    </div>
</body>
</html>
    '''.format(''.join(li)).strip()

if __name__ == '__main__':
    dir = path.dirname(path.realpath(__file__))
    modules = [m for m in os.listdir(dir) if path.isdir(m)]
    index_html = ['index.html' in os.listdir(m) for m in modules]
    li_str = []
    for i, m in enumerate(modules):
        if index_html[i]:
            li_str.append('<li><a href="{}/index.html">{}</a></li>'.format(m , m.split('/')[0]))
    index = gen_page(li_str)
    with open('index.html', 'w') as out:
        out.write(index)
