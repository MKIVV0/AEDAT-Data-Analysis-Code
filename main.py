from datetime import date
from src.classes.noise_characterization import NoiseCharacterization
import utils.data_manager as dm
import os
import numpy as np


if __name__ == "__main__":
    obj1 = NoiseCharacterization(date(2024, 4, 4))
    print(obj1.get_date())

    file_path: str = os.path.join("data", "24-04-04-dataset", "wave0.txt")
    # dm.organize_data(file_path, 1030, output_folder="24-04-04-organized_data")

    '''
    for i in range(1, 5):
        f_name = f"waveform_{i}.txt"
        f = os.path.join("data", "24-04-04-organized_data", f_name)
        dm.plot_file(f, f"waveform_{i}")
    '''
    p = os.path.join("data", "24-04-04-organized_data")
    matrix: np.ndarray = dm.assemble_data_matrix(p, 1030)
    print(matrix)
    print(np.shape(matrix))
