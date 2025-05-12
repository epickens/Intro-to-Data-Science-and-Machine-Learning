# Environment Management

For this project we will primarily use Conda as our environment manager.

## Creating Environments

#### `conda create --name <my-env>`

**Creates a new Conda environment** with a specified name. This is the most basic way to start a new isolated environment.

**Example:**

```bash
# Create a basic environment
conda create --name data-science-project

# Create an environment with Python 3.9
conda create --name data-science-project python=3.9

# Create an environment with specific packages
conda create --name data-science-project python=3.9 pandas numpy matplotlib
```

#### `conda env create -f environment.yml`

**Creates an environment from a YAML file** that specifies the environment name, channels, and required packages. This is ideal for **reproducing environments** across different machines.

**Example:**

```bash
# Create environment from file
conda env create -f environment.yml
```

**Sample environment.yml file:**

```yaml
name: data-science-project
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - pandas=1.4.2
  - numpy=1.22.3
  - matplotlib=3.5.1
  - scikit-learn=1.0.2
  - pip
  - pip:
      - kaggle==1.5.12
      - tensorflow==2.9.0
```

## Switching Environments

#### `conda activate <my-env>`

**Activates a specific Conda environment**, making its packages and settings available in your current terminal session.

**Example:**

```bash
# Activate the data science environment
conda activate data-science-project

# Verify activation (shows environment name in prompt)
# (data-science-project) user@computer:~$

# Check Python version to confirm
python --version
```

## Installing Packages

#### `conda install <package>`

**Installs packages from Conda repositories**. Conda handles dependencies and ensures compatibility with other packages in your environment.

**Example:**

```bash
# Install a single package
conda install pandas

# Install a specific version
conda install pandas=1.4.2

# Install multiple packages
conda install pandas numpy matplotlib

# Install from a specific channel
conda install -c conda-forge xgboost
```

#### `pip install <package>`

**Installs packages from PyPI** (Python Package Index). Use this for packages not available in Conda repositories.

**Example:**

```bash
# Install a single package
pip install kaggle

# Install a specific version
pip install tensorflow==2.9.0

# Install from requirements file
pip install -r requirements.txt

# Install in development mode (for your own packages)
pip install -e .
```

## Exporting Environments

#### `conda env export`

**Exports your current environment** to a YAML file, capturing all installed packages and their exact versions. This is essential for **reproducibility** and sharing your environment with others.

**Example:**

```bash
# Export to standard output
conda env export

# Export to a file
conda env export > environment.yml

# Export without build numbers
conda env export --no-builds > environment.yml

# Export with simplified dependencies (more portable)
conda env export --from-history > environment.yml

# Export only pip-installed packages
pip freeze > requirements.txt
```

**Note:** The `--from-history` flag creates a more portable environment file that only includes packages you explicitly installed, not all dependencies.

## Checking Environment

#### `conda list`

**Lists all packages installed** in the current environment. This helps you verify what's installed and check package versions.

**Example:**

```bash
# List all packages
conda list

# Search for specific packages
conda list pandas

# List packages with their source channel
conda list --show-channel-urls

# Export package list to a text file
conda list --export > package-list.txt
```

**Additional useful commands:**

```bash
# List all environments on your system
conda env list

# Get information about current environment
conda info

# Check if a package is available
conda search pandas
```
