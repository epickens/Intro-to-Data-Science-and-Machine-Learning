# Command Line Basics

This tutorials is designed to help explain the most fundamental command line operations. In a later tutorials we will cover more advanced features.

In particular, this tutorial exists to help you get settled into the world of the terminal. Using the terminal can be an intimidating experience - even for experienced developers - so we're going to take things slow as we begin to climb the steepest part of the learning curve.

## Navigating at the Command Line Level

#### `ls`

**Lists the contents of a directory**. This is one of the most frequently used commands when navigating the file system.

**Example:**

```bash
# List files and directories in current directory
ls

# List with detailed information (permissions, size, date)
ls -l

# List all files (including hidden ones that start with .)
ls -a

# List files with human-readable sizes
ls -lh

# List files sorted by modification time (newest first)
ls -lt
```

#### `cd`

**Changes your current directory** to a specified location. This is how you move around the file system.

**Example:**

```bash
# Move to a specific directory
cd Documents

# Move to a subdirectory
cd Documents/projects

# Move up one directory level
cd ..

# Move to your home directory
cd ~

# Move to the previous directory you were in
cd -

# Move to root directory
cd /
```

#### `pwd`

**Prints the working directory**, showing your current location in the file system. Useful when you need to confirm where you are.

**Example:**

```bash
# Show current directory path
pwd
# Output example: /home/username/Documents/data-science-project
```

#### `type`

**Shows information about a command**, whether it's a built-in shell command, an alias, or an executable file.

**Example:**

```bash
# Check what type of command 'ls' is
type ls
# Output: ls is aliased to `ls --color=auto'

# Check what type of command 'cd' is
type cd
# Output: cd is a shell builtin
```

#### `which`

**Locates the executable file** associated with a given command by searching through the PATH environment variable.

**Example:**

```bash
# Find the location of Python
which python
# Output example: /usr/bin/python

# Find the location of pip
which pip
# Output example: /home/username/miniconda3/bin/pip
```

## Creating Files and Directories

#### `touch`

**Creates an empty file** or updates the timestamp of an existing file.

**Example:**

```bash
# Create a new empty file
touch new_file.txt

# Create multiple files at once
touch file1.py file2.py file3.py

# Update the timestamp of an existing file
touch existing_file.csv
```

#### `mkdir`

**Creates a new directory** (folder) in the file system.

**Example:**

```bash
# Create a new directory
mkdir data

# Create nested directories (with parent directories if they don't exist)
mkdir -p projects/data-analysis/raw-data

# Create multiple directories at once
mkdir data scripts notebooks
```

#### `mv`

**Moves or renames files and directories**. This command can both relocate files and change their names.

**Example:**

```bash
# Rename a file
mv old_name.txt new_name.txt

# Move a file to another directory
mv file.csv data/

# Move and rename at the same time
mv old_file.py scripts/new_file.py

# Move multiple files to a directory
mv file1.txt file2.txt file3.txt backup/
```

#### `cp`

**Copies files and directories** from one location to another.

**Example:**

```bash
# Copy a file
cp original.py copy.py

# Copy a file to another directory
cp data.csv backup/

# Copy with the same name to another directory
cp report.pdf ~/Documents/

# Copy a directory and its contents recursively
cp -r scripts/ backup/scripts/
```

#### `rm`

**Removes (deletes) files and directories**. **Be careful with this command as deleted files cannot be easily recovered.**

**Example:**

```bash
# Remove a file
rm unwanted_file.txt

# Remove multiple files
rm file1.txt file2.txt

# Remove a directory and all its contents (use with caution!)
rm -r old_project/

# Force removal without confirmation
rm -f sensitive_data.csv

# Remove directory and contents without confirmation (very dangerous!)
rm -rf directory_to_delete/
```

## Peaking Into Files

#### `echo`

**Displays text or variable values** to the terminal. Also useful for creating simple files.

**Example:**

```bash
# Print text to terminal
echo "Hello, Data Science!"

# Create a file with content
echo "import pandas as pd" > script.py

# Append text to an existing file
echo "import numpy as np" >> script.py

