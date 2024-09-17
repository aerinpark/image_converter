# Image Converter

---
## Overview
This is part of a coding project of CMPT 365: Multimedia Systems at Simon Fraser University. The main focus of this project is to create a program where users select an image of their choice and convert it into three different versions: grayscale, dithered and auto-leveled.

---
## Grayscale
A coloured image can be converted to grayscale by either averaging the RGB values or converting them into the YUV systems for each pixel. However, for greater accuracy, this program uses the <b>luminosity</b> method, specifically the <b>YCbCr model</b>, where Y represents luminance or brightness. The Y value for each pixel is calculated using the following equation:
<p style="text-align:center;">Y' = 0.2126R + 0.7152G + 0.0722B</p>
This method is more accurate than simple averaging because each RGB component has a different contribution to the overall luminance. Human eyes perceive colours with varying sensitivity, so averaging RGB values without accounting for this can result in lower-quality grayscale images.

---
## Dithering
Dithering is a technique in image processing that blends and disperses pixels of available shades to smooth out the image. This helps the image appear more natural and accurate despite the limitations of the colour palette.

This program uses ordered dithering, which utilizes a pre-defined threshold matrix, known as the  <b>dither matrix</b>. This matrix determines how shades are dispersed throughout the image. For smoother images with as little loss in details as possible, 8 x 8 matrix is used:

| 0   | 32  | 8   | 40  | 2   | 34  | 10  | 42  |
|-----|-----|-----|-----|-----|-----|-----|-----|
| 48  | 16  | 56  | 24  | 50  | 18  | 58  | 26  |
| 12  | 44  | 4   | 36  | 14  | 46  | 6   | 38  |
| 60  | 28  | 52  | 20  | 62  | 30  | 54  | 22  |
| 3   | 35  | 11  | 43  | 1   | 33  | 9   | 41  |
| 51  | 19  | 59  | 27  | 49  | 17  | 57  | 25  |
| 15  | 47  | 7   | 39  | 13  | 45  | 5   | 37  |
| 63  | 31  | 55  | 23  | 61  | 29  | 53  | 21  |

---
## Auto-level
Auto-Leveling is a feature in some image processing programs that redistributes the colours of an image to enhance its contrast and brightness, improving the overall vibrancy of the image.

This program uses a histogram equalization algorithm to emulate the auto-leveling feature. It works as follows:
1. <b>Create the Histogram: </b>Generate a histogram for the R values of the image.
2. <b>Cumulative Histogram: </b>Scan through the histogram to create and normalize the cumulative histogram.
3. <b>Repeat for R and B: </b>Perform steps 1 and 2 for both G and B channels.
4. <b>Update Pixel Values: </b>Reassign each pixel's RGB values using the normalized cumulative histograms.

---
## Getting Started
1. Clone the repository<br>
`git clone https://github.com/aerinpark/image_converter.git`
2. Run the program<br>
`python3 main.py`

---
## Instructions
* Supported image formats are: .bmp, .jpeg, .jpg, .png, and .webp
* The original image will be displayed on the left side of the screen once selected.
* The modified image (grayscale, dither, auto-level) will be shown on the right side when the corresponding buttons are pressed.
