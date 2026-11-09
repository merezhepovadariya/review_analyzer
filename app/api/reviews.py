from fastapi import APIRouter, HTTPException
from app.schemas.review import ReviewCreate, ReviewResponse, ReviewUpdate
from app.services.review_service import create_review as save_review
from app.services.review_service import get_review as get_review_from_service
from app.services.review_service import get_reviews as get_reviews_from_service
from app.services.review_service import delete_review as delete_reviews_from_service
from app.services.review_service import update_review as update_reviews_from_service

router = APIRouter(prefix="/reviews", tags=["Reviews"])

@router.get("/", response_model=list[ReviewResponse])
def get_reviews():
    return get_reviews_from_service()

@router.post("/", response_model=ReviewResponse)
def create_review(review: ReviewResponse):
    return save_review(review)

@router.get("/{review_id}", response_model=ReviewResponse)
def get_review(review_id: int):
    review = get_review_from_service(review_id)

    if review is None:
        return HTTPException(
            status_code=404,
            detail="Review not found"
        )
    return review

@router.delete("/{review_id}")
def delete_review(review_id: int):
    deleted = delete_reviews_from_service(review_id)
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )
    return {"message": "Review is deleted"}

@router.patch("/{review_id}", response_model=ReviewResponse)
def update_review(review_id: int, review: ReviewUpdate):
    updated = update_reviews_from_service(review_id, review)
    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Review not updated"
        )
    return get_review_from_service(review_id)
