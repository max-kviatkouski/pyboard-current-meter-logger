import sys
import os
import re
import json

INDEX_JSON = 'report-index.json'

REPORT_FILENAME_PATTERN = "^\d{4}-\d{2}-\d{2}.csv$"

def main():
    index_folder = sys.argv[1]
    files = os.listdir(index_folder)
    result = list()
    for f in files:
        if re.match(REPORT_FILENAME_PATTERN, f):
            result.append(f.replace('.csv', ''))
        elif f != INDEX_JSON:
            print('Ignored file {} since it doesn\'t match {} pattern.'.format(f, REPORT_FILENAME_PATTERN))
    with open(os.path.join(index_folder, INDEX_JSON), 'w') as index_file:
        json.dump(result, index_file)
        print('{} has been succesfully updated.'.format(INDEX_JSON))


if __name__ == "__main__":
    main()