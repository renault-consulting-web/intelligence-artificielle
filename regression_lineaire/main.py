# On choisit un modèle de régression linéaire
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import pandas as pd

reg = LinearRegression()

df = pd.read_csv('age_vs_poids_vs_taille_vs_sexe.csv')

# Les variables prédictives
X = df[['sexe','age','taille']]

# La variable cible, le poids
y = df.poids

# On entraine ce modèle sur les données avec la méthode fit
reg.fit(X, y)

# et on obtient directement un score
#print(reg.score(X,y))

# ainsi que les coefficients a,b,c de la régression linéaire
#print(reg.coef_)

#poids = reg.predict(np.array([[0,150,153]]))
#print(poids)

# Lewis
#poids = reg.predict(np.array([[0,125,146]]))

# Naëlle
#poids = reg.predict(np.array([[1,164,165]]))

#print(poids)
y_pred = reg.predict(X)

# metrics
mse = mean_squared_error(y, y_pred)
print(mse)
print(mean_absolute_error(y, y_pred))
print(mean_absolute_percentage_error(y, y_pred))

# Root Mean Squared Error
print(np.sqrt(mse))