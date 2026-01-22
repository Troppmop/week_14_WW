import pandas as pd
import numpy as np

from .models import Weapon

def validate_items(file_data) -> bool:
    try:
        for item in file_data:
            Weapon.model_validate(item)
        return True
    except:
        return False
    
def create_dataframe(data):
    df = pd.read_csv(data)
    return df

def export_dict(df:pd.DataFrame) -> list[dict]:
    data = df.to_dict(orient="records")
    return data

def add_risk_level(df: pd.DataFrame) -> pd.DataFrame:
    df['risk_level'] = pd.cut(x=df['range_km'], bins=[0,20,100,300,np.inf], labels=['low','medium','high','extreme'])
    return df
