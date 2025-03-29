# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model has been trained on data from the U.S. Census Bureau to make predictions on income. 
It uses a RandomForestClassifier within a FastAPI deployment pipeline.  

## Intended Use
The purpose of this model is to predict whether an individual earns more or less than $50K per year based on the census data.
It is intended for use by data analysts seeking to understand income distribution patterns across various demographic groups. 

## Training Data
The model was trained on the census dataset provided in data/census.csv file. 

The data includes the following features:
income (Target Variable)
age  
workclass  
fnlwgt  
education  
education-num  
marital-status  
occupation  
relationship  
race  
sex  
capital-gain  
capital-loss  
hours-per-week  
native-country  

## Evaluation Data
The model was evaluated on a test split derived from the original dataset, with approximately 20% of the data reserved to validate its performance.

## Metrics
The model was evaluated using the following metrics:
- **Precision**: 0.7323
- **Recall**: 0.6331 
- **F1 Score**: 0.6791 

## Ethical Considerations
This model was trained on demographic data, which may include societal biases such as income disparities related to race or gender.
These biases can be inadvertently learned by the model and may influence its predictions. 
Users should carefully consider these risks when deploying or interpreting the model's outputs.

## Caveats and Recommendations
Predictive power varies between features. Some features may introduce noise or reflect outdated socioeconomic patterns that can skew predictions. 
Additionally, because the dataset has not been updated to reflect the current year, the model's relevance and accuracy may decline over time.