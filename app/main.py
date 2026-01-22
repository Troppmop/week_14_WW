from fastapi import FastAPI, File, UploadFile
from io import StringIO

from .utils import *

app = FastAPI()

@app.get('/')
def root():
    return {"status":"healthy"}

@app.post('/upload')
def upload_csv(file: UploadFile = File(media_type='multipart/form-data')):
    contents = file.file.read()
    s = str(contents,'utf-8')
    data = StringIO(s)
    
    #to add custom pandas function calls here
    dataframe = create_dataframe(data)
    dataframe = add_risk_level(dataframe)
    dataframe_dict = export_dict(dataframe)
    #to add pydantic validation function calls here
    valid_data = validate_items(data)
    print(dataframe_dict)


    data.close()
    file.file.close()
    return {"file uploaded":file.filename,
            "valid data": valid_data,
            "data": "dataframe_dict"}