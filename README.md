# Airbnb Listings API

A Flask-based RESTful API that manages Airbnb listings. This API provides comprehensive endpoints for creating, reading, updating, and deleting (CRUD) Airbnb listing data, with data persistence using JSON file storage.

## Features

1. **Listing Management**
   - Get all listings
   - Get specific listing by ID
   - Search listings by terms
   - Create new listings
   - Update existing listings
   - Delete listings

2. **API Endpoints**
   - `GET /listings`: Retrieve all listings
   - `GET /listings/<listing_id>`: Get specific listing
   - `POST /listings/search`: Search listings by terms
   - `POST /listings`: Create new listing
   - `PATCH /listings/<listing_id>`: Update listing
   - `DELETE /listings/<listing_id>`: Delete listing

## Data Structure

Required fields for listings:
- name
- host_id
- neighbourhood
- latitude
- longitude
- room_type
- price

## Error Handling

- 200: Successful operation
- 201: Resource created
- 400: Invalid request
- 404: Resource not found
- 500: Server error

