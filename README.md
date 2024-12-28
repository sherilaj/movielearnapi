# MovieLearnAPI
MovieLearnAPI is a Django-based RESTful API for managing and exploring movie data. The application integrates with external movie databases 
like OMDb and provides endpoints for searching, viewing details, and managing favourite movies.

## Features
1. Search for movies by title using the OMDb API.
2. Retrieve detailed information about a specific movie.
3. Manage a list of favourite movies.
4. RESTful endpoints for CRUD operations on movie data.

### API's
### Movie Search
- **Endpoint**: `/api/search/`
- **Method**: `GET`
- **Description**: Search for movies by title.
- **Query Parameters**: `Title` 

### Movie Details
- **Endpoint**: `/api/movie/<id>/`
- **Method**: `GET`
- **Description**: Retrieve detailed information about a specific movie.

### Favorite Movies
- **Endpoint**: `/api/favourites/`
- **Method**: `GET`
- **Description**: Retrieve a list of favorite movies.

### Add a Movie
- **Endpoint**: `/api/addmovie/`
- **Method**: `POST`
- **Description**: Add a new movie to the database.

### Edit a Movie
- **Endpoint**: `/api/updatemovie/<id>`
- **Method**: `PUT`
- **Description**: Editing existing movie to the database.

  ### Delete a Movie
- **Endpoint**: `/api/deletemovie/<id>`
- **Method**: `DELETE`
- **Description**: Deleting existing movie 