# Display environment variable
echo $PATH
```

#### `cat`

**Concatenates and displays file contents**. Good for viewing small files or combining files.

**Example:**

```bash
# Display file contents
cat data.csv

# Display multiple files
cat header.txt data.txt

# Combine files into a new file
cat file1.csv file2.csv > combined.csv

# Display with line numbers
cat -n script.py
```

#### `head`

**Displays the beginning (first 10 lines by default) of a file**. Useful for previewing large files.

**Example:**

```bash
# Show first 10 lines
head large_dataset.csv

# Show first 5 lines
head -n 5 large_dataset.csv

# Show first 20 lines of multiple files
head -n 20 file1.txt file2.txt
```

#### `tail`

**Displays the end (last 10 lines by default) of a file**. Useful for viewing recent log entries or the end of large files.

**Example:**

```bash
# Show last 10 lines
tail large_dataset.csv

# Show last 5 lines
tail -n 5 large_dataset.csv

# Follow a file as it grows (useful for log files)
tail -f app.log
```

#### `grep`

**Searches for patterns in files** and prints lines that match. Essential for finding specific information in files.

**Example:**

```bash
# Find lines containing a word
grep "error" log.txt

# Case-insensitive search
grep -i "warning" log.txt

# Show line numbers with matches
grep -n "import" *.py

# Recursive search through directories
grep -r "TODO" ./project/

# Show only the matching part
grep -o "data\[.*\]" script.py
```

#### `wc`

**Counts lines, words, and characters** in a file. Useful for quick file statistics.

**Example:**

```bash
# Get full count (lines, words, characters)
wc report.txt

# Count only lines
wc -l data.csv

# Count words
wc -w document.txt

# Count characters
wc -c script.py

# Count bytes
wc -c binary_file
```

## Interacting With the Outside World

#### `curl`

**Transfers data to or from a server**, supporting numerous protocols. Essential for downloading files or interacting with APIs.

**Example:**

```bash
# Download a file
curl -O https://example.com/data.csv

# Download and save with a different name
curl -o renamed_data.csv https://example.com/data.csv

# Make a GET request to an API
curl https://api.example.com/data

# Make a POST request with data
curl -X POST -d "name=value" https://api.example.com/submit

# Include HTTP headers
curl -H "Authorization: Bearer token123" https://api.example.com/secure

# Follow redirects
curl -L https://redirecting-site.com
```

## CLI Tools

#### `ripgrep (rg)`

**Ripgrep** is a modern, blazing-fast search tool that recursively searches directories for a regex pattern. It's designed as a faster alternative to tools like grep, with better defaults for code searching.

**Installation:**

```bash
# Ubuntu/Debian
sudo apt-get install ripgrep

# macOS with Homebrew
brew install ripgrep
```

**Example:**

```bash
# Basic search for a pattern in all files
rg "def"

# Search only Python files
rg "import pandas" -t py

# Case-insensitive search
rg -i "error"

# Search with regular expressions
rg "data\.[a-z]+\("

# Show context (3 lines before and after match)
rg -C 3 "TODO"

# Search only in specific directories
rg "api_key" src/ config/

# Exclude specific directories
rg "def" --glob '!tests/*'

# Show only filenames of matches
rg -l "def"

# Count matches per file
rg -c "test" tests/

# Search hidden files too (by default ripgrep ignores hidden files/directories)
rg --hidden "secret"
```

**Key features of ripgrep:**

- **Extremely fast** - often 10x faster than grep
- **Respects .gitignore** rules by default
- **Automatically skips binary files**
- **Searches compressed files** with the `-z` flag
- **Unicode support**
- **Colorized output** for better readability
- **Smart case** searching with `-S` (case-insensitive if pattern is all lowercase)

**Advanced usage:**

```bash
# Find files with multiple patterns (AND logic)
rg "user" | rg "authentication"

# Replace text (preview only)
rg "old_function" --replace "new_function"

# Actually perform replacement
rg "old_function" --replace "new_function" -i

# Search for whole words only
rg -w "log"

# Fixed strings (no regex interpretation)
rg -F "data.frame[1]"

# Show line numbers
rg -n "TODO"

# Follow symbolic links
rg --follow "config"
```

For most tasks, I default to using `rg` over `grep`.
