from typing import Annotated
from fastapi import status, Response, Depends

from api.oauth2 import oauth2_scheme
from app.app import v1
import api.urls as urls

v1.get(urls.PING, status_code=status.HTTP_204_NO_CONTENT) 
async def ping() :
    """ accept ping for various object such as healthcheck.

    Returns:
        fastapi.Response: http connection response
    """
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@v1.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}