from pydantic import BaseModel
  
class ScrapeUsersRequest(BaseModel):
    num_users: int