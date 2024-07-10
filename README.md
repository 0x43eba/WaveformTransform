## Waveform Transformer

# Image to Sound Converter

This Python script converts images into sound files by interpreting the image data and generating corresponding audio signals.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib
- SciPy

## Installation

Ensure you have Python installed on your system. You can then install the required packages using pip:

```bash
pip install opencv-python numpy matplotlib scipy
```

## Usage
To use the script, you need to provide the path to the input image file (PNG format) and the desired output path for the WAV file.

## Flags

-f or --file: Specifies the path to the input image file. Only PNG files are supported.
-o or --output: Specifies the path where the output WAV file will be saved. Only WAV files are supported.
-h or --help: Displays the usage information.

## Example

```bash
python main.py -f example.png -o output.wav
```

This command will read example.png, process the image, and generate a sound file named output.wav based on the image data.
