# Download OpenBUGs at www.openbugs.net/w/Downloads
# Loading BRUGs
library(BRugs)

# Setting wd
setwd("C:/Users/Home/Dropbox/Mixi/08 - Study/UTS/37458-Adv-Bayesian-Methods/Week 3 - Lab 1/Proper Extensions")

# Monte Carlo sample sizes
nBurnin <- 10^5
nIter   <- 10^5
nThin   <- 1

# Probability for x_2 ~ B(1, probx2)
probx2 <- 0.62

#  List of distributions (?) + initial values of said distributions
allData    <- list(probx2=probx2)
initValues <- list(list(x1 = 0, x2 = 0))

BRugsFit(modelFile = "BobTheDAGModel.txt",
         data      = allData,
         inits     = initValues,
         nBurnin   = nBurnin,
         nIter     = nIter,
         nThin     = nThin)
