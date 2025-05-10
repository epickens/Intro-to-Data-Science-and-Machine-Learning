# Intro-to-Data-Science-and-Machine-Learning

Materials for an introductory course in data science and machine learning

## Setup

#### Clone the repository

```
git clone https://github.com/epickens/Intro-to-Data-Science-and-Machine-Learning.git
cd Intro-to-Data-Science-and-Machine-Learning
```

#### Create a Conda environment.

```
conda env create -f environment.yml
```

#### Activate the environment

```
conda activate introML
```

## Project Structure

Each directory in this project contains a number of files that you should complete on your own. The `tests` directory contains a series of tests that will allow you to check your work.

## Testing Your Work

After setting up the environment, you can run the tests with `pytest`. To run all available tests, simply run

```
pytest
```

To run a specific test use

```
pytest tests/example_test.py
```

## Acknowledgements

This repository is inspired by Sasha Rush's fantastic [MiniTorch](https://minitorch.github.io) project and the associated Cornell course. I have taken the liberty of using `operators.py` and the associated tests in the initial commit to this repository. I expect the our projects to diverge in all future commits, but the inspiration will remain nonetheless.
