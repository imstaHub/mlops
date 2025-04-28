# main.py

# data
books = [
  { 'title': '1984', 'author': 'George Orwell', 'year': '1949' },
  { 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': '1925' }
]



from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/books")
def get_books(title: str = None):
    if(title is None):
        rst = books
    else:
        rst = [x for x in books if x['title']==title]
    return rst

@app.post("/books")
def set_books(item: dict):
    if('title' not in item.keys()):
        raise Exception('No title')
    if('author' not in item.keys()):
        raise Exception('No author')
    if('year' not in item.keys()):
        raise Exception('No year')

    books.append(item)

    return True