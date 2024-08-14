import os
from PIL import Image
import numpy as np


class ImageController:

    def __init__(self, image_name):
        self.name, self.ext = os.path.splitext(image_name)
        self.original = Image.open(image_name)
        self.gray = self.gray_scale()
        self.auto = self.auto_level()
        self.dither = self.dithering()

    def gray_scale(self) -> Image:
        # use Y of YCbCr since Y = luminance
        # Y' = 0.2126R + 0.7152G + 0.0722B
        new_image = Image.open(f"{self.name}{self.ext}")
        width, height = new_image.size
        pixels = (new_image.convert('RGB')).load()

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                gray_y = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
                new_image.putpixel((x, y), (gray_y, gray_y, gray_y))

        new_image.save(f"{self.name}_gray{self.ext}")
        return new_image

    def auto_level(self) -> Image:
        new_image = Image.open(f"{self.name}{self.ext}")
        width, height = new_image.size
        total_pixels = width * height
        scale_factor = 255 / total_pixels

        hist_r = [0] * 256
        hist_g = [0] * 256
        hist_b = [0] * 256
        pixels = (new_image.convert('RGB').load())
        # count the appearances of R, G, B
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                hist_r[r] += 1
                hist_g[g] += 1
                hist_b[b] += 1

        # cumulative histogram of each channel
        cum_hist_r = [0] * 256
        cum_hist_g = [0] * 256
        cum_hist_b = [0] * 256
        sum_r = sum_g = sum_b = 0
        for i in range(256):
            sum_r += hist_r[i]
            cum_hist_r[i] = int(sum_r * scale_factor)
            sum_g += hist_g[i]
            cum_hist_g[i] = int(sum_g * scale_factor)
            sum_b += hist_b[i]
            cum_hist_b[i] = int(sum_b * scale_factor)

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                new_image.putpixel((x, y), (cum_hist_r[r], cum_hist_g[g], cum_hist_b[b]))
        new_image.save(f"{self.name}_auto{self.ext}")
        return new_image

    def dithering(self) -> Image:
        new_image = Image.open(f"{self.name}{self.ext}")
        width, height = new_image.size
        pixels = (new_image.convert('RGB')).load()
        n = 8
        threshold_mat = np.array([
            [0, 32, 8, 40, 2, 34, 10, 42],
            [48, 16, 56, 24, 50, 18, 58, 26],
            [12, 44, 4, 36, 14, 46, 6, 38],
            [60, 28, 52, 20, 62, 30, 54, 22],
            [3, 35, 11, 43, 1, 33, 9, 41],
            [51, 19, 59, 27, 49, 17, 57, 25],
            [15, 47, 7, 39, 13, 45, 5, 37],
            [63, 31, 55, 23, 61, 29, 53, 21]
        ]) / 64.0 * 255

        # white if Y > dithering matrix, else black
        for x in range(width):
            for y in range(height):
                i = x % n
                j = y % n
                r, g, b = pixels[x, y]
                gray_scale = (0.2126 * r + 0.7152 * g + 0.0722 * b)
                if gray_scale > threshold_mat[i][j]:
                    new_image.putpixel((x, y), (255, 255, 255))
                else:
                    new_image.putpixel((x, y), (0, 0, 0))
        new_image.save(f"{self.name}_dither{self.ext}")
        return new_image
