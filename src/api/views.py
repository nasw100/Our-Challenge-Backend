from fastapi import status, Response

from app.app import v1
import api.urls as urls

v1.get(urls.PING, status_code=status.HTTP_204_NO_CONTENT) 
async def ping() :
    """ accept ping for various object such as healthcheck.

    Returns:
        fastapi.Response: http connection response
    """
    return Response(status_code=status.HTTP_204_NO_CONTENT)

