(Working with the `diamonds.csv` Dataset in Pandas) In this book's data-science chapters, you'll work extensively with datasets, many in CV format. You'll frequently use pandas to load datasets and prepare their data for use in machine-learning studies. Datasets are available for almost anything you'd want to study. There are numerous dataset repositories from which you can download datasets in CSV and other formats. 
In this chapter, we mentioned: https://vincentarelbundock.github.io/Rdatasets/datasets.html and https://github.com/awesomedata/awesome-public-datasets
- The Kaggle competition site:  https://www.kaggle.com/datasets?filetype=CSV has approximately 11,000 datasets with over 7500 in CSV format.
- The U.S. government's data. gov site: https://catalog.data.gov/dataset?res_format=CSV&_res_format_limit=0 has over 300,000 datasets with approximately 19,000 in CSV format.

In this exercise, you'll use the diamonds dataset to perform tasks similar to those you saw in the Intro to Data Science section. This dataset is available as diamonds.csv from various sources, including the Kaggle and Rdatasets sites listed above. The dataset contains information on 53,940 diamonds, including each diamond's carats, cut, color, clar-ity, depth, table (flat top surface), price and x, y and z measurements. The Kaggle site's web page for this dataset describes each column's content.

Perform the following tasks to study and analyze the diamonds dataset:
- a) Download diamonds.csv from one of the dataset repositories.
- b) Load the dataset into a pandas DataFrame with the following statement, which uses the first column of each record as the row index: `df = pd. read_sv('diamonds.csv', index_col=0)`
- c) Display the first seven rows of the DataFrame.
- d) Display the last seven rows of the DataFrame.
- e) Use the DataFrame method describe (which looks only at the numerical columns) to calculate the descriptive statistics for the numerical columns `carat`, `depth`, `table`, `price`, `x`, `y` and `z`.
- f) Use Series method describe to calculate the descriptive statistics for the categorical data (text) columns: `cut`, `color` and `clarity`.
- g) What are the unique category values (use the Series method `unique`)?
- h) Pandas has many built-in graphing capabilities. Execute the `%matplotib` magic to enable `Matplotlib` support in `IPython`. Then, to view histograms of each numerical data column, call your DataFrame's hist method.


