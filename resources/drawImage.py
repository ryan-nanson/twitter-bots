#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import imageio
import numpy
import matplotlib.pyplot as plot
import scipy.ndimage

def drawImage(image_path):
    # import image
    image = imageio.imread(image_path)
    
    grayscale_image = grayscale(image)
    
    inverted_image = invert(grayscale_image)
    
    blured_image = blur(inverted_image)
    
    final_image= color_dodge(blured_image, grayscale_image)
    
    plot.imshow(final_image, cmap='gray')
    
    return(final_image)


# method to turn an image grayscale
def grayscale(image): 
    return numpy.dot(image[...,:3], [0.299, 0.587, 0.114])

# method to invert images
def invert(grayscale_image):
    # subtract from 255, as grayscale images are 8 bit images or have a maximum of 256 tones.
    return 255 - grayscale_image

# method to blur image
def blur(image):
    # apply gaussian filter
    # higher sigma means more blur
    return scipy.ndimage.filters.gaussian_filter(image, sigma = 15s)

# method to color dodge (highlights the boldest edges)
def color_dodge(front, back):
    result=front * 255 / (255 - back)
    result[result > 255] = 255 
    result[back == 255] = 255
    return result.astype('uint8')

def main():
    image_path = "https://pbs.twimg.com/profile_images/1260852763963121664/wOfOpfsH_bigger.jpg"
    hand_drawn_image = drawImage(image_path)
    return hand_drawn_image

if __name__ == "__main__":
    main()


