import os
import Tkinter
import tkFileDialog
import matplotlib.pyplot as pyplot
import scipy.ndimage as ndimage
import skimage.filter as skif
from PIL import Image, ImageTk

def loadimage(imagefile, title):
    """Loads the specified image or if not found, prompts the user for the file."""

    # If the hardcoded path doesn't exist, then prompt for a file.
    if(not os.path.isfile(imagefile)):
        root=Tkinter.Tk()
        root.withdraw()
        imagefile = tkFileDialog.askopenfilename(parent=root, title=title)

    theImage = ndimage.imread(imagefile)
    return theImage

def processimage(theImage, name, thresholdMethod, block_size = 3):


    if(thresholdMethod == "otsu"):
        # Apply thresholding
        img1GlobalThres = skif.threshold_otsu(theImage)
        img1GlobalCut = theImage > img1GlobalThres
    else:
        img1GlobalCut = skif.threshold_adaptive(theImage, block_size)

    # Count the objects
    labeled,nr_objects = ndimage.label(img1GlobalCut)

    # Determine center points
    centers = ndimage.center_of_mass(img1GlobalCut, labeled, range(1, nr_objects + 1, 1))

    # Visualize what we found by the above functions
    fig = pyplot.figure(figsize=(8,4))
    fig.subplots_adjust(hspace=0.05, wspace=0.05)

    ax1 = fig.add_subplot(131)
    ax1.imshow(theImage)
    ax1.xaxis.set_visible(False)
    ax1.yaxis.set_visible(False)

    ax3 = fig.add_subplot(132)
    ax3.imshow(img1GlobalCut)
    ax3.xaxis.set_visible(False)
    ax3.yaxis.set_visible(False)

    ax4 = fig.add_subplot(133)
    ax4.imshow(theImage)
    for p in centers:
        ax4.scatter(p[1], p[0], s=80, facecolor='none', edgecolor='#FF7400')
    #ax4.set_xlim(0, theImage.shape[0])
    #ax4.set_ylim(0, theImage.shape[1])
    ax4.xaxis.set_visible(False)
    ax4.yaxis.set_visible(False)

    savePath = '/users/bcarancibia/CUNY_IS_602/Lesson8/{0}.png'.format(name)
    fig.savefig(savePath, bbox_inches='tight')

    # Print to console the results
    print ("*** {0} ***".format(name))
    print ("# of Objects: {0}".format(nr_objects))
    print ("Local Maxima:")
    for i in range(0, len(centers), 1):
        print (" {0}".format(centers[i]))

    os.startfile(savePath)

def main():
    """Our main function for unit testing purposes."""
    img1 = loadimage("", "Select Circles File")
    processimage(img1, "firstImg", "otsu")

    img2 = loadimage("", "Select Objects File")
    processimage(img2, "secondImg", "adaptive", 999)

    img3 = loadimage("", "Select Peppers File")
    processimage(img3, "thirdImg", "adaptive", 1000)

# This is the main of the program.
if __name__ == "__main__":
    main()
