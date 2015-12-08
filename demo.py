from scipy.misc import imresize
import graphcut
#from array import array
from PIL import Image
from pylab import *
import numpy as np
import scipy.ndimage

im = Image.open('images.jpg')
figure()
im.show()

im = imresize(im,0.2,interp='bilinear')
size = im.shape[:2]
print "size is {}".format(size)

# add two rectangular training regions
labels = zeros(size)
print labels
labels[3:18,3:18] = -1
labels[-18:-3,-18:-3] = 1

# create graph
g = graphcut.build_bayes_graph(im,labels,kappa=10)
print g

# cut the graph
res = graphcut.cut_graph(g,size)


figure()
graphcut.show_labeling(im,labels)

figure()
imshow(res)
gray()
axis('off')

show()
