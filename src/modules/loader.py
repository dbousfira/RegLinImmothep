import csv
from os import path, listdir
import pandas as pd
import requests
import sys
import zipfile

csv.field_size_limit(10000000)

ZIP_REMOTE_PATH = 'https://stdatalake005.blob.core.windows.net/public/movies_dataset.zip'
LOCAL_PATH = '../data/IN/valeursfoncieres-2019.txt'
RAW_LOCAL_PATH = '../data/IN/'
CURATED_LOCAL_PATH = '../data/OUT/'
# RAW_LOCAL_PATH = 'data/IN/'
# CURATED_LOCAL_PATH = 'data/OUT/'


class DataLoader:

    def split_data(self, filename, sep, column_name, values=None, input=True):
        """Break raw data into one or many files.

        Args:
            filename (str): source file name
            sep (str): file delimiter
            column_name (str): header column of tsv/csv file
            values (list, optional): values to extract. Defaults to None
            input (bool): input (True) or output (False) folder. Defaults to input (True).
        """

        with open(RAW_LOCAL_PATH if input else CURATED_LOCAL_PATH + filename, encoding='utf-8') as file_stream:
            file_stream_reader = csv.DictReader(
                file_stream, delimiter=sep)

            open_files_references = {}

            for row in file_stream_reader:
                column_value = row[column_name]

                # if column_value == value:

                # Open a new file and write the header
                if column_value not in open_files_references:
                    if values is None or (values is not None and column_value in values):
                        output_file = open(
                            CURATED_LOCAL_PATH + f'{column_value}.csv', 'w', encoding='utf-8', newline='')
                        dictionary_writer = csv.DictWriter(
                            output_file, fieldnames=file_stream_reader.fieldnames, delimiter=sep)
                        dictionary_writer.writeheader()
                        open_files_references[column_value] = output_file, dictionary_writer

                if values is None or (values is not None and column_value in values):
                    # Always write the row
                    open_files_references[column_value][1].writerow(row)

            # Close all the files
            for output_file, _ in open_files_references.values():
                output_file.close()


if __name__ == "__main__":
    pass
