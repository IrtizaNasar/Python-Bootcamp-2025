# Python-Bootcamp-2025
This is a basic Introduction to Python for the Diploma and Graduate Diploma in Creative Computing students at the UAL Creative Computing Institute.

Three core areas of foucs:
1. <b>Programming Fundamentals:</b> <br>Variables, data types, control structures, and functions
2. <b>Data Analysis:</b> <br>Introduction to Pandas library for handling and visualizing datasets
3. <b>Interactive Applications:</b> <br>Building user interfaces with Python GUI frameworks
<br></br>

## Set-up Instructions 

#### Note: 
You will need to have [VS Code](https://code.visualstudio.com/download) Installed for these sessions. 
<br></br>
#### Step 01: Install Conda <br>
Download and install [Anacoda](https://www.anaconda.com/download/success)
<br>

#### Step 02: Open the Terminal
Once you have installed Conda, open your terminal. On Windows, you can use the Anaconda Prompt, while on macOS and Linux, you can use the standard terminal.

#### Step 3: Create a New Conda Environment 

To create a new Conda environment with a specific Python version (3.12.2 in this case), use the following command:

```
conda create --name dipcc python=3.12.2
```

<!-- Note: You can replace "dipcc" with the name you want for your environment, and replace 3.12.2 with the Python version you want to use. -->

#### Step 4: Activate the Conda Environment 

After creating the environment, you need to activate it using the following command:

```
conda activate dipcc
```

#### Step 5: Install Jupyter 

```
conda install jupyter 
```

#### Step 6: Install VSCode Jupyter Extension
Open VS Code and navigate to the Extensions panel (MacOS - Cmd+Shift+X).<br>```Search for "Jupyter"``` and install the official Microsoft Jupyter extension. This enables you to create, edit, and run Jupyter notebooks directly within VS Code, eliminating the need to launch a separate browser instance.

#### Step 6: Start a new notebook 
1. In VS Code, create a new file with the ```.ipynb``` extension (e.g., python_basics.ipynb)
2. VS Code will automatically recognize it as a Jupyter notebook and open it in notebook mode
3. The notebook interface will appear with an empty cell, ready for your code or markdown input <br>

Note: You can also use the Command Palette (MacOS - Cmd+Shift+X) and search for "Create New Jupyter Notebook" as an alternative method.

#### Step 7: Check your environemnt

```
import os
print(os.environ['CONDA_DEFAULT_ENV'])
```

That cell above should output the text "dipcc" as this the name of the envrionment we created above.