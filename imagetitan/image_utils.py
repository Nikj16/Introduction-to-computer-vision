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

def zero_padding(image, pad):
    pad_image = np.zeros((image.shape[0]+2*pad, image.shape[1]+ 2*pad))
    pad_image[pad: -pad, pad: -pad] = image
    return pad_image


def check_kernel(kernel):
    k_size = kernel.shape[0]
    if (k_size!=kernel.shape[1]):
        print("please enter a square matrix with an odd number size")
        return False
    else:
        if(k_size%2==0):
            print("please enter a square matrix with odd size")
            return False 


    return True


def correlate_kernel(image, kernel, convolve=False):
    if convolve:
        kernel = np.flipud(kernel)
        kernel = np.fliplr(kernel)
    #some key variables to consider:
    k_size = kernel.shape[0]-1
    k_mid = int(np.floor(k_size/2)) # index of the middle pixel. floor because numpy indexing starts at 0.
    k_span = int(k_size - k_mid) # span is the number of pixels the kernel "spans" from the center pixel
    print("k_span is ", k_span)
    img_height, img_width = image.shape
    
    
    #padding the image with zeros so we can perform convolution on border pixels
    image = zero_padding(image, k_span)
    print("image height is:", img_height, "& image with is:", img_width)
    kernel_sum = np.sum(np.concatenate(kernel))
    result = np.zeros_like(image)
    
    #perform the actual convolution
    for i in range(k_span, img_width + k_span):
        for j in range( k_span, img_height + k_span):
            #roi is the region of interest
            roi =image[j-k_span:j+ k_span+1,i-k_span:i+k_span+1]
#             roi =image[k_span:-k_span,k_span:-k_span]
            #kernel multiplication along with normalization:
            result[j,i] = np.sum(np.concatenate(roi * kernel/kernel_sum))
    
    
    return result[k_span: -k_span, k_span: - k_span]





if __name__ == "__main__":
    main()