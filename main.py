import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

from scipy.io.wavfile import write
from scipy.interpolate import CubicSpline

FORMAT = cv2.IMREAD_GRAYSCALE

def flags_parser(input):

    # Input validation
    for entry in input:
        if entry == "-h" or entry == "--help":
            print("Usage: python main.py -f [image_path] -o [output_path]")
            sys.exit(0)
        if len(input) < 3:
            print("Usage: python main.py -f [image_path] -o [output_path]")
            sys.exit(1)
    if "-f" and "-o" not in input:
        print("Usage: python main.py -f [image_path] -o [output_path]")
        sys.exit(1)
    
    # Parse the input
    for entry in input:
        if entry == "-f":
            file_dir = input[input.index(entry) + 1]
            if not file_dir.endswith(".png"):
                print("Only PNG files are supported")
                sys.exit(1)
        if entry == "-o":
            output_dir = input[input.index(entry) + 1]
            if not output_dir.endswith(".wav"):
                print("Only WAV files are supported")
                sys.exit(1)

    return file_dir, output_dir

def image_parse(file_dir: str):

    # Read the image
    image = cv2.imread(file_dir, FORMAT)
    
    # Generate the outline
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    
    # Threshold the image
    sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    sobel_magnitude = np.uint8(np.clip(sobel_magnitude, 0, 255))
    _, binary_image = cv2.threshold(image, 250, 255, cv2.THRESH_BINARY)

    # Invert the image
    cv2.bitwise_not(binary_image, binary_image)
    
    # re-orient the image back to the original orientation
    binary_image = np.array(list(reversed(binary_image)))
    out = np.where(binary_image == 255)
    display = cv2.flip(binary_image, 0)
    
    # Display the image
    cv2.imshow("Outline", display)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return out[1], out[0]

def generate_frequency(base, transformer):
    
    # Output sine wave
    output = []

    # Output linear transform 
    linear_transform = []
    
    # The raw transform
    plt.plot([x for x in range(len(transformer))], transformer)
    plt.show()
    
    for i in transformer.tolist():
        
        # Generate the sine wave
        wave_data = np.sin(2 * np.pi * base * i * np.arange(5) / 5)
        for entry in wave_data.tolist():
            output.append(entry)
        
        # Generate the no-op validation transform 
        line_data = np.linspace(1, 1, 5)
        line_data = line_data * i
        for entry in line_data.tolist():
            linear_transform.append(entry)

    # Validation transform, should be the transformer, but scaled out to the max value of the sine wave
    plt.plot([x for x in range(len(linear_transform))], linear_transform)
    plt.show()

    # Returning the data as a float32 array here
    return np.asarray(output, dtype=np.float32)

def process_coordinates(x_coords, y_coords):
    # Dedouped coordinates
    cleaned_coords = []
    cleaned_coords_y = []
    
    # Remove duplicates
    for i in range(len(x_coords)):
        if x_coords[i] not in cleaned_coords:
            cleaned_coords_y.append(y_coords[i])
            cleaned_coords.append(x_coords[i])
    
    # Normalize the y coordinates
    y = cleaned_coords_y / np.max(np.abs(cleaned_coords_y))
    x = cleaned_coords
    d2 = np.column_stack((x, y))
    
    # Sort them for the spline fit
    sorted_indices = np.argsort(d2[:, 0])
    sorted_points = d2[sorted_indices]
    
    # Fit the spline
    cs = CubicSpline(sorted_points[:, 0], sorted_points[:, 1])

    # Generate the spline
    x_fine = np.linspace(min(x), max(x), 5000)
    y_fine = cs(x_fine)

    # Plot the spline
    plt.scatter([x for x in range(len(y_fine))], y_fine)
    plt.show()
    
    # Scale the spline
    scaled = np.int16(y_fine / np.max(np.abs(y_fine)) * 32767)
    return scaled

if __name__ == "__main__":
    target_name, output_name = flags_parser(sys.argv)

    # Parse the image
    x_coords, y_coords = image_parse(target_name)
    
    # Process the coordinates
    scaled = process_coordinates(x_coords, y_coords)
    
    # Generate and transform the frequency
    data = generate_frequency(1, scaled)

    # Plot the final data
    plt.plot([x for x in range(len(data))], data)
    plt.show()
    
    # Write the data to a WAV file
    write(output_name, 100, data)
