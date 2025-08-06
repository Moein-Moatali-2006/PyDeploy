""" API for information of six chess pieces """
import io
import cv2
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import StreamingResponse


app = FastAPI()

pieces_name = {
    "king" : "Must be protected; game ends if it's checkmated",
    "queen" : "Moves in any direction; most powerful piece",
    "rook" : "Moves straight: horizontally or vertically",
    "bishop" : "Moves diagonally",
    "knight" : "Moves in an L-shape; jumps over pieces",
    "pawn" : "Moves forward, captures diagonally; promotes at last rank"
}

@app.get("/")
def root():
    return "API for information of six chess pieces"

@app.get("/pieces")
async def pieces():
    return list(pieces_name.keys())

@app.get("/pieces/{piece_name}")
def players(piece_name:str):
    if piece_name in pieces_name:
        return pieces_name[piece_name]
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="you got me a bad request please choice between:[pawn, bishop, knight, rook, queen, king].")
    
@app.get("/pieces/{piece_name}/image")
async def image(piece_name:str):
    if piece_name in pieces_name:
        image = cv2.imread(f"images/{piece_name}.png")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        _, image_encoded = cv2.imencode('.png', image)
        if not _:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to encode image.")
        
        return StreamingResponse(io.BytesIO(image_encoded.tobytes()), media_type="image/png")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="you got me a bad request please choice between:[pawn, bishop, knight, rook, queen, king].")
        
