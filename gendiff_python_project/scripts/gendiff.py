#!/usr/bin/env/python3
import argparse



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fisrt_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()