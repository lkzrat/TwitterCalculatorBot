#Modules
import csv

class Mycsv:
    @classmethod
    def write(cls, text: str, file: str) -> None:
        """
        writes a string per row
        :param text: string
        """
        with open(file, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([text])

    @classmethod
    def read(cls, file: str) -> list[str]:
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
