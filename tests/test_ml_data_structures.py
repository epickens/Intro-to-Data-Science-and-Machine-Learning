import pytest
import math
from dataclasses import dataclass, field

# Import the classes from your assignment file
# Assuming the file is named ml_data_structures.py
from fundamentals.ml_data_structures import Vector, ActivationFunction, ReLU, Sigmoid, Neuron, Layer, Dataset


class TestVector:
    def test_creation(self):
        v = Vector([1.0, 2.0, 3.0])
        assert len(v) == 3
        assert v[0] == 1.0
        assert v[1] == 2.0
        assert v[2] == 3.0

    def test_validation(self):
        with pytest.raises(TypeError):
            Vector("not a list")

        with pytest.raises(TypeError):
            Vector(["a", "b", "c"])

    def test_addition(self):
        v1 = Vector([1.0, 2.0, 3.0])
        v2 = Vector([4.0, 5.0, 6.0])
        result = v1 + v2
        assert result.values == [5.0, 7.0, 9.0]

        # Test error case
        v3 = Vector([1.0, 2.0])
        with pytest.raises(ValueError):
            v1 + v3

    def test_scalar_multiplication(self):
        v = Vector([1.0, 2.0, 3.0])
        result = v * 2.5
        assert result.values == [2.5, 5.0, 7.5]

        with pytest.raises(TypeError):
            v * "not a number"

    def test_dot_product(self):
        v1 = Vector([1.0, 2.0, 3.0])
        v2 = Vector([4.0, 5.0, 6.0])
        assert v1.dot(v2) == 32.0  # 1*4 + 2*5 + 3*6 = 32

        v3 = Vector([1.0, 2.0])
        with pytest.raises(ValueError):
            v1.dot(v3)

    def test_magnitude(self):
        v = Vector([3.0, 4.0])
        assert v.magnitude() == 5.0  # sqrt(3^2 + 4^2) = 5


class TestActivationFunctions:
    def test_relu(self):
        relu = ReLU()
        assert relu(5.0) == 5.0
        assert relu(-3.0) == 0.0
        assert relu(0.0) == 0.0

        # Test derivative
        assert relu.derivative(5.0) == 1.0
        assert relu.derivative(-3.0) == 0.0
        assert relu.derivative(0.0) == 0.0  # Technically undefined, but we define it as 0

    def test_sigmoid(self):
        sigmoid = Sigmoid()
        assert sigmoid(0.0) == 0.5
        assert abs(sigmoid(10.0) - 0.9999) < 1e-4
        assert abs(sigmoid(-10.0) - 0.0001) < 1e-4

        # Test derivative
        assert abs(sigmoid.derivative(0.0) - 0.25) < 1e-6  # sigmoid(0)*(1-sigmoid(0)) = 0.5*0.5 = 0.25


class TestNeuron:
    def test_creation(self):
        weights = Vector([0.1, 0.2, 0.3])
        bias = 0.5
        activation = ReLU()
        neuron = Neuron(weights, bias, activation)

        assert neuron.weights is weights
        assert neuron.bias == bias
        assert neuron.activation is activation

    def test_forward(self):
        weights = Vector([0.1, 0.2, 0.3])
        bias = 0.5
        activation = ReLU()
        neuron = Neuron(weights, bias, activation)

        inputs = Vector([1.0, 2.0, 3.0])
        # Expected: ReLU(0.1*1 + 0.2*2 + 0.3*3 + 0.5) = ReLU(1.6) = 1.6
        assert neuron.forward(inputs) == 1.6

        # Test with negative result before activation
        weights = Vector([-0.1, -0.2, -0.3])
        neuron = Neuron(weights, -0.5, activation)
        # Expected: ReLU(-0.1*1 - 0.2*2 - 0.3*3 - 0.5) = ReLU(-1.6) = 0
        assert neuron.forward(inputs) == 0.0

        # Test dimension mismatch
        with pytest.raises(ValueError):
            neuron.forward(Vector([1.0, 2.0]))


class TestLayer:
    def test_creation(self):
        neurons = [
            Neuron(Vector([0.1, 0.2]), 0.1, ReLU()),
            Neuron(Vector([0.3, 0.4]), 0.2, Sigmoid())
        ]
        layer = Layer(neurons)
        assert layer.neurons is neurons

    def test_forward(self):
        neurons = [
            Neuron(Vector([0.1, 0.2]), 0.1, ReLU()),
            Neuron(Vector([0.3, 0.4]), 0.2, Sigmoid())
        ]
        layer = Layer(neurons)

        inputs = Vector([1.0, 2.0])
        outputs = layer.forward(inputs)

        # Expected outputs:
        # Neuron 1: ReLU(0.1*1 + 0.2*2 + 0.1) = ReLU(0.6) = 0.6
        # Neuron 2: Sigmoid(0.3*1 + 0.4*2 + 0.2) = Sigmoid(1.3) ≈ 0.786
        assert outputs[0] == 0.6
        assert abs(outputs[1] - 0.786) < 1e-3


class TestDataset:
    def test_creation(self):
        features = [Vector([1.0, 2.0]), Vector([3.0, 4.0])]
        labels = [0.0, 1.0]
        dataset = Dataset(features, labels, "Test Dataset")

        assert dataset.features is features
        assert dataset.labels is labels
        assert dataset.name == "Test Dataset"
        assert len(dataset.feature_names) == 2  # Should auto-generate feature names

    def test_validation(self):
        features = [Vector([1.0, 2.0]), Vector([3.0, 4.0])]
        labels = [0.0]  # One label missing

        with pytest.raises(ValueError):
            Dataset(features, labels)

    def test_getitem(self):
        features = [Vector([1.0, 2.0]), Vector([3.0, 4.0])]
        labels = [0.0, 1.0]
        dataset = Dataset(features, labels)

        feature, label = dataset[1]
        assert feature is features[1]
        assert label == labels[1]

    def test_split(self):
        features = [Vector([1.0, 2.0]), Vector([3.0, 4.0]), Vector([5.0, 6.0]), Vector([7.0, 8.0])]
        labels = [0.0, 1.0, 0.0, 1.0]
        dataset = Dataset(features, labels, "Test Dataset")

        train_data, test_data = dataset.split(0.75)

        assert len(train_data) == 3
        assert len(test_data) == 1
        assert train_data.name == "Test Dataset_train"
        assert test_data.name == "Test Dataset_test"

        # Test invalid ratio
        with pytest.raises(ValueError):
            dataset.split(1.5)

