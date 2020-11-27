import openpyxl
import json
import os
import sys


EXCEL_COL_NO = 0
EXCEL_COL_SECTION = 1
EXCEL_COL_KEY = 2
EXCEL_COL_EN_VAL = 3
EXCEL_COL_JA_VAL = 4

def convert2json(excel_path):

    json_file_name = 'locale.json'
    json_path_en = 'locales/en/'
    json_path_ja = 'locales/ja/'

    wb = openpyxl.load_workbook(excel_path, data_only=True)
    sheets = wb['Sheet1']

    json_en = {}
    json_ja = {}
    section = []
    section_raw = []

    # keyとvalを取得する
    for row in sheets.iter_rows(min_row=2):
        if '' == row[EXCEL_COL_NO].value:
            break
        section_key = row[EXCEL_COL_SECTION].value
        key_val = row[EXCEL_COL_KEY].value
        en_val = row[EXCEL_COL_EN_VAL].value
        ja_val = row[EXCEL_COL_JA_VAL].value

        if section_key is None or key_val is None:
            continue

        if not section_key in json_en:
            json_en[section_key] = {}

        if not section_key in json_ja:
            json_ja[section_key] = {}

        json_en[section_key][key_val] = en_val
        json_ja[section_key][key_val] = ja_val

    write_json(json_path_en, json_file_name, json_en)
    write_json(json_path_ja, json_file_name, json_ja)


def write_json(file_path, file_name, json_dict):

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    json_file = file_path + file_name

    with open(json_file, mode='w') as f:
        f.write(json.dumps(json_dict, sort_keys=True,
                           ensure_ascii=False, indent=2))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('[ERROR] Please select Excel file')
        print('Usage:')
        print('  python ex2localejson.py EXCEL_PATH')
        exit(1)

    excel_path = sys.argv[1]
    convert2json(excel_path)

    print('complete!')

    exit(0)
