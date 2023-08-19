from fastapi import APIRouter, status, HTTPException
from src.schemas.song import SongGet, SongModel, SongDelete, SongList, SongNameList
from starlette.responses import JSONResponse
from src.db import database as db

from src.service.impl.song_service import SongService
from src.schemas.song import SongCreateModel

router = APIRouter()

# Get a specific song
@router.get(
    "/song/{song_id}",
    response_model=SongModel,
    response_class=JSONResponse,
    summary="Get a specific song",
)
def get_song(song_id: str):
    song_get_response = SongService.get_song(song_id)

    return song_get_response

@router.put(
    "/song/{song_id}",
    response_model=SongModel,
    response_class=JSONResponse,
    summary="update a song",
)
def edit_song(song_id: str, song: SongCreateModel):
    song_edit_response = SongService.edit_song(song_id, song)

    return song_edit_response


# Add a song
@router.post(
    "/song",
    response_model=SongModel,
    response_class=JSONResponse,
    summary="create a song",
)
def add_song(song: SongCreateModel):
    song_add_response = SongService.add_song(song)

    return song_add_response

@router.delete(
    "/song/{song_id}",
    response_model=SongDelete,
    response_class=JSONResponse,
    summary="delete a song",
)
def delete_song(song_id: str):
    song_delete_response = SongService.delete_song(song_id)
    return song_delete_response

@router.get(
    "/songs/get_top_rated_songs",
    response_model=SongNameList,  # Assuming Song model has a field for average rating
    description="Retrieve top-rated songs"
)
def get_top_rated_songs(limit: int = 5):
    """
    Get the top-rated songs based on average rating.

    Args:
    - limit (int): How many top-rated songs to retrieve. Default is 10.

    Returns:
    - A list of top-rated songs.
    """
    print('teste')
    songs = db.get_top_rated_songs('songs', limit)
    print('TESTE2 ')
    print(songs)
    return {'songs':songs}


# Edit a song's genre
# @router.put(
#     "/song/{song_id}/genre",
#     response_model=HttpResponseModel,
#     status_code=status.HTTP_200_OK,
#     responses={
#         status.HTTP_404_NOT_FOUND: {
#             "description": "Song not found",
#         }
#     },
# )
# def edit_genre(song_id: str, genre: str) -> HttpResponseModel:
#     edit_genre_response = SongService.edit_genre(song_id, genre)
#     return edit_genre_response
