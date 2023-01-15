import logging

from dataclasses import dataclass
from typing import Optional, Union, List

from . import massage


logger = logging.getLogger('root')


@dataclass
class Preview:
    id: int
    title: str
    image: str
    release_date: str


def get_list_preview(data: Optional[dict]) -> Union[List[Preview], str]:
    """Get preview list movie/tv"""
    if not data:
        logger.error("There is no data for preview")
        return massage.ERROR_NOT_DATA_PREVIEW

    image_base = "https://image.tmdb.org/t/p/w220_and_h330_face"
    list_preview = []
    for item in data.get("results"):
        list_preview.append(
            Preview(
                id=item.get("id"),
                title=item.get("title") or item.get("name"),
                image=image_base + item.get("poster_path", ""),
                release_date=(item.get("release_date")
                              or item.get("first_air_date"))
            )
        )

    return list_preview
