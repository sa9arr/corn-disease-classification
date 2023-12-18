# from fastapi import FastAPI, File, UploadFile
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image


# app = FastAPI()

# @app.get("/test")

# async def test():
#     return "The server is live."


# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)))
#     return image



# @app.post("/predict")
# async def predict(
#     file: UploadFile = File(...)
    
# ):
#     bytes =  await file.read()


# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port= 8000 )