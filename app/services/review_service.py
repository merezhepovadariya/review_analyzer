from app.schemas.review import ReviewCreate, ReviewResponse, ReviewUpdate

reviews = []

def create_review(review: ReviewCreate):
    review_data = review.model_dump()
    review_data["id"] = len(reviews)+1
    reviews.append(review_data)
    return review_data

def get_review(review_id: int) -> dict | None:
    for review in reviews:
        if review["id"] == review_id:
            return review
    return None

def get_reviews() -> list[dict]:
    return reviews

def delete_review(review_id: int) -> bool:
    for review in reviews:
        if review["id"] == review_id:
            reviews.remove(review)
            return True
    return False

def update_review(review_id: int, review: ReviewUpdate) -> bool:
    update_data = review.model_dump(exclude_unset=True)
    for review in reviews:
        if review["id"] == review_id:
            review.update(update_data)
            return True
    return False