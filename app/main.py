from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get('/')
def root():
    return {"status":"healthy"}

@app.post('/upload')
def upload_csv(file: UploadFile = File(media_type='multipart/form-data')):
    
    #to add pydantic validation function calls here

    #to add custom pandas function calls here
    
    return {"file uploaded":file.filename}