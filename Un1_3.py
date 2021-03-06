#!/usr/bin/env python3
# Purpose: Say hello

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
    
    parser.add_argument('-f', '--file', help='A readable file', metavar='FILE', type=argparse.FileType('r'), default=None)
    
    return parser.parse_args()
    
def main():
    args = get_args()
    file_arg = args.file
    
    print('Hello, ' + args.name + '!')
      
    if file_arg != None:
        print('\nfile_arg = "{}"\n'.format(file_arg.name))
        
        with open('{}'.format(file_arg.name), 'r') as fp:
        # считываем сразу весь файл
            data = fp.read()
        
        for line in data.splitlines():
            print(line)
    
    '''
    # читаем файл по 20 байт
        chunk = fp.read(20)
        while chunk:
            print(chunk)
            chunk = fp.read(20)
    '''
    
if __name__ == '__main__':
    main()
    
# python Un1_3.py -n Universe
## > Hello, Universe!

# python Un1_3.py 
## > Hello, World!

# python Un1_3.py -f text_file.txt

# python Un1_3.py -h