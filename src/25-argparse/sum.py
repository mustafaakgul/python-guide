import argparse

#python sum.py --values 4 5 6

parser = argparse.ArgumentParser()
parser.add_argument('--values', type=int, nargs='+', help='list of values')
args = parser.parse_args()
sum = sum(args.values)
print('Sum:', sum)