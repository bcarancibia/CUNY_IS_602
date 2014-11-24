#Ben Arancibia
#Week 8 Assignment
#November 4th, 2014
 
import scipy.ndimage as ndimage
import scipy.misc as misc
import numpy as np

dir = '/users/bcarancibia/CUNY_IS_602/Lesson8'
images = ['circles.png', 'objects.png', 'peppers.png']
#file import
for i in range(len(images)):
    print "-" * 30
    print images[i][0:-4]
    raw = misc.imread(dir + images[i])
    
    img = ndimage.gaussian_filter(raw, 2) 
    #gaussian http://en.wikipedia.org/wiki/Gaussian_filter
    #http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.ndimage.filters.gaussian_filter.html
    thresh = img > img.mean()
    
    lbls = ndimage.label(thresh)
    nrobj = lbls[1]
    print "Object count: " + str(nrobj) #count

    
    centers = ndimage.center_of_mass(thresh, lbls[0], np.arange(1, nrobj + 1, 1)) #centers
    for j in range(len(centers)):
        print "Object number" + str(j+1) + "center:" #print
        print "x = " + str(centers[j][0])
        print "y = " + str(centers[j][1])
