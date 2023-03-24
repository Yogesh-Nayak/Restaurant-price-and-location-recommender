import numpy as np
import pandas as pd
import json
from flask import Flask, redirect, url_for, render_template, request
import pickle

#Database
df = pd.read_csv(r"/home/yogesh/Downloads/Food Delivery ML/Completed_work/processed_data.csv")
normal_form = pd.read_csv(r"/home/yogesh/Downloads/Food Delivery ML/Completed_work/normal_form.csv")
restaurant_data = pd.read_csv(r"/home/yogesh/Downloads/Food Delivery ML/Completed_work/restaurant_data.csv")
df_json = json.loads(df.to_json(orient='records'))


cuisines = df['cusine'].unique()
cuisine_dic = {}
for i in range(len(cuisines)):
    cuisine_dic[cuisines[i].lower().strip()] = i

location=df['Location'].unique()
location_dic={}
for i in range(len(location)):
    location_dic[location[i].lower().strip()] = i

# Create flask app
app = Flask(__name__)
reg_model = pickle.load(open("reg_model.pkl", "rb"))
clas_model = pickle.load(open("clas_model.pkl", "rb"))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/partners')
def partners():
    return render_template('partners.html')


@app.route('/inputs')
def inputs():
    return render_template('inputs.html')


@app.route('/conclusion')
def conclusion():
    return render_template('conclusion.html')


@app.route("/predict", methods = ["POST","GET"])
def predict():
    if request.method == "POST":
        a = request.form.get("cusine")
        b = request.form.get("price")
        c = request.form.get("Location")
        d = request.form.get("rating")

    cuisine = str(a).lower().strip()
    price = int(b)
    location = str(c).lower().strip()
    rating = float(d)

    #getting encoded values from dictionary
    en_c = cuisine_dic[cuisine]
    en_l = location_dic[location]

    #Regression Model
    arr = [[int(en_c), int(en_l), rating]]
    prediction = reg_model.predict(arr)
    predict1 = round(prediction[0], 2)

    #Classification Model
    arr1 = [[int(en_c), price, rating]]
    prediction1 = clas_model.predict(arr1)
    predict2 = list(location_dic.keys())[list(location_dic.values()).index(prediction1)]

    #getting aggregation result
    def pop_rest(cusine, location):
        popular_cus = ''
        popular_cusine = normal_form[normal_form['Location'] == location].groupby('cusine')[
            'cusine'].count().sort_values(ascending=False)
        popular_cusine = popular_cusine[popular_cusine == popular_cusine.max()].index.tolist()
        if len(popular_cusine) == 1:
            popular_cus = popular_cusine[0]
        else:
            for i in popular_cusine:
                if i not in popular_cusine[-1]:
                    popular_cus += i
                    popular_cus += ','
                else:
                    popular_cus += i

        popular_restaurant_cusine = restaurant_data[
            (restaurant_data['cusine'].str.contains(cusine)) & (restaurant_data['Location'] == location)].sort_values(
            ['review', 'rating'], ascending=False).iloc[0][0]

        avg_price = restaurant_data['price'][restaurant_data['Location'] == location]

        most_popular_restaurant = restaurant_data[restaurant_data['Location'] == location].sort_values(
            ['review', 'rating'], ascending=False)

        return [round(avg_price.mean(), 0), popular_cus, most_popular_restaurant.iloc[0][0],
                most_popular_restaurant.iloc[0][4], popular_restaurant_cusine]

    avg_price,pop_cuisine,mpop_rest,serve,rest_popcui=pop_rest(cuisine,location)

    return render_template("Recommendation.html", predict1="{}".format(int(predict1)), predict2="{}".format(predict2.title()),
                           average_text="{}".format(int(avg_price)),
                           popular_text="{}".format(pop_cuisine.title()), rest_text="{}".format(mpop_rest.title()),
                           serves_text="{}".format(serve.title()), poprest_text="{}".format(rest_popcui.title()))


if __name__ == "__main__":
    app.run(debug=True)
