# Algorithm-Time-Testing-Based-on-Characterisitics
# What is this project about? 
This project attempts to test algorithms based on the size and nature (sorted or unsorted) of the dataset.

# Which algorithms were tested?
* Merge Sort
* Quick Sort
* Insertion Sort
* Bubble Sort
* Selection Sort

# Why is it useful?
* Time complexity is only an estimate, and as can be observed from this project, is not always the best representation of which algorithm would perform better for certain dataset characteristics
* Algorithmic efficiency has not been measured for the different sizes of datasets in such a manner
* For certain algorithms such as selection sort, the impact of whether the dataset is sorted or unsorted is very minor
* Algorithms of similar time complexities can perform differently

# How can I test the algorithms?
* Download the zip folders 'sorted data.zip' and 'unsorted data.zip', and unzip the folders
# Using a linux terminal (or WSL on windows):
* cd into the 'sorted data' folder or 'unsorted data' folder
* Run the generatedata bash file in both the sorted and unsorted folders
* This will prepare csv files for each algorithm, within their respective folders, for the specific size of the dataset

# Languages used:
* C++ for algorithm implementation
* Bash to automate the testing

# This project is the work of Aditya Pujara, email: adityapujara42002@gmail.com
