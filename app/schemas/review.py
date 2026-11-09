from pydantic import BaseModel, Field

class ReviewCreate(BaseModel):
    product_id: int
    rating: int = Field(ge=1, le=5)
    text: str

class ReviewResponse(ReviewCreate):
    id: int

class ReviewUpdate(BaseModel):
    rating: int | None = Field(default=None,ge=1, le=5)
    text: str | None = None