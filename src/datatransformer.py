import joblib as jb
from sklearn.preprocessing import StandardScaler

Scalar = StandardScaler()

def data_transform(x):
    print("Data Transformation ...")
    Scalar.fit(x)
    t_data = Scalar.transform(x)
    jb.dump(Scalar, "models/scalar.pkl")
    return t_data