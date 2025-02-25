# Step 01:
Remove the existing ```dipcc``` environment and all of its dependencies 

```conda remove --name 'dipcc' --all```

# Step 02:

Recreate ```dipcc``` from the ```.yml``` file in this repo. <br> After the -f flag please provide the path to the file.

```conda env create -f /path/to/your/environment.yml```

# Step 03:
Activate ```dipcc```

```conda activate dipcc```