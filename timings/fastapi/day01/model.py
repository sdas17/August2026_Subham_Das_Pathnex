# from fastapi import FastAPI, Header, HTTPException, Depends,Request
# import time
# app = FastAPI()

# @app.middleware("http")
# async def timing_middleware(request: Request, call_next):

#     start = time.time()

#     response = await call_next(request)

#     end = time.time()

#     process_time = end - start

#     response.headers["X-Process-Time"] = str(process_time)

#     return response
# def verify_token(token: str = Header(None)):

#     if token != "subham":
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid token"
#         )

#     return token


# @app.get("/login")
# async def login_user(user=Depends(verify_token)):
#     return {
#         "message": "Successfully authenticated",
#         "token": user
#     }