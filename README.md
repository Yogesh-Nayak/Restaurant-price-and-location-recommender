# Price and Location Recommender

## Aim:
The aim of the project is to predict the optimal price for a given cuisine and determine the best location to sell that cuisine. This is achieved by implementing a machine-learning model using the scraped data from Zomato.
<br>
## Description:
The data obtained from Zomato is likely to require cleaning and pre-processing before being used for analysis. This may involve handling missing values, removing duplicates, standardizing formats, and addressing any inconsistencies or errors in the data. The cleaning process is performed using the Pandas library, which provides efficient data manipulation and transformation capabilities.
<br>

## Data exploration and Analysis:
After cleaning the data, exploratory data analysis (EDA) is performed to gain insights and understand the characteristics of the dataset. This involves calculating summary statistics, examining distributions, identifying trends or patterns, and exploring relationships between variables. The EDA phase helps in identifying any data quirks or issues that need to be addressed before modeling.
<br>

## Working of Project:
The project involves implementing a Flask website that takes three inputs from the user: Price, Location, and Cuisine. The machine learning model utilizes a Random Forest Regressor to predict the optimal price for the given cuisine. Additionally, a Random Forest Classifier is employed to determine the best location to sell the cuisine based on the input variables.
<br>

## Website:
### Home Page
![First page](https://github.com/Yogesh-Nayak/Restaurant-price-and-location-recommender/assets/79314126/a4475063-b9ce-49d1-9aa1-64a7d60e00d8)
<br><br>

### Tech stack page
![second page](https://github.com/Yogesh-Nayak/Restaurant-price-and-location-recommender/assets/79314126/21299cdc-b074-43d9-8824-f76fd6a8b342)
<br><br>

### Team members page
![third page](https://github.com/Yogesh-Nayak/Restaurant-price-and-location-recommender/assets/79314126/0cf3f56d-d28e-4aec-b662-d879f92ac02f)
<br><br>

### User input page
![fourth page](https://github.com/Yogesh-Nayak/Restaurant-price-and-location-recommender/assets/79314126/5877dd40-8772-41dd-9a82-d7ba2b1f7bab)
<br><br>

### Recommendation page
![sixth page](https://github.com/Yogesh-Nayak/Restaurant-price-and-location-recommender/assets/79314126/8e17e3ba-02d3-413b-b687-fa9ea49658ba)

### Conclusion page

![image](https://github.com/Yogesh-Nayak/Restaurant-price-and-location-recommender/assets/79314126/bdcad00e-97c4-4429-8723-176d0fbcd172)



<br><br>

## Findings:
At each step of the analysis, various findings can be observed. During data cleaning and pre-processing, missing values may be imputed or dropped, ensuring the data is ready for further analysis. In the data exploration phase, insights regarding the distribution of prices, popular cuisines, and shared locations can be derived. These findings assist in understanding the dataset and identifying any patterns or trends that can be leveraged for prediction.
<br>

## Conclusion:
  - We were able scrape the zomato website successfully and were able to extract around 5000 records.
  - The dataset which was recovered after webscraping were very less correlated to the target label.
  - Number of features were low and was not enough to make proper prediction model.
  - Due to less features and lower correlation between the features and the label, the model was having very low accuracy.
  - If there were more number of features and higher co-linearity between the features and the target label, the model would may had higher accuracy.
<br>

## Challenges Faced:
There are several limitations and challenges that arised during the project. Some potential challenges include:

- Data quality and consistency: The scraped data from Zomato contained errors, missing values, or inconsistencies that affected the accuracy of the analysis and model predictions.
- Feature engineering: The available features were not sufficient to capture all the relevant information for predicting price and location accurately. Additional feature engineering techniques may be required to improve the model's performance.
- Overfitting: The machine learning models may be prone to overfitting if the training data is not representative of the real-world scenarios. Careful model selection and evaluation techniques, such as cross-validation, can help mitigate this issue.
- Scalability: Depending on the size of the dataset and the complexity of the models, scalability can be a challenge. Efficient implementation and optimization techniques may be needed to handle larger datasets or more complex algorithms.






