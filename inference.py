import joblib
import pandas as pd

MODEL_PATH="models/snv_svm_linear.joblib"

model=joblib.load(MODEL_PATH)

def make_prediction(file):

    df = pd.read_csv(
    file,
    sep=";",
    header=0
    )

    if df.empty:
        raise ValueError("The file is empty.")
    
    first_column=df.columns[0].strip().lower()

    if first_column!="wavelength":
        raise ValueError("The first column must be 'wavelength'.")
    
    if len(df.columns)<2:
        raise ValueError("The file must contain at least one sample.")
    
    sample_names=list(df.columns[1:])

    for sample in sample_names:
        if not str(sample).strip():
            raise ValueError("All samples must have a name.")
    wavelength=pd.to_numeric(df.iloc[:,0],errors="coerce")

    if wavelength.isna().any():
        raise ValueError("The wavelength column contains invalid values.")
    data=df.iloc[:,1:].apply(pd.to_numeric,errors="coerce")

    if data.isna().any().any():
        raise ValueError("Spectral data must contain only numeric values.")
    
    X=data.values.T

    predictions=model.predict(X)
    results=[]

    for sample,prediction in zip(sample_names,predictions):
        results.append({"sample":sample,"class":prediction})
    return results
