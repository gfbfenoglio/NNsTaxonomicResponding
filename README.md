# NNsTaxonomicResponding
A neural network model for taxonomic responding with realistic visual inputs.
The code proposed is referred to the master thesis contained in the folder Documents.

## Abstract of the thesis
In this work we propose a neural network model for taxonomic responding with realistic visual inputs. The model learns word-object associations, and generalizes those associations to objects belonging to the same category. It takes visual inputs from the ImageNet dataset, and simplified acoustic stimuli. It is made of a convolutional deep neural network processing the visual input, a visual and acoustic self-organizing maps that topologically organize the visual and acoustic inputs respectively, a set of Hebbian connections connecting the visual and acoustic self-organizing maps. 

## Folders
The DCNN folder contains the files that handle the Deep Convolutional Neural Network InceptionNet:
 * ExtractActivations.py contains the functions used to extract the activation of a specific layer from the net when an image is presented to the net; utility functions are used to evaluate the weights.
 * RetrainSoftmax.py contains the functions used to retrain the InceptionNet classifier in order to focus on a subset of classes.
 * ClusterExperiments.py contains the functions used to conduct the cluster experiments on the representations, that is the activations of the last level.

The SOMs folder contains the files that handle the Self Organizing Maps:
 * SOM.py contains the functions used to create and train the SOMs.
 * SOMTest.py contains the functions used to handle the SOMs of interest.
 * wordLearningTest.py contains the functions used to train an test the Hebbian Connections.

The alghoritms in the folders DCNN and SOMs work on data (trained models, images, representations extracted from the DCNN) can be found here: [data](https://www.dropbox.com/sh/81o2dmkigupp7k6/AADKWlKaaYQoO6CNNhLOA_-ra?dl=0).
