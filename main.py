import psycopg
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

databasepass = "123456abc"
url2= f"postgresql://postgres.ungwosiuhjtkxdnrbttr:{databasepass}@aws-0-us-east-2.pooler.supabase.com:6543/postgres"
def getConnection():
    try:
        conn = psycopg.connect(url2, sslmode='require')
        
        return conn
    except Exception as e:
        print("Error:", e)
        return None

conn = getConnection()
if conn:
    print("✅")
    conn.close()
else:
    print("❌")


class User(BaseModel):
    usuario: str
    password: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/users")
def getUsers():
    try:
        conn = getConnection()
        cur = conn.cursor()
        cur.execute("SELECT id, usuario, password FROM usuarios LIMIT 10;") 
        rows = cur.fetchall()
        results = [{"id": row[0], "usuario": row[1],"password": row[2]} for row in rows]
        return results
    except Exception as e:
        return {"error": str(e)}


@app.post("/insert_user")
def postUser(user:User):
    try:
        conn = getConnection()
        with conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO usuarios (usuario, password) VALUES (%s, %s);", (user.usuario, user.password)) 
                return {"mensaje": "usuario insertado correctamente"}
       
    except Exception as e:
        return {"error": str(e)}

@app.delete("/delete_user/{id}")
def postUser(id:int):
    try:
        conn = getConnection()
        with conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM usuarios WHERE id = (%s);", (id,)) 
                return {"mensaje": "usuario eliminado correctamente"}
       
    except Exception as e:
        return {"error": str(e)}

@app.put("/update_user/{id}")
def postUser(user:User, id: int):
    try:
        conn = getConnection()
        with conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE usuarios SET usuario = %s, password = %s WHERE id = %s;", (user.usuario, user.password, id)) 
                return {"mensaje": "usuario actualizado correctamente"}
       
    except Exception as e:
        return {"error": str(e)}