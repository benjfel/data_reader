import csv
import json
import xml.etree.ElementTree as xml
import xlrd as excel

def read_csv(file_path, delimiter, has_headers):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)

        # skip first row (column headers)
        if has_headers:
            next(csv_reader)

        csv_data = []

        for row in csv_reader:
            csv_data.append(row)
        
        return csv_data

def read_json(file_path):
    with open(file_path) as json_file:
        json_data = json.loads(json_file.read())

        return json_data

def read_xml(file_path):
    with open(file_path) as xml_file:
        root = xml.parse(xml_file).getroot()

        xml_data = []

        for child in root.iter():
            xml_data.append(child.text)

        return xml_data

def read_excel(file_path, has_headers, sheet_index = 0):
    workbook = excel.open_workbook(file_path)
    sheet = workbook.sheet_by_index(sheet_index)

    start = 0
    if has_headers:
        start = 1

    cell_values = []

    for row_index in range(start, sheet.nrows):
        cell_values.append(sheet.row_values(row_index))

    return cell_values