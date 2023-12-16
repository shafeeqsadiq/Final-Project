from flask import Flask, jsonify, request
from utils.data_handler import read_data, write_data

app = Flask(__name__)

# Load data handler
data_file_path = 'data/airbnb.json'
airbnb_data = read_data(data_file_path)

@app.route('/listings', methods=['GET'])
def get_all_listings():
    try:
        return jsonify(airbnb_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/listings/<int:listing_id>', methods=['GET'])
def get_listing_by_id(listing_id):
    try:
        listing = next((item for item in airbnb_data if item["id"] == listing_id), None)
        if listing:
            return jsonify(listing), 200
        else:
            return jsonify({"error": "Listing not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/listings/search', methods=['POST'])
def search_listings():
    try:
        search_terms = request.json.get('search_terms', [])
        if not search_terms:
            return jsonify({"error": "No search terms provided"}), 400

        results = [item for item in airbnb_data if any(term.lower() in item['name'].lower() for term in search_terms)]
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Function to validate the new listing data
def validate_listing_data(new_listing):
    required_fields = ["name", "host_id", "neighbourhood", "latitude", "longitude", "room_type", "price"]
    
    for field in required_fields:
        if field not in new_listing:
            return False, f"Field '{field}' is required."
    
    return True, None

@app.route('/listings', methods=['POST'])
def create_listing():
    new_listing = request.json

    # Validate the new listing data
    is_valid, error_message = validate_listing_data(new_listing)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    # Add the new listing to the data
    new_listing["id"] = max(item["id"] for item in airbnb_data) + 1
    airbnb_data.append(new_listing)
    write_data(data_file_path, airbnb_data)

    return jsonify({"message": "Listing created successfully", "id": new_listing["id"]}), 201
    return jsonify({"message": "Listing created successfully", "id": new_listing["id"]}), 201

    
def validate_updated_data(updated_data):
    allowed_fields = ["name", "host_id", "neighbourhood", "latitude", "longitude", "room_type", "price"]
    
    for field in updated_data:
        if field not in allowed_fields:
            return False, f"Field '{field}' is not allowed for updating."

    # Additional validation rules can be added based on your requirements
    # For example, checking if 'price' is a positive number, etc.
    
    return True, None

@app.route('/listings/<int:listing_id>', methods=['PATCH'])
def update_listing(listing_id):
    # Find the index of the listing with the given ID
    index = next((i for i, item in enumerate(airbnb_data) if item["id"] == listing_id), None)
    
    if index is None:
        return jsonify({"error": "Listing not found"}), 404

    # Get the existing listing data
    existing_listing = airbnb_data[index]

    # Get the updated data from the request
    updated_data = request.json

    # Validate the updated data
    is_valid, error_message = validate_updated_data(updated_data)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    # Update the existing listing with the new data
    existing_listing.update(updated_data)

    # Write the updated data back to the file
    write_data(data_file_path, airbnb_data)

    return jsonify({"message": "Listing updated successfully"}), 200

@app.route('/listings/<int:listing_id>', methods=['DELETE'])
def delete_listing(listing_id):
    # Find the index of the listing with the given ID
    index = next((i for i, item in enumerate(airbnb_data) if item["id"] == listing_id), None)

    if index is None:
        return jsonify({"error": "Listing not found"}), 404

    # Remove the listing from the data
    deleted_listing = airbnb_data.pop(index)

    # Write the updated data back to the file
    write_data(data_file_path, airbnb_data)

    return jsonify({"message": "Listing deleted successfully", "deleted_listing": deleted_listing}), 200

if __name__ == "__main__":
    app.run(debug=True)
