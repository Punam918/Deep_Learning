# -*- coding: utf-8 -*-
"""Log_Loss_Function.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mPFZT2ykwbthGe1hV5DXRoet_RYn5qBU

**The Log Loss activation function, also known as the Binary Cross-Entropy activation function, is commonly used in the output layer of binary classification models to calculate the loss.**
"""

import numpy as np

class LogLossActivation:
    def __call__(self, z):
        return 1 / (1 + np.exp(-z))
    def gradient(self, z):
        sig_z = self.__call__(z)
        return sig_z * (1 - sig_z)

logloss_activation = LogLossActivation()

# Compute the activation for a given input z
z = np.array([0.5, -0.3, 0.8])
activation = logloss_activation(z)
print("Activation:", activation)

# Compute the gradient of the activation function for the same input z
gradient = logloss_activation.gradient(z)
print("Gradient:", gradient)