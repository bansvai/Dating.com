import logging
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, crud
from .database import SessionLocal, engine
from .random_users import RandomUsers
from .schemas import ScrapeUsersRequest

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API endpoint to scrape requested number of users.
@app.post("/scrape_users")
def scrape_users(request: ScrapeUsersRequest, db: Session = Depends(get_db)):
    try:
        users = RandomUsers.generate_users(request.num_users)
        scraped_count = 0
        for user in users:
                user_data = {
                    "first_name": user['name']['first'],
                    "last_name": user['name']['last'],
                    "email": user['email'],
                    "gender": user['gender'],
                    "latitude": user['location']['coordinates']['latitude'],
                    "longitude": user['location']['coordinates']['longitude'],
                }
                crud.create_user(db=db, user_data=user_data)
                scraped_count += 1
        return {"status": "success", "message": f"Scraped and stored {scraped_count} users."}
    except Exception as e:
        logging.error(f"Exception occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))