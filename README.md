## Waveform Transformer

A user provided image is converted into a spline, which is then applyed to windows of a generated wave function as a frequency transform.

### High Contrast Line Drawing
<img width="850" alt="target" src="https://github.com/0x43eba/WaveformTransform/assets/76260172/aca82875-0fcb-4f89-9e7a-a36fc85fbf15">

### Resulting Edge Detection
<img width="849" alt="Screenshot 2024-07-10 at 20 06 03" src="https://github.com/0x43eba/WaveformTransform/assets/76260172/6e3a2c3c-605d-4c11-8faa-1a31af38d186">

### Resulting Spline Fit and Spline Expansion
<img width="642" alt="Screenshot 2024-07-10 at 20 05 42" src="https://github.com/0x43eba/WaveformTransform/assets/76260172/995cbb74-ff82-48d0-9b1a-68901166ab53">
<img width="642" alt="Screenshot 2024-07-10 at 20 05 47" src="https://github.com/0x43eba/WaveformTransform/assets/76260172/8b6b9d95-ebb9-4d83-928a-211c904c2bc2">

### Resulting Wave Function
<img width="640" alt="Screenshot 2024-07-10 at 20 05 53" src="https://github.com/0x43eba/WaveformTransform/assets/76260172/54f41b0f-7e71-453a-bc5e-8a5ec5b83d2a">


### Resulting Output WAVE File (segment)
<img width="570" alt="Screenshot 2024-07-10 at 20 12 46" src="https://github.com/0x43eba/WaveformTransform/assets/76260172/952b6366-ca5a-40ea-941b-68824fd89781">

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
