(main.py)
1. FastAPI server
2. POST /upload route for csv file
    Method: POST 
    Path: /upload 
    Content-Type: multipart/form-data 
    Field name: file 
    File type: CSV
commit:
    feat (fastapi): server + POST /upload

(models.py)
3. BaseModel Weapon
    check pdf for specifications
commit:
    feat (pydantic): Weapon basemodel

(utils.py)
4. Validation loop using .model_validate()
commit:
    feat (pydantic): BaseModel validation

5. Convert to pandas dataframe
6. add risk_level column based on range_km
    low – טווח עד 20 ק״מ
    medium – טווח 21–100 ק״מ
    high – טווח 101–300 ק״מ
    extreme – טווח מעל 300 ק״מ
commit: 
    feat (pandas): dataframe + risk_column added

7. replace missing values in manufacturer to 'Unknown'
commit:
    feat (pandas): standardized manufacturer data 

(db.py)
8. make connection with mysql database (using placeholder .env values)
9. run mysql database using image in docker compose
10. initialize database with CREATE IF NOT EXISTS
commit:
    feat (mysql.connector): connected and initialized database
