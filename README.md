# FastAPI Bookstore CRUD API

A simple CRUD (Create, Read, Update, Delete) REST API built using FastAPI and Pydantic.

## Features

* View all books
* Get a single book by ID
* Add new books
* Update existing books
* Delete books
* Automatic Swagger UI documentation
* Request validation using Pydantic

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn

## API Endpoints

### GET

* `/all_books` → Get all books
* `/all_books/{book_id}` → Get a specific book

### POST

* `/create` → Add a new book

### PUT

* `/update_book/{id2}` → Update book details

### DELETE

* `/delete/{book_id}` → Delete a book

## Run the Project

Install dependencies:

```bash
pip install fastapi uvicorn
```

Run server:

```bash
uvicorn main:app --reload
```

Open Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

## Project Goal

This project was created to practice FastAPI fundamentals, REST API development, CRUD operations, request validation, and API testing using Swagger UI.
