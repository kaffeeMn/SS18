import os
from copy import deepcopy

def gen_rst(pdf_list, path_list):
    bullet_list = ''
    for i, pdf in enumerate(pdf_list):
        bullet_list += '* :download:`{}<{}>`\n'.format(pdf, path_list[i])
    return '''
    UBs
    ===

    {}
    '''.format(bullet_list)

def crawl(dir):
    files = []
    paths = []
    for root, _, files in os.walk(dir):
        pdf_list = []
        path_list = []
        for f in files:
            if f[-4:] == '.pdf':
                rst_str = (f[:-4], root)
                files.append(rst_str)
                paths.append(
                    '{}/rst/source/{}.rst'.format(
                        root.split(dir)[1].split('/')[0]
                        , f[:-4]
                    )
                )

    return files, paths

def write(file_str, file_path):
    for i, p in enumerate(file_path):
        with open(p, 'w') as f:
            f.write(file_str[i])

if __name__ == '__main__':
    files, paths = crawl('./')
    write(files, paths)
