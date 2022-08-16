import csv
from pprint import pprint
import re
from Decorator.Decorator import path, path_logger


class CsvManager:
    def __init__(self, file):
        self.file = file

    @path_logger(path)
    def csv_opener(self):
        with open(self.file, encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            data = list(reader)
        return data

    @path_logger(path)
    def regulate_name(self, data):
        result = data
        for k, i in enumerate(data):
            lastname = i[0].split(' ')
            firstname = i[1].split(' ')
            if len(lastname) == 2:
                result[k][0] = lastname[0]
                result[k][1] = lastname[1]
            if len(lastname) == 3:
                result[k][0] = lastname[0]
                result[k][1] = lastname[1]
                result[k][2] = lastname[2]

            if len(firstname) == 2:
                result[k][1] = firstname[0]
                result[k][2] = firstname[1]
            if len(firstname) == 3:
                result[k][0] = firstname[0]
                result[k][1] = firstname[1]
                result[k][2] = firstname[2]

        return result

    @path_logger(path)
    def delete_doubles(self, data):
        result = data
        tmp_list = []
        for k, i in enumerate(data):
            for c in range(k+1, len(data)):
                if i[0] == data[c][0] and i[1] == data[c][1]:
                    if i[2] == '':
                        result[k][2] = data[c][2]
                    else:
                        result[k][2] = i[2]
                    if i[3] == '':
                        result[k][3] = data[c][3]
                    else:
                        result[k][3] = i[3]
                    if i[4] == '':
                        result[k][4] = data[c][4]
                    else:
                        result[k][4] = i[4]
                    if i[5] == '':
                        result[k][5] = data[c][5]
                    else:
                        result[k][5] = i[5]
                    if i[6] == '':
                        result[k][6] = data[c][6]
                    else:
                        result[k][6] = i[6]
                    tmp_list.append(c)

        for k, i in enumerate(tmp_list):
            result.pop(i-k)

        return result

    @path_logger(path)
    def regulate_phone_numbers(self, data):
        text = ''
        for i in range(len(data)):
            text = text + ',' + (','.join(data[i]))
        pattern = r"(\+7|8)\s?\(?(\d{3})\)?\s?-?(\d{3})-?(\d{2})-?(\d{2})"
        sub = r"+7(\2)\3-\4-\5"
        ad_pattern = r"(\+7|8)\s?\(?(\d{3})\)?\s?-?(\d{3})-?(\d{2})-?(\d{2})\s?\(?(доб.)\s(\d+)\)?"
        ad_sub = r"+7(\2)\3-\4-\5 \6\7"
        text = re.sub(pattern, sub, text)
        text = re.sub(ad_pattern, ad_sub, text)
        text = text.split(',')
        text.remove('')
        result = [text[i:i+7] for i in range(0, len(text), 7)]
        return result

    @path_logger(path)
    def csv_writer(self, result):
        with open("phonebook.csv", "w") as f:
            datawriter = csv.writer(f, delimiter=',')
            datawriter.writerows(result)
        print('Книга контактов в порядке!')

    @path_logger(path)
    def fix_contact_book(self):
        self.csv_writer(self.regulate_phone_numbers(self.delete_doubles(self.regulate_name(self.csv_opener()))))
