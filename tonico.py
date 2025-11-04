#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Markus Thilo'
__version__ = '0.0.1_2025-11-04'
__license__ = 'GPL-3'
__email__ = 'markus.thilo@gmail.com'
__status__ = 'Testing'
__description__ = 'Read binary file and generate human readable output'

from argparse import ArgumentParser
from pathlib import Path

if __name__ == '__main__':  # start here when run as application
	argparser = ArgumentParser(description=__description__)
	argparser.add_argument('-e', '--encodings', type=str, metavar='STRING',
		help='Encodings to try (e.g. ascii,cp1252,utf-8 - comma, no spaces, the default is "ascii,cp1252,utf-8")')
	argparser.add_argument('-o', '--out', type=Path, metavar='FILE',
		help='File to store output as CSV/TSV')
	argparser.add_argument('src_file_paths', nargs=1, help='Source file', type=Path, metavar='FILE')
	args = argparser.parse_args()
	encodings = args.encodings.split(',') if args.encodings else ['ascii', 'cp1252', 'utf-8']
	ofh = args.out.open('w') if args.out else None
	int_array = args.src_file_paths[0].read_bytes()
	line = f'hex\t{"\t".join(encodings)}'
	print(f'hex\t{"\t".join(encodings)}')
	if ofh:
		print(line, file=ofh)
	for i in range(0, len(int_array)):
		line = f'{int_array[i]:X}'
		for enc in encodings:
			line += f'\t{bytes(int_array[i:i+8]).decode(enc, errors='replace' )[0]}'
		print(line)
		if ofh:
			print(line, file=ofh)
	if ofh:
		ofh.close()