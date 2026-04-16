import pandas as pd
from sklearn.model_selections import train_text_split
from sklearn.feature_extracion.text import TfidfVectorize
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("train.csv")
