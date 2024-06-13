from fastapi import FastAPI, APIRouter, Query, HTTPException, Path
from typing import Union
from time import time
import uuid
from fastapi.responses import RedirectResponse
from collections import defaultdict
from typing import Dict, DefaultDict


app = FastAPI()
router = APIRouter(prefix='/api/v1', tags=['Shorten URL'])

#url_repository = {}
url_repository: DefaultDict[str, Dict[str, Union[str, int]]] = defaultdict(dict)


class URLMapping:
    def __init__(self, original_url: str, access_count: int):
        self.original_url = original_url
        self.access_count = access_count

#UUIDs são projetados para serem únicos
#apesar do truncamento a chance de colisão é baixa
def generate_alias():
    alias = str(uuid.uuid4())[:8]
    while alias in url_repository:
        alias = str(uuid.uuid4())[:8]
    return alias

@router.post('/shorten_url', description='Shorten original URL.')
def shorten_url(
    url: str = Query(..., description='URL to shorten', min_length=10),
    custom_alias: Union[str, None] = Query(None, description='Custom alias', min_length=1, max_length=50)
):
    start_time = time()

    if custom_alias:
        if custom_alias in url_repository:
            raise HTTPException(status_code=400, detail={"ERR_CODE": "001", "Description": "CUSTOM ALIAS ALREADY EXISTS"})
        alias = custom_alias
    else:
        alias = generate_alias()

    url_repository[alias] = URLMapping(original_url=url, access_count=0)
    short_url = f"http://shortener/u/{alias}"

    end_time = time()
    return {
        "alias": alias,
        "short_url": short_url,
        "original_url": url,
        "statistics": {
            "time_taken": end_time - start_time,
        }
    }

@router.get('/retrive_url/{alias}', description='Retrieve original URL.')
def get_original_url(alias: str = Path(..., description="Shortened URL alias")):
    if alias not in url_repository:
        raise HTTPException(status_code=404, detail={"ERR_CODE": "002", "Description": "SHORTENED URL NOT FOUND"})
    
    url_repository[alias].access_count += 1
    return RedirectResponse(url=url_repository[alias].original_url)

@router.get('/most_accessed', description='Retrieve 10 most accessed URLs.')
def get_most_accessed_urls():
    most_accessed = sorted(url_repository.values(), key=lambda x: x.access_count, reverse=True)[:10]
    return most_accessed

