# A book review app

This app would allow users to create, read, and review books. It would have the following features:
- A user management system to allow users to create and manage their accounts.
- A book model to store information about books, such as the title, author, genre, and rating.
- A review model to store information about reviews, such as the user who wrote the review, the book they reviewed, and the rating they gave.
- A REST API that allows users to interact with the app's data programmatically.

This app would be a great addition to your portfolio because it would demonstrate your skills in Django, Django REST framework, and user authentication. It would also be a useful app for people who want to read and review books.

### Here are some additional details about the app:

- The user management system would use Django's built-in authentication system.
- The book model would have the following fields:
  - title
  - author
  - genre
  - rating (out of 5 stars)
- The review model would have the following fields:
  - user
  - book
  - rating (out of 5 stars)
  - review text
- The REST API would expose the following endpoints:
  - /books/
    - GET: Get a list of all books.
    - POST: Create a new book.
  - /books/<int:book_id>/
    - GET: Get a book by its ID.
    - PUT: Update a book.
    - DELETE: Delete a book.
  - /reviews/
    - GET: Get a list of all reviews.
    - POST: Create a new review.
  - /reviews/<int:review_id>/
    - GET: Get a review by its ID.
    - PUT: Update a review.
    - DELETE: Delete a review.


### Example of data for test

#### User data

{
    "id": 1,
    "username": "johndoe",
    "email": "johndoe@example.com",
    "password": "password"
}

{
    "id": 2,
    "username": "janedoe",
    "email": "janedoe@example.com",
    "password": "password"
}

##### Book data

{
    "id": 1,
    "title": "The Martian",
    "author": "Andy Weir",
    "genre": "Sci-Fi",
    "rating": 4.5
}

{
    "id": 2,
    "title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "genre": "Comedy",
    "rating": 5.0
}

#### Review data

{
    "id": 1,
    "user": 1,
    "book": 1,
    "rating": 5,
    "review text": "This book was amazing! I couldn't put it down."
}

{
    "id": 2,
    "user": 2,
    "book": 2,
    "rating": 4,
    "review text": "This book was very funny! I loved the wit and humor."
}