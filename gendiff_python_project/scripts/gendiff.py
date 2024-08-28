#!/usr/bin/env/python3
import argparse



def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument("fisrt_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(args.format)


if __name__ == '__main__':
    main()