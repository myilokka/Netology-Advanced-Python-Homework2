from CsvManager import CsvManager


if __name__ == '__main__':
    file = 'phonebook_raw.csv'
    csv = CsvManager(file)
    csv.fix_contact_book()
