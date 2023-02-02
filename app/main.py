from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
	return {"Hello": "World"}

@app.get("/lex/{message}")
def read_item(message: str, q: str=None):
	return { "message": message, "q": q}
