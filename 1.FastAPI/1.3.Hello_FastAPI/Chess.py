""" API for information of six chess pieces """

from fastapi import FastAPI, HTTPException, status


app = FastAPI()

@app.get("/")
async def root():
    return "API for information of six chess pieces"

@app.get("/pieces")
async def pieces():
    return "[pawn, bishop, knight, rook, queen, king]"

@app.get("/pieces/{piece_name}")
async def players(piece_name:str):
    pieces = {
        "king" : "Must be protected; game ends if it's checkmated",
        "queen" : "Moves in any direction; most powerful piece",
        "rook" : "Moves straight: horizontally or vertically",
        "bishop" : "Moves diagonally",
        "knight" : "Moves in an L-shape; jumps over pieces",
        "pawn" : "Moves forward, captures diagonally; promotes at last rank"
    }

    if piece_name in pieces:
        return pieces[piece_name]
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="you got me a bad request please choice between:[pawn, bishop, knight, rook, queen, king].")
    
