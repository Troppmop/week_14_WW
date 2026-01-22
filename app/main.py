from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get('/')
def root():
    return {"status":"healthy"}

@app.post('/upload')
def upload_csv(file: UploadFile = File(media_type='multipart/form-data')):
    #to add custom pandas functions here
    
    return {"file uploaded":file.filename}