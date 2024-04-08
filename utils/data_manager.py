import numpy as np
import os
import time
from tqdm import tqdm
import matplotlib.pyplot as plt


def organize_data(input_file: str, points_per_file: int, output_folder: str) -> None:
    try:
        t1: int = time.time_ns()
        # Load data from the input file
        data: np.ndarray[np.int64] = np.loadtxt(input_file)

        # Determine the total number of output files needed
        num_files = (len(data) + points_per_file - 1) // points_per_file

        # Forces the folder creation inside 'data'
        output_folder = os.path.join('data', output_folder)

        # Initialize tqdm progress bar
        progress_bar: tqdm = tqdm(total=num_files, desc="Writing files", unit="file", position=0, unit_scale=True)

        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Write each part into separate files
        for i in range(num_files):
            # Determine the start and end indices for the current part
            start_idx = i * points_per_file
            end_idx = min((i + 1) * points_per_file, len(data))

            # Extract the current part of the data
            part = data[start_idx:end_idx]

            # Generate the output file name
            output_file = os.path.join(output_folder, f"waveform_{i+1}.txt")

            # Write the part to the output file
            np.savetxt(output_file, part, fmt="%d")

            # Update progress bar
            progress_bar.update(1)

        t2: int = time.time_ns()
        progress_bar.close()

        # Time conversion to minutes
        t1_seconds: float = t1 / 1_000_000_000
        t2_seconds: float = t2 / 1_000_000_000
        time_difference_seconds: float = t2_seconds - t1_seconds
        time_difference_minutes: float = time_difference_seconds / 60

        print(f"{num_files} files created in {output_folder}.\nTime elapsed: {time_difference_minutes} minutes")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")

    except IOError as e:
        print(f"Error: Failed to create output folder '{output_folder}': {e}")


def assemble_data_matrix(input_folder: str, num_data_points_per_file: int):
    try:
        # Get a list of all files in the input folder
        files = os.listdir(input_folder)

        # Initialize the data matrix with zeros
        data_matrix = np.zeros((len(files), num_data_points_per_file))

        # Fill the data matrix with data from each file
        for i, file in enumerate(files):
            file_path = os.path.join(input_folder, file)
            data = np.loadtxt(file_path)
            # Extract first num_data_points_per_file data points
            data_matrix[i, :] = data

        return data_matrix

    except FileNotFoundError:
        print(f"Error: Input folder '{input_folder}' not found.")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None


def plot_file(file_path: str, output_file: str) -> None:
    try:
        # Load intensity data from the file
        intensity = np.loadtxt(file_path)

        # Generate indices for the data points
        indices = np.arange(len(intensity))

        # Plot the intensity data
        plt.plot(indices, intensity)
        plt.xlabel('Index')
        plt.ylabel('Intensity')
        plt.title('Signal Intensity Plot')
        plt.grid(True)

        # Save the plot as a file
        plt.savefig(output_file)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")