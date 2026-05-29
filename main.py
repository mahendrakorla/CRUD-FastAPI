from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

data = [
    {
        "book_id": 1,
        "author": "George Orwell",
        "name": "1984",
        "date": "1949-06-08"
    },
    {
        "book_id": 2,
        "author": "J.K. Rowling",
        "name": "Harry Potter and the Sorcerer's Stone",
        "date": "1997-06-26"
    },
    {
        "book_id": 3,
        "author": "Harper Lee",
        "name": "To Kill a Mockingbird",
        "date": "1960-07-11"
    },
    {
        "book_id": 4,
        "author": "F. Scott Fitzgerald",
        "name": "The Great Gatsby",
        "date": "1925-04-10"
    },
    {
        "book_id": 5,
        "author": "J.R.R. Tolkien",
        "name": "The Hobbit",
        "date": "1937-09-21"
    }
]

app = FastAPI()

@app.get("/all_books")
def books():
    return data


class Create(BaseModel):
    book_id: int
    author: str
    name: str
    date: str


@app.post("/create")
def create_book(create: Create):

    new_book = create.model_dump()

    data.append(new_book)

    return {
        "message": "Book added successfully",
        "data": new_book
    }


@app.get("/all_books/{book_id}")
def spec(book_id: int):

    for book in data:

        if book["book_id"] == book_id:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND
    )


class Update(BaseModel):
    author: str
    name: str
    date: str


@app.put("/update_book/{id2}")
def book_update(id2: int, update: Update):

    for book in data:

        if book["book_id"] == id2:

            book["author"] = update.author
            book["name"] = update.name
            book["date"] = update.date

            return {
                "message": "Book updated successfully",
                "data": book
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


@app.delete("/delete/{book_id}")
def dele(book_id: int):

    for book in data:

        if book["book_id"] == book_id:

            data.remove(book)

            return {
                "Message": "Book removed successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Details not found"
    )
