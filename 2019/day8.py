from matplotlib import pyplot as plt
import numpy as np

WIDTH = 25
HEIGHT = 6


def task1(image):
    layer_with_fewest_zeros = image[0]
    for layer in image: 
        if np.count_nonzero(layer) > np.count_nonzero(layer_with_fewest_zeros):
            layer_with_fewest_zeros = layer
    return (layer_with_fewest_zeros == 1).sum() * (layer_with_fewest_zeros == 2).sum()


def decode(image):
    decoded_image = np.copy(image[0])
    for layer in image[1:]: 
        transparent = decoded_image == 2
        decoded_image[transparent] = layer[transparent]
    return decoded_image


if __name__ == "__main__":
    with open("input8") as file:
        data = file.readline()[:-1]
    num_layers = len(data) // (WIDTH * HEIGHT)
    image = np.zeros((num_layers, HEIGHT, WIDTH), dtype=int)
    for layer in range(num_layers):
        for row in range(HEIGHT):
            for col in range(WIDTH):
                image[layer, row, col] = data[layer * WIDTH * HEIGHT + row * WIDTH + col]
    print("Task 1: %d" %task1(image))
    print("Task 2: see plot")
    decoded_image = decode(image)
    plt.imshow(decoded_image)
    plt.show()
