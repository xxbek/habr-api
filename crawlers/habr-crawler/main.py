from crawler_tools.habr_parser import HabrParser
import argparse
import logging
import json

if __name__ == '__main__':
    # TODO add import from json config with headers, brand, nums
    # TODO add delay and while True
    arg_parser = argparse.ArgumentParser('seach data in habr-crawler.com')
    arg_parser.add_argument('--num', help='Input the nums of article')
    arg_parser.add_argument('--brand', help='Input the researched item')
    args = arg_parser.parse_args()

    num = 40
    # int(args.num)
    brand = 'editor-js codex'

    habr_parser = HabrParser(brand)
    result = habr_parser.run_parser(num)

    with open('result', 'w') as f:
        f.write(result)
