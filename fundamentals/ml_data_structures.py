"""
Assignment: ML Data Structures
This assignment focuses on implementing core ML data structures using Python classes and dataclasses.
"""

import math
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Union, Callable


@dataclass
class Vector:
    """
    A vector class representing a mathematical vector with basic operations.
    """
    values: List[float]

    def __post_init__(self):
        # TODO: Validate that values is a list and all elements are numeric
        pass

    def __len__(self):
        # TODO: Return the length of the vector
        pass

    def __getitem__(self, idx):
        # TODO: Return the element at the given index
        pass

    def __add__(self, other):
        # TODO: Implement vector addition
        # Raise ValueError if vectors have different lengths
        pass

    def __mul__(self, scalar):
        # TODO: Implement scalar multiplication
        # Raise TypeError if scalar is not a number
        pass

    def dot(self, other):
        """Compute dot product with another vector"""
        # TODO: Implement dot product
        # Raise ValueError if vectors have different lengths
        pass

    def magnitude(self):
        """Compute the magnitude (L2 norm) of the vector"""
        # TODO: Implement magnitude calculation
        pass


class ActivationFunction:
    """Base class for activation functions used in neural networks"""

    def __call__(self, x: float) -> float:
        """Apply the activation function"""
        raise NotImplementedError("Subclasses must implement __call__")

    def derivative(self, x: float) -> float:
        """Compute the derivative of the activation function"""
        raise NotImplementedError("Subclasses must implement derivative")


class ReLU(ActivationFunction):
    """Rectified Linear Unit activation function"""

    def __call__(self, x: float) -> float:
        # TODO: Implement ReLU function
        pass

    def derivative(self, x: float) -> float:
        # TODO: Implement ReLU derivative
        pass


class Sigmoid(ActivationFunction):
    """Sigmoid activation function"""

    def __call__(self, x: float) -> float:
        # TODO: Implement sigmoid function
        # Hint: Consider numerical stability for large negative values
        pass

    def derivative(self, x: float) -> float:
        # TODO: Implement sigmoid derivative
        pass


@dataclass
class Neuron:
    """
    A single neuron in a neural network with weights, bias and an activation function.
    """
    weights: Vector
    bias: float
    activation: ActivationFunction

    def forward(self, inputs: Vector) -> float:
        """
        Compute the output of the neuron for the given inputs.
        """
        # TODO: Implement forward pass
        # 1. Check if input dimension matches weights dimension
        # 2. Compute weighted sum
        # 3. Apply activation function and return result
        pass


@dataclass
class Layer:
    """
    A layer of neurons in a neural network.
    """
    neurons: List[Neuron]

    def forward(self, inputs: Vector) -> Vector:
        """
        Compute the outputs of all neurons in the layer.
        """
        # TODO: Implement forward pass through all neurons
        # Return a Vector containing all neuron outputs
        pass


@dataclass
class Dataset:
    """
    A simple dataset class for machine learning.
    """
    features: List[Vector]
    labels: List[Union[float, Vector]]
    name: str = "Unnamed Dataset"
    description: str = ""
    feature_names: List[str] = field(default_factory=list)

    def __post_init__(self):
        # TODO: Validate that features and labels have the same length
        # TODO: Generate default feature names if not provided
        pass

    def __len__(self):
        # TODO: Return the number of samples in the dataset
        pass

    def __getitem__(self, idx):
        # TODO: Return the feature vector and label at the given index
        pass

    def split(self, train_ratio: float = 0.8) -> Tuple['Dataset', 'Dataset']:
        """Split dataset into training and testing sets"""
        # TODO: Implement dataset splitting
        # 1. Validate train_ratio is between 0 and 1
        # 2. Split features and labels according to the ratio
        # 3. Create and return two new Dataset objects
        pass

