# Aim:
---
The aim of the project is to predict the optimal price for a given cuisine and determine the best location to sell that cuisine. This is achieved by implementing a machine learning model using the scraped data from Zomato.

# Description:
---
The data obtained from Zomato is likely to require cleaning and pre-processing before being used for analysis. This may involve handling missing values, removing duplicates, standardizing formats, and addressing any inconsistencies or errors in the data. The cleaning process is performed using the Pandas library, which provides efficient data manipulation and transformation capabilities.

# Data exploration and Analysis:
---
After cleaning the data, exploratory data analysis (EDA) is performed to gain insights and understand the characteristics of the dataset. This involves calculating summary statistics, examining distributions, identifying trends or patterns, and exploring relationships between variables. The EDA phase helps in identifying any data quirks or issues that need to be addressed before modeling.

# Working of Project:
---
The project involves implementing a Flask website that takes three inputs from the user: Price, Location, and Cuisine. The machine learning model utilizes a Random Forest Regressor to predict the optimal price for the given cuisine. Additionally, a Random Forest Classifier is employed to determine the best location to sell the cuisine based on the input variables.

# Findings:
---

At each step of the analysis, various findings can be observed. During data cleaning and pre-processing, missing values may be imputed or dropped, ensuring the data is ready for further analysis. In the data exploration phase, insights regarding the distribution of prices, popular cuisines, and shared locations can be derived. These findings assist in understanding the dataset and identifying any patterns or trends that can be leveraged for prediction.

# Conclusion:
---
The accuracy of the models was not up to the mark. There was less collinearity between the target variable and features. Data was biased as most of the cuisine was available in Whitefield Location. 
Addressing these below limitations and challenges requires careful data handling, model selection, and rigorous evaluation to ensure the project's success. Regular monitoring and updates to the models based on new data can also help maintain their accuracy over time.


# Challenges Faced:
---
There are several limitations and challenges that may arise during the project. Some potential challenges include:

- Data quality and consistency: The scraped data from Zomato contained errors, missing values, or inconsistencies that affected the accuracy of the analysis and model predictions.
- Feature engineering: The available features were not sufficient to capture all the relevant information for predicting price and location accurately. Additional feature engineering techniques may be required to improve the model's performance.
- Overfitting: The machine learning models may be prone to overfitting if the training data is not representative of the real-world scenarios. Careful model selection and evaluation techniques, such as cross-validation, can help mitigate this issue.
- Scalability: Depending on the size of the dataset and the complexity of the models, scalability can be a challenge. Efficient implementation and optimization techniques may be needed to handle larger datasets or more complex algorithms.






