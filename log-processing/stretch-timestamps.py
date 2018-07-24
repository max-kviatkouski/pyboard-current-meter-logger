#!/usr/bin/env python3

def load_corrections(filename):
    date_fomat = '(%Y, %-m, %-d)'
    with open(filename) as f:
        lines = f.readlines()
        start_ = lines[0]
        end_actual_ = lines[-2]
        end_expected_ = lines[-1]
        pass

def main():
    pass

if __name__ == "__main__":
    main()