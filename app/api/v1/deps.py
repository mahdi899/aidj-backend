# Place for dependencies (auth, db sessions, etc.)
from fastapi import Depends
from app.db.session import get_db
def with_db(db = Depends(get_db)):
    return db
