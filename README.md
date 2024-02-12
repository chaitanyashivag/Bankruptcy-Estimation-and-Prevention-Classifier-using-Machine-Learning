# Bankruptcy-Estimation-and-Prevention-Classifier-using-Machine-Learning

For Testing Purposes, a main dataset from Kaggle is downloaded having 6 input features and 1 target variable.

# Objective

To develop a predictive model using Logistic Regression, Decision Trees, Random Forests, K Nearest Neighbours, Support Vector Machines to classify whether a given company will go bankrupt or not based on various risk factors as input features.

# Prerequisites

Install following packages:

pip install numpy 
pip install pandas 
pip install sklearn
pip install keras 
pip install seaborn

# Data Processing

Used a Label Encoder to convert the target variable into 0 and 1

# Exploratory Data Analysis 

Following visualization graphs are selected for exploratory data analysis

1. Histograms
2. Box Plots
3. Pair plots
4. Heat maps
5. Count plots
6. Cross tab plot

# Model Building

Following 5 models are selected and are built to solve this classification problem 

1. Logistic Regression
2. Random Forest Classifier
3. K Nearest Neighbors Classifier
4. Support Vector Machines
5. Decision Tree Classifier

We will be trying different machine learning models one by one. Defining models are much easier. A single line of code can define our model. And, in the same way, a single line of code can fit the model on our data.

We can also tune these models by selecting different optimized parameters. But, if the accuracy is better even with less parameter tuning then — no need to make it complex.

# Deploying the model

We are using streamlit for deploying our best model i.e Decision Tree Classifier as it is showing maximum accuracy. We are exporting the model through pickle format

# Conclusion

We arrived at a 99 % accuracy in our bankruptcy prediction  and successfully deployed it through streamlit so as to use it in realtime.
