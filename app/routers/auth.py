from fastapi import FastAPI,Depends,APIRouter,HTTPException,Response,status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database,schemas,models,utility,oauth2

router = APIRouter(tags=['Authentication'])

#create toke 
#return token

@router.post('/login',response_model=schemas.Token)
def get_user(user_credentials : OAuth2PasswordRequestForm= Depends(),db:Session = Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
     
    if not user:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid credentials")
    
    if not utility.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    access_token = oauth2.create_access_token(data={"user_id" : user.id})
    return {"access_token" : access_token, "token_type" :"bearer"}