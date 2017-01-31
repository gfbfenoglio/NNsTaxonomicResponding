# NNsTaxonomicResponding
A neural network model for taxonomic responding with realistic visual inputs

## Abstract
In this work we propose a neural network model for taxonomic responding with realistic visual inputs. The model learns word-object associations, and generalizes those associations to objects belonging to the same category. It takes visual inputs from the ImageNet dataset, and simplified acoustic stimuli. It is made of a convolutional deep neural network processing the visual input, a visual and acoustic self-organizing maps that topologically organize the visual and acoustic inputs respectively, a set of Hebbian connections connecting the visual and acoustic self-organizing maps. 

## Code
The DCNN folder.py contains the files that handle the Deep Convolutional Neural Network InceptionNet:
 * ExtractActivations contains the functions used to extract the activation of a specific layer from the net when an image is presented to the net; utility functions are used to evaluate the weights.
 * RetrainSoftmax.py contains the functions used to retrain the InceptionNet classifier in order to focus on a subset of classes.
* ClusterExperiments.py contains the functions used to conduct the cluster experiments on the representations, that is the activations of the last level.


