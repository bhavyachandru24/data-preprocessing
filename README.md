# Data-preprocessing

**Model overview**
The objective of this model is to predict the target variable using structured input features after proper data preprocessing. The model is designed to learn patterns from historical data and generate accurate predictions on unseen data.

Depending on the problem statement, the model can perform:

Regression (for continuous target variables such as price or salary)

Classification (for categorical target variables such as performance level or category)

**Dataset Description**

The dataset contains a mix of numerical and categorical features along with a target variable. It includes:

Numerical features (e.g., Age, Salary, Experience)

Categorical features (e.g., Department, City)

Target variable (e.g., Performance_Score)

The raw dataset may contain:

Missing values

Categorical data

Outliers

Features on different scales

**Preprocessing Steps Performed**
1. Handling Missing Values

Numerical columns were filled using the median value.

Categorical columns were filled using the most frequent value (mode).

This ensures no null values remain in the dataset.

2. Outlier Detection and Removal

The Interquartile Range (IQR) method was applied to numerical features.

Extreme values outside acceptable bounds were removed.

This improves model stability and reduces noise.

3. Encoding Categorical Variables

Categorical columns were converted into numerical form using encoding techniques.

Label Encoding or OneHot Encoding was applied depending on the use case.

4. Feature Scaling

StandardScaler was used to normalize numerical features.

This ensures all features are on a comparable scale.

5. Train-Test Split

The dataset was split into:

80% Training data

20% Testing data

A fixed random state was used for reproducibility.

**Output**

After preprocessing:

The dataset contains no missing values.

Categorical variables are encoded.

Numerical features are scaled.

Outliers are handled.

The cleaned dataset is saved as cleaned_dataset.csv.

**Requirements**

The following Python libraries are required:

pandas

numpy

scikit-learn

Ensure these libraries are installed in your Python environment before running the script.

**How to Run the Code**

Download or copy the project files into a folder.

Place the dataset file (for example, preprocessing.csv) in the same directory as the preprocessing script file (for example, preprocess.py).

Open the project folder in a Python-supported environment such as VS Code or PyCharm.

Open the preprocessing script file.

Run the script.

After execution, the program will:

Load the raw dataset

Perform data cleaning

Apply encoding and scaling

Split the dataset

Save the cleaned dataset

The cleaned dataset will be saved in the project directory.
