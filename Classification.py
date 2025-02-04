import streamlit as st  # Importing Streamlit for building the web app
import pandas as pd  # Importing Pandas for handling dataframes
from sklearn.datasets import load_iris  # Importing the Iris dataset from scikit-learn
from sklearn.ensemble import RandomForestClassifier  # Importing RandomForestClassifier for model training

# Caching the data loading function to improve performance and avoid reloading on every interaction
@st.cache_data
def load_data():
    iris = load_iris()  # Loading the Iris dataset
    df = pd.DataFrame(iris.data, columns=iris.feature_names)  # Creating a dataframe with feature names
    df['species'] = iris.target  # Adding the target variable (species) to the dataframe
    return df, iris.target_names  # Returning the dataframe and target names (species names)

# Loading the dataset and target names
df, target_names = load_data()

# Initializing and training the RandomForestClassifier model
model = RandomForestClassifier()  # Creating an instance of RandomForestClassifier
model.fit(df.iloc[:, :-1], df['species'])  # Training the model using all features except the target column

# Sidebar inputs for user-defined feature values
st.sidebar.title("Input Features")  # Sidebar title for input feature selection

# Sliders to allow the user to select values for each feature
sepal_length = st.sidebar.slider("Sepal length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

# Storing the selected input feature values into a list
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# Making a prediction using the trained model
prediction = model.predict(input_data)  # Predicting the species based on user input
predicted_species = target_names[prediction[0]]  # Mapping the predicted class label to the actual species name

# Displaying the prediction result
st.write("Prediction")  # Output section header
st.write(f"The predicted species is: {predicted_species}")  # Displaying the predicted species name


# To run the app, use the following command in the terminal:
#  streamlit run classification.py