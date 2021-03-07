#!/usr/bin/env python3
"""Jump the Five"""

import argparse

# --------------------------------------------------

def get_args():
	parser = argparse.ArgumentParser(description='Jump the Five',
									formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('text', metavar='str', help='Input text')
	return parser.parse_args()

def main():
	args = get_args()
	jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
				'6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}
	for char in args.text:
		print(jumper.get(char, char), end='')
	print()

# --------------------------------------------------

if __name__ == '__main__':
	main()

# $ ./Un4.py 867-5309
# 243-0751
# $ ./Un4.py 'Call 1-800-329-8044 today!'
# Call 9-255-781-2566 today!