import argparse

# Usage
# python multiply.py --x 4 --y 5
# python multiply.py 4 5

parser = argparse.ArgumentParser()

parser.add_argument('--x', type=int, required=True, help='The first value to multiply')
parser.add_argument('--y', type=int, required=True, help='The second value to multiply')

# parser.add_argument('a', type=int)
# parser.add_argument('b', type=int)

args = parser.parse_args()
product = args.x * args.y
print('Product:', product)