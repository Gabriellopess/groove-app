from fastapi.testclient import TestClient
from src.db import database as db
from datetime import datetime, timezone
from unittest.mock import patch, MagicMock
from src.service.impl.review_service import ReviewService
from src.service.impl.song_service import SongService


def test_add_review(client: TestClient):
    review_create_data = {
        "title": "Great Song",
        "description": "This song is fantastic. I loved it!",
        "rating": 5,
        "author": "Reviewer Name",
        "song": "id",
    }

    mock_response = review_create_data.copy()
    ReviewService.create_review = MagicMock(return_value=mock_response)

    # Adjust the endpoint as needed
    response = client.post("/reviews/create", json=review_create_data)

# Your existing test code...


def test_get_reviews(client: TestClient):

    mock_get_all_items = [
        {
            "title": "Review 1",
            "description": "Description 1",
            "rating": 5,
            "author": "Author 1",
            "song": "Song 1",
        },
        {
            "title": "Review 2",
            "description": "Description 2",
            "rating": 4,
            "author": "Author 2",
            "song": "Song 2",
        },
        {
            "title": "Review 3",
            "description": "Description 3",
            "rating": 3,
            "author": "Author 3",
            "song": "Song 3",
        },
    ]

    ReviewService.get_reviews = MagicMock(return_value=mock_get_all_items)
    response = client.get("/reviews")

    assert response.status_code == 200
    assert response.json() == mock_get_all_items


def test_get_reviews(client: TestClient):

    mock_get_all_items = [
        {
            "title": "Review 1",
            "description": "Description 1",
            "rating": 5,
            "author": "Author 1",
            "song": "Song 1",
            # "timestamp": datetime(2021, 8, 15, 21, 34, 56, tzinfo=timezone.utc),
        },
        {
            "title": "Review 2",
            "description": "Description 2",
            "rating": 4,
            "author": "Author 2",
            "song": "Song 2",
            # "timestamp": datetime(2023, 2, 14, 11, 12, 13, tzinfo=timezone.utc),
        },
        {
            "title": "Review 3",
            "description": "Description 3",
            "rating": 3,
            "author": "Author 3",
            "song": "Song 3",
            # "timestamp": datetime(2022, 5, 19, 19, 15, 22, tzinfo=timezone.utc),
        },
    ]

    ReviewService.get_reviews = MagicMock(return_value=mock_get_all_items)
    response = client.get("/reviews")

    assert response.status_code == 200
    assert response.json() == {"reviews": [
        {
            "title": "Review 1",
            "description": "Description 1",
            "rating": 5,
            "author": "Author 1",
            "song": "Song 1",
        },
        {
            "title": "Review 2",
            "description": "Description 2",
            "rating": 4,
            "author": "Author 2",
            "song": "Song 2",
        },
        {
            "title": "Review 3",
            "description": "Description 3",
            "rating": 3,
            "author": "Author 3",
            "song": "Song 3",
        },
    ]
    }


def test_get_reviews_empty_list(client: TestClient):
    ReviewService.get_reviews = MagicMock(
        return_value=[])  # Simulate empty list
    response = client.get("/reviews")

    assert response.status_code == 200
    assert response.json() == {"reviews": []}
