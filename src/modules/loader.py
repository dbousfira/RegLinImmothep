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

    def ensure_data_loaded(self):
        """Ensure if data are already loaded. Download if missing."""
        if path.exists(LOCAL_PATH) == False:
            self._download_data()

        if len(listdir(RAW_LOCAL_PATH)) == 0:
            self._extract_data()

        print('Les fichiers sont correctement extraits')

    def _download_data(self):
        """
        Download the data from internet
        """

        print('Donwloading data')
        with open(LOCAL_PATH, "wb") as f:
            response = requests.get(ZIP_REMOTE_PATH, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:  # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)

                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" %
                                     ('=' * done, ' ' * (50-done)))
                    sys.stdout.flush()

        print('Data download successfully')

        self._extract_data()

    def _extract_data(self):
        """
        Extract the zip file to the hard disk
        """

        print('Begin extracting data')
        with zipfile.ZipFile(LOCAL_PATH, 'r') as zip_ref:
            zip_ref.extractall(RAW_LOCAL_PATH)
        print('Data extract successfully')


if __name__ == "__main__":
    pass
