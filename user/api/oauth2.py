from fastapi.security import OAuth2PasswordRequestFormStrict, OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
