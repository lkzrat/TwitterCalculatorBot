#Modules
import csv

class Mycsv:
    @classmethod
    def write(cls, text, file):
        """
        writes a string per row
        :param text: string
        """
        with open(file, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([text])

    @classmethod
    def read(cls, file):
        """
        reads the csv file
        :return: list object [row1, row2, row3, ...]
        """
        content = []
        with open(file) as f:
            reader = csv.reader(f)
            for row in reader:
                content.append(row)
        return content