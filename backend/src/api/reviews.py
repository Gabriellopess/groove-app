from fastapi import APIRouter, status
from pydantic import BaseModel
from src.db import database as db
from datetime import datetime
from src.service.impl.review_service import ReviewService
from src.schemas.review import ReviewCreateModel, ReviewModel, ReviewList
from starlette.responses import JSONResponse
from fastapi import HTTPException

router = APIRouter()

class Review(BaseModel):
    rating: int
    title: str
    description: str
    author: str
    song: str
    created_at: datetime
    timestamp: datetime
      
def get_reviews_by_song_id(song_id: int):
    """
    Get reviews by song ID.

    Args:
    - song_id (int): The ID of the song to retrieve reviews for.

    Returns:
    - A list of reviews for the specified song.

    Raises:
    - HTTPException(404) if the song is not found.
    """
    reviews = db.get_reviews_by_song_id(song_id) # fazer uma função dessa no db.py
    if not reviews:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
    return reviews

@router.post(
    "/create",
    response_model=ReviewCreateModel,
    response_class=JSONResponse
)
def create_review(review: ReviewCreateModel):
    review_create_response = ReviewService.create_review(review)
    return review_create_response


@router.get(
    "/{review_id}",
    response_model=ReviewModel,
    response_class=JSONResponse
)
def get_review(review_id: str):
    review_get_response = ReviewService.get_review(review_id)
    return review_get_response


@router.get(
    "/",
    response_model=ReviewList,
    response_class=JSONResponse
)
def get_reviews():
    review_list_response = db.get_all_items("reviews")
    return {
        'reviews': review_list_response,
    }


@router.put(
    "/{review_id}",
    response_model=ReviewCreateModel,
    response_class=JSONResponse
)
def edit_review(review_id: str, review: ReviewCreateModel):
    review_edit_response = ReviewService.update_review(review_id, review)
    return review_edit_response

# @router.delete(
#     "/{review_id}",
# )