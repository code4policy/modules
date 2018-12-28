import pandas as pd
import argparse
import sys


def convert_data(file, output_format):
	input_format = file.split('.')[-1]

	if input_format == 'csv':
		data = pd.read_csv(file)
	elif input_format == 'tsv':
		data = pd.read_csv(file, sep = '\t')
	elif input_format == 'json':
		data = pd.read_json(file, orient = 'records')
	else:
		print('Input format not recognized, please use either .csv, .tsv, or .json')
		return

	output_file = file.replace(input_format, output_format)
	if output_format == 'csv':
		data.to_csv(output_file, index = False)
	elif output_format == 'tsv':
		data.to_csv(output_file, sep = '\t', index = False)
	elif output_format == 'json':
		data.to_json(output_file, orient = 'records')
	else:
		print('Output format not recognized, please use either csv, tsv, or json')
		return

	print('File converted')

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', help = 'file to convert')
	parser.add_argument('-o', '--outputformat', help = 'output format')

	args = parser.parse_args()

	if args.file:
		file = args.file
	else:
		sys.exit('Please specify a file to convert')

	if args.outputformat:
		output_format = args.outputformat
	else:
		sys.exit('Please specify a format to convert to')

	convert_data(file, output_format)


