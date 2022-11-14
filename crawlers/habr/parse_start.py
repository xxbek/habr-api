from habr_parser import HabrParser
import argparse

arg_parser = argparse.ArgumentParser('seach data in habr.com')
arg_parser.add_argument('--num', help='Input the nums of article')
arg_parser.add_argument('--brand', help='Input the researched item')
args = arg_parser.parse_args()

num = 3
# int(args.num)
brand = 'nodejs'

habr_parser = HabrParser()
result = habr_parser.run_parser(num, brand)

with open('result', 'w') as f:
    f.write(result)
