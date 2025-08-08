import aiosqlite as sql
from fastapi import FastAPI,HTTPException, Form


DataBase = "todo.db"
app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Welcome to my To-DO app."}

@app.get("/items")
async def read_items():
    async with sql.connect(DataBase) as db:
        db.row_factory = sql.Row
        curser = await db.execute("SELECT * FROM tasks;")
        items = await curser.fetchall()
        return [dict(item) for item in items]
    
@app.delete("/items")
async def remove(id: str = Form()):
    async with sql.connect(DataBase) as db:
        id = int(id)
        curser = await db.execute("DELETE FROM tasks WHERE id=?",(id,))
        await db.commit()
        if curser.rowcount == 0:
            raise HTTPException(status_code=404, detail="ID not found!")
        return {"Message": f"Task with {id} deleted ✅"}

...