#!/usr/bin/env python3
"""Crow's Nest"""

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('word', metavar='word', default='', help='give a word')
    return parser.parse_args()

def main():
    args = get_args()
    word = args.word
    
    article = ''
    if word[0].lower() in 'aeiou':     
        article = 'an'
    else:
        article = 'a'
    
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')
    
if __name__ == '__main__':
    main()
    
# python Un2.py narwhal