import cv2 as cv2
import numpy as np

def open_image(path, type):
    image_buffer = cv2.imread(path)
    if (type=='color'):
        image = cv2.cvtColor(image_buffer,cv2.COLOR_BGR2RGB)
    else:
        image = cv2.cvtColor(image_buffer,cv2.COLOR_BGR2GRAY)
    
    return image

def add_noise(mu, sigma, image):
    noise =np.random.normal(mu,sigma,image.shape)
    noisy_image = image + noise
    return noisy_image
    

if __name__ == "__main__":
    main()