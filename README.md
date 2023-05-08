# Rename Files
This repository contains a Python script that renames a set of image files in a specified directory for use in AI applications.

This repository contains three Python scripts that can be used to manage machine learning data.

The first script, renameFiles.py, takes a directory location as input and renames all the files inside it. This can be useful when organizing training, validation, and testing datasets, as it is often easier to work with numbered files. The script can handle large numbers of files and automates the renaming process, saving time and effort.

The second script, rename-sub-dir.py, is used to rename labeled data. If you have a directory with thousands of labeled images stored in subdirectories, this script can be used to rename the images inside each subdirectory. This can help to keep your data organized and make it easier to work with during machine learning experiments.

The third script, unlabel.py, can be used to remove labels from labeled training data. If you have thousands of labeled images stored in subdirectories and need to remove the labels, this script automates the process, saving time and effort.

Each script comes with clear instructions for use and can be easily customized to suit your specific needs. These scripts can help to streamline the data management process and make it easier to work with machine learning data.

## Usage

1. rename-sub-dir.py
This script is used to rename labeled images inside subdirectories. Follow the steps below to use this script:
  * Open the script and change the path variable to the path of the directory containing the subdirectories with labeled images.
  * Run the script by executing the command "python rename-sub-dir.py" in your terminal.
  * The script will rename the labeled images inside each subdirectory with a unique numerical filename.

2. renameFiles.py
 This script is used to rename files in a directory to a unique numerical filename. Follow the steps below to use this script:
  * Open the script and change the path variable to the path of the directory containing the files to be renamed.
  * Run the script by executing the command "python renameFiles.py" in your terminal.
  * The script will rename the files in the directory with a unique numerical filename.
  * 
3. unlabel.py
 This script is used to remove labels from labeled images stored in subdirectories. Follow the steps below to use this script:
  * Open the script and change the source_dir and dest_dir variables to the path of the directory containing the labeled images and the path of the destination directory respectively.
  * Run the script by executing the command "python unlabel.py" in your terminal.
  * The script will remove the labels from the labeled images and move them to the destination directory.

## REQUIREMENTS:

* os
* shutil
You can install these libraries using the pip package manager by running the following command in your terminal:
pip install os shutil

