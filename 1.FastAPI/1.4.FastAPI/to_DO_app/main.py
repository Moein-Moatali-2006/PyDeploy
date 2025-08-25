import aiosqlite as sql
from fastapi import FastAPI,HTTPException, Form


DataBase = "todo.db"
app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Welcome to my To-DO app."}

@app.get("/task")
async def read_task():
    async with sql.connect(DataBase) as db:
        db.row_factory = sql.Row
        curser = await db.execute("SELECT * FROM tasks;")
        items = await curser.fetchall()
        return [dict(item) for item in items]
    
@app.delete("/task")
async def remove_task(id: str = Form()):
    async with sql.connect(DataBase) as db:
        id = int(id)
        curser = await db.execute("DELETE FROM tasks WHERE id=?",(id,))
        await db.commit()
        if curser.rowcount == 0:
            raise HTTPException(status_code=404, detail="ID not found!")
        return {"Message": f"Task with {id} deleted ✅"}

@app.post("/task")
async def add_task(title: str= Form(), description: str= Form(), time: str= Form(), status: str= Form()):
    async with sql.connect(DataBase) as db:
        id = int(id)
        status = int(status)
        await db.execute(f'INSERT INTO tasks (title, description, time, status) VALUES ("{title}", "{description}", "{time}", {status})')
        await db.commit()
        return {"Message": "Data Added."}
    
@app.put("/task")
async def edit_task(id: str= Form(), title: str= Form(), description: str= Form(), time: str= Form(), status: str= Form()):
    async with sql.connect(DataBase) as db:
        id = int(id)
        status = int(status)
        curser = await db.execute(f"UPDATE tasks SET title='{title}', description='{description}', time='{time}', status={status} WHERE id=?",(id,))
        await db.commit()
        
        if curser.rowcount == 0:
            raise HTTPException(status_code=404, detail="ID not found!")
        
        return {"Message": "Data changed"}
    
