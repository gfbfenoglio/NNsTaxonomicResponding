# Copyright 2017 Giorgia Fenoglio
#
# This file is part of NNsTaxonomicResponding.
#
# NNsTaxonomicResponding is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# NNsTaxonomicResponding is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NNsTaxonomicResponding.  If not, see <http://www.gnu.org/licenses/>.

from matplotlib import pyplot as plt
import numpy as np
from colour import Color
from SOM import SOM
import os
import math
import random

fInput = 'input10classes/VisualInputTrainingSet.csv'
N = 1000
lenExample = 2048
NumXClass = 10

def printToFileCSV(prototipi,file):
  """
    print of the prototypes in file.csv
    prototipi: dictionary of the prototypes to print
  """

  f = open(file,'w')

  # stampa su file
  for k in prototipi.keys():
    st = k+','
    for v in prototipi[k]:
      st += str(v)+','
    st = st[0:-1]
    f.write(st+'\n')

  f.close()

def showSom(som,inputs,nameInputs,count,title):
  """
    build of the map with the color associated to the different classes
  """
  print('costruzione mappa '+title)
  mapped = som.map_vects(inputs)
  image_grid = np.zeros(shape=(20,30,3))
  plt.figure(count)
  plt.imshow(image_grid)
  plt.title(title)
  inputClass = nameInputs[0]

  # color generation
  classColor = list()
  ## for 100 classes
  # for i in range(100):
  #   print(i)
  #   c = Color(rgb=(random.random(), random.random(), random.random()))
  #   classColor.append(str(c))
  ## for 10 classes:
  classColor = ['white','red','blue','cyan','yellow','green','gray','brown','orange','magenta']

  iColor = 0

  lenExample = len(inputs[0])
  print(lenExample)

  print(inputClass+' -- '+classColor[iColor])

  for i, m in enumerate(mapped):
    if nameInputs[i] != inputClass:
      inputClass = nameInputs[i]
      iColor = iColor + 1
      print(inputClass+' -- '+classColor[iColor])


    plt.text(m[1], m[0], str('____'), ha='center', va='center', color=classColor[iColor], alpha=0.5,
          bbox=dict(facecolor=classColor[iColor], alpha=0.6, lw=0, boxstyle='round4'))

  ## draw of the prototypes on the map
  # for k in prototipi.keys():
  #     [BMUi, BMUpos] = som.get_BMU(prototipi[k])
  #     plt.text(BMUpos[1], BMUpos[0], str(k), ha='center', va='center',
  #             bbox=dict(facecolor='white', alpha=0.9, lw=0))
  plt.draw()
  plt.show()
  return plt


def classPrototype(inputs,nameInputs):
  #build the prototypes of the different classes
  protClass = dict()
  nameS = list(set(nameInputs))
  temp = np.array(inputs)

  i = 0
  for name in nameS:
    protClass[name] = np.mean(temp[i:i+NumXClass][:],axis=0)
    i = i + NumXClass

  #printToFileCSV(protClass,'prototipi.csv')
  return protClass



if __name__ == '__main__':
  #read the inputs from the file fInput and show the SOM with the BMUs of each input

  inputs = np.zeros(shape=(N,lenExample))
  nameInputs = list()

  # read the inputs
  with open(fInput, 'r') as inp:
      i = 0
      for line in inp:
        if len(line)>2:
          inputs[i] = (np.array(line.split(',')[1:])).astype(np.float)
          nameInputs.append((line.split(',')[0]).split('/')[6])
          i = i+1

  prototipi = classPrototype(inputs,nameInputs)

  #get the 20x30 SOM or train a new one (if the folder does not contain the model)
  som = SOM(20, 30, lenExample, checkpoint_dir= './VisualModel10classes/', n_iterations=20,sigma=4.0)

  loaded = som.restore_trained()
  if not loaded:
    som.train(inputs)

  for k in range(len(nameInputs)):
    nameInputs[k] = nameInputs[k].split('_')[0]

  #shows the SOM
  showSom(som,inputs,nameInputs,1,'Visual map')
