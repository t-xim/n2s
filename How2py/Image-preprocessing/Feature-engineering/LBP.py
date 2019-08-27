# Taken from Nabin's notebook
class LocalBinaryPatterns:
	def __init__(self, numPoints, radius):
		# store the number of points and radius
		self.numPoints = numPoints
		self.radius = radius
 
	def LBPfeatures(self, image, eps=1e-7):
		# compute the Local Binary Pattern representation
		# of the image, and then use the LBP representation
		# to build the histogram of patterns
		lbp = feature.local_binary_pattern(image, self.numPoints,
			self.radius, method="uniform")
    # Form the histogram
		(hist, _) = np.histogram(lbp.ravel(),
			bins=np.arange(0, self.numPoints + 3),
			range=(0, self.numPoints + 2))
 
		# normalize the histogram
		hist = hist.astype("float")
		hist /= (hist.sum() + eps)
 
		# return the histogram of Local Binary Patterns
		return hist
    
# Appending
desc = LocalBinaryPatterns(24, 8)
LBP_data_train = []
LBP_label_train = []

for img_index in range (len(X)):
    img = X[img_index]
    histo = desc.LBPfeatures(img)
    
    LBP_label_train.append(y[img_index])
    LBP_data_train.append(histo) 
