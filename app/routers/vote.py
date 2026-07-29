from fastapi import FastAPI , Response , status , HTTPException ,Depends,APIRouter
from fastapi.routing import APIRoute
from sqlalchemy.orm import Session
from .. import schemas,database,oauth2,models


router = APIRouter(
    prefix = "/votes",
    tags = ['votes']
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote,db: Session = Depends(database.get_db),current_user :int = Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == vote.post_id)
    if post_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {vote.post_id} not found")

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()

    if vote.dir == 1:
        if found_vote :
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"user {current_user.id} has already voted on post {vote.post_id}")
        new_vote = models.Vote(post_id= vote.post_id,user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message" : "sucessfully added vote"}
    else:
        if found_vote is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Vote not found")

        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message" : "susessfully removed vote"}

