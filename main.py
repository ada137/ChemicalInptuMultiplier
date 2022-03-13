import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class ChemicalinpUtMultiplier:

    def __init__(self, input_file=None, output_file=None):

        self.input_file = input_file
        self.output_file = output_file

        self.initial_data = pd.DataFrame()

    def load_file(self, path):
        """
        loads file into the object
        :param path: str, path to input file
        """
        if not os.path.isfile(path):
            raise FileNotFoundError()
        self.input_file = path

    def set_output_file(self, path, overwrite=True):
        """
        set path where output file will be saved
        :param overwrite: bool, True existing file will be overwritten, False otherwise
        :param path: str, set the path of output file
        """
        if overwrite is False:
            if os.path.isfile(path):
                raise FileExistsError()
        self.output_file = path

    def exec(self):
        if self.input_file is None or self.output_file is None:
            raise Exception("Input or output not good")

        self.initial_data = pd.read_csv(self.input_file)
        print(self.initial_data)

        while True:
            break


if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
