from sklearn.preprocessing import OrdinalEncoder
import joblib as jb

OR = OrdinalEncoder()

def data_Encoder(df):
    print("Data Encoded")
    df["Genre"] = OR.fit_transform(df[["Genre"]])
    jb.dump(OR, "encoder.pkl")
    return df
