from datetime import date
from .assignment import Assignment
from typing import Optional
import utils.data_manager as dm
import os
import numpy as np


class NoiseCharacterization(Assignment):
    _instance: Optional["NoiseCharacterization"] = None

    def __new__(cls) -> "NoiseCharacterization":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, assignment_date: date) -> None:
        if not hasattr(self, "initialized"):
            super().__init__(assignment_date)
            self.initialized: bool = True
            self.matrix: np.ndarray = None
            self.waveform_file: str = os.path.join(
                "data", self.__assignment_date, "-waveforms", "waveforms.txt"
                )
            self.waveforms_folder: str = os.path.join(
                "data", self.__assignment_date, "-splitted-waveforms"
                )
            self.waveform_matrix_file: str = os.path.join(
                "data", self.__assignment_date, "-waveform-matrix", "matrix.txt"
                )

    def get_matrix(self) -> np.ndarray:
        """
        Get the class attribute matrix.

        Returns:
            numpy.ndarray: a waveform matrix.
        """
        if self.matrix is None:
            print("Import the waveform matrix first")
            return
        return self.matrix

    def set_matrix(self, matrix: np.ndarray) -> None:
        """
        Set the class attribute matrix.

        Args:
            matrix (numpy.ndarray): the imported waveform matrix.
        """
        self.matrix = matrix

    def show_menu(self):
        while True:
            print(self.get_date())
            print("Noise and Signal Characterization Menu:")
            print("\t1. Separate waveforms into multiple files.")
            print("\t2. Create a waveform matrix and save it to a file.")
            print("\t3. Load waveform matrix from file.")
            print("To go back to the main menu, enter -1.")
            sub_option: str = input("Select an option: ")

            match sub_option:
                case "1":
                    """
                    Input file path setting.
                    """
                    print("Insert the path of the file that contains multiple waveforms.")
                    print(f"By default is: {self.waveform_file}")
                    print("Just press <Enter> to keep the default path.")

                    # Assigns 'self.waveform_file', if the 'input_file_path'
                    # is an empty string.
                    input_file_path: str = input("Path: ") or self.waveform_file

                    """
                    Output folder path setting.
                    """
                    print("Insert the output folder for the waveforms.")
                    print(f"By default is: {self.waveforms_folder}")
                    print("Just press <Enter> to keep the default path.")

                    # Assigns 'self.waveforms_folder', if the 'output_folder_path'
                    # is an empty string.
                    output_folder_path: str = input("Path: ") or self.waveforms_folder

                    dm.organize_data(input_file_path, 1030, output_folder_path)

                case "2":
                    """
                    Input folder path setting.
                    """
                    print("Insert the path of the folder that contains the waveforms.")
                    print(f"By default is: {self.waveforms_folder}")
                    print("Just press <Enter> to keep the default path.")

                    # Assigns 'self.waveforms_folder', if the 'input_folder_path'
                    # is an empty string.
                    input_folder_path: str = input("Path: ") or self.waveforms_folder

                    """
                    Output file path setting.
                    """
                    print("Insert the output file path for the matrix.")
                    print(f"By default is: {self.waveform_matrix_file}")
                    print("Just press <Enter> to keep the default path.")
                    output_file_path: str = input("Path: ") or self.waveform_matrix_file

                    matrix = dm.assemble_data_matrix(input_folder_path, 1030)
                    # Function for saving a numpy matrix into a file.

                case "3":
                    """
                    Input file path setting.
                    """
                    print("Insert the path of the file that contains waveform matrix.")
                    print(f"By default is: {self.waveform_matrix_file}")
                    print("Just press <Enter> to keep the default path.")

                    # Assigns 'self.waveform_matrix_file', if the 'input_file_path'
                    # is an empty string.
                    input_file_path: str = input("Path: ") or self.waveform_matrix_file

                    # Import waveform matrix from file
                    # Assign the imported matrix to the class attribute self.matrix

                case "-1":
                    print("Going back to the main menu...")
                    break
