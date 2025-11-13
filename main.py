
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

"""python -m pip install "fastapi[all]"
CRUD
Create, Read, Update, Delete
app.post: Create
app.get: Read  
app.put: Update
app.delete: Delete
"""

items = {
			0: {"name": "bread",
				"price": 1000},
		    1: {"name": "water",
			    "price": 500},
		    2: {"name": "라면",
				"price": 1200}
	    }

# Path PrameterC:\Users\thswj\Desktop
@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items[item_id]
    return item

@app.get("/items")
def read_all_item():
    return items

# Query Parameter
@app.get("/item-by-name")
def read_item_by_name(name: str):
    for item_id, item in items.items():
        if item['name'] == name:
            return item
    return {"message": "Not found"}

@app.get("/search")
def search_item(name: str, price: int = 1000):
    return {"name": name, "price": price}

class Item(BaseModel):
    name: str
    price: int

@app.post("/items")
def create_item(item: Item):
    return item

from fastapi import status

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    return item