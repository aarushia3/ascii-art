from PIL import Image
import numpy as np
import os

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_PIXEL_VALUE = 255

def getPixelMatrix(imagePath):
    '''
    Return a numpy array containing RGB data for each pixel of the image at given image path

    Arguments: valid image path
    '''
    im = Image.open(imagePath)
    imArray = np.asarray(im).astype(int)
    print("Successfully loaded image into array!")
    print("Pixel array dimensions: ", imArray.shape, ", dtype: ",imArray.dtype)
    return imArray

def getBrightnessMatrix(imArray, algo = "average"):
    '''
    Returns a numpy array with each pixel of the given array (that has 3 RGB values) reduced to a single dimension.
    You can choose the algorithm you like. The default is average.

    Arguments: numpy array with RGB data of each pixel (shape: [height, width, 3]), 
    optional: algorithm name (\"average\", \"max_min\" or \"luminosity\").
    '''
    reducedIm = np.zeros_like(imArray[:, :, 0])
    for i in range(imArray.shape[0]):
        for j in range(imArray.shape[1]):
            if (algo == "average"):
                reducedIm[i][j] = (imArray[i][j][0] + imArray[i][j][1] + imArray[i][j][2])/3
            elif (algo == "max_min"):
                reducedIm[i][j] = (max(imArray) + min(imArray))/2
            elif (algo == "luminosity"):
                reducedIm[i][j] = 0.21*imArray[i][j][0] + 0.72*imArray[i][j][1] + 0.07*imArray[i][j][2]
            else:
                raise Exception("Unrecognixed algo_name: ", algo,". \nPlease try \"average\", \"max_min\" or \"luminosity\".")
    print("Successfully constructed brightness array!")
    print("Brightness Array Dimensions: ", reducedIm.shape, ", dtype: ",reducedIm.dtype)
    return reducedIm

def normalizeMatrix(reducedIm):
    '''
    Returns a scaled matrix such that each value corresponds to an index in the string ASCII_CHARS.

    Arguments: numpy array (shape: [height, width])
    '''
    normIm = np.empty(reducedIm.shape, dtype=int)
    for i in range(reducedIm.shape[0]):
        for j in range(reducedIm.shape[1]):
            normIm[i][j] = int(min((reducedIm[i][j] / 255 * len(ASCII_CHARS)), len(ASCII_CHARS) - 1))
    print("Successfully normalized!")
    print("Normalized Array Dimensions: ", normIm.shape, ", dtype: ",normIm.dtype)
    return normIm

def invertMatrix(normIm):
    '''
    Returns an inverted matrix, given a normalized matrix. Each pixel `p` is replaced by 255 - `p`

    Arguments: numpy array (shape: [height, width])
    '''
    print("Successfully inverted the matrix!")
    return (255 - normIm)

def convertToAscii(normIm):
    '''
    Returns a matrix containing ASCII characters corresponding to each pixel.

    Arguments: numpy array (shape: [height, width])
    '''
    charArray = np.empty(normIm.shape, dtype = str)
    for i in range(normIm.shape[0]):
        for j in range(normIm.shape[1]):
            charArray[i][j] = ASCII_CHARS[normIm[i][j]]
    print("Successfully built ASCII Array!")
    print("ASCII Array Dimensions: ", charArray.shape, ", dtype: ",charArray.dtype)
    return charArray


inputPath = input("Enter path of image relative to current directory: ")
if not os.path.exists(inputPath):
    raise Exception("Invalid File Path")
outputPath = input("Enter path to save output: ")
if not os.path.exists(outputPath):
    raise Exception("Invalid File Path")
pixelMatrix = getPixelMatrix(inputPath)
brightnessMatrix = getBrightnessMatrix(pixelMatrix)
normMatrix = normalizeMatrix(brightnessMatrix)
asCIIMatrix = convertToAscii(normMatrix)
np.savetxt(outputPath, asCIIMatrix, delimiter='', fmt='%s')