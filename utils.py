import numpy as np
import pandas as pd

def data_pre_process(dicto):
    # Dictionary to DataFrame
    df = pd.DataFrame(dicto, index=[0])

    # Converting Gender values.
    df['Gender'] = df['Gender'].replace(to_replace=['Female', 'Male'], value=[0,1])
    df['MultipleLines'] = df['MultipleLines'].replace(to_replace=['No', 'Yes', 'No phone'], value=[0,1,2])
    df['InternetService'] = df['InternetService'].replace(to_replace=['DSL', 'Fiber', 'No'], value=[0,1,2])
    df['Contract'] = df['Contract'].replace(to_replace=['Month', 'One year', 'Two year'], value=[0,1,2])
    df['PaymentMethod'] = df['PaymentMethod'].replace(to_replace=['Electronic', 'Mail', 'Bank', 'Credit'], value=[0,1,2,3])
    
    # Converting one set of values.
    for attr in ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'SeniorCitizen']:
        df[attr] = df[attr].replace(to_replace=['No', 'Yes'], value=[0,1])
    
    # Converting other values.
    for attr in ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']:
        df[attr] = df[attr].replace(to_replace=['No', 'Yes', 'No internet'], value=[0,1,2])
    
    df['Tenure'] = df['Tenure'].astype('float')
    df['MonthlyCharges'] = df['MonthlyCharges'].astype('float')
    df['TotalCharges'] = df['TotalCharges'].astype('float')    
    return df.iloc[0,:].values

