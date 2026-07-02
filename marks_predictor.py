import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [1,2,3,4,5,6,7,8],
    "Marks": [25,35,45,55,65,75,85,95]
}

df = pd.DataFrame(data)

print(df)

X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()

model.fit(X,y)

hours=float(input("Enter study hours: "))

prediction=model.predict([[hours]])

print("Predicted Marks:",prediction[0])