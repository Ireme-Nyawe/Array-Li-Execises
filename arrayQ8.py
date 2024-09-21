# Program to create a 2D array representing an RGB image and invert the colors

image = [
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [0, 255, 255], [255, 0, 255]],
    [[192, 192, 192], [128, 128, 128], [64, 64, 64]]
]

def invert_colors(image):
    inverted_image = []
    for row in image:
        inverted_row = []
        for pixel in row:
            inverted_pixel = [255 - value for value in pixel]
            inverted_row.append(inverted_pixel)
        inverted_image.append(inverted_row)
    return inverted_image

inverted_image = invert_colors(image)

print("Original Image:")
for row in image:
    print(row)

print("\nInverted Image:")
for row in inverted_image:
    print(row)
