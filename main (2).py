from fastapi import FastAPI, HTTPException

app = FastAPI(title="Restaurant Menu API")

# Dataset with 4 appetizers, 5 mains, and 3 desserts
menu_items = [
    # Appetizers
    {"name": "Fried Rice", "price": 5.99, "category": "appetizer", "is_vegetarian": True},
    {"name": "Chicken Wings", "price": 8.99, "category": "appetizer", "is_vegetarian": False},
    {"name": "Samosa", "price": 6.50, "category": "appetizer", "is_vegetarian": True},
    {"name": "Spring Rolls", "price": 7.25, "category": "appetizer", "is_vegetarian": True},
    
    # Main Courses
    {"name": "Grilled Croaker Fish", "price": 18.99, "category": "main", "is_vegetarian": False},
    {"name": "Veggie Burger", "price": 12.50, "category": "main", "is_vegetarian": True},
    {"name": "Ribeye Steak", "price": 24.99, "category": "main", "is_vegetarian": False},
    {"name": "Jollof Rice", "price": 14.00, "category": "main", "is_vegetarian": True},
    {"name": "Chicken Tikka Masala", "price": 16.50, "category": "main", "is_vegetarian": False},
    
    # Desserts
    {"name": "Chocolate Lava Cake", "price": 7.99, "category": "dessert", "is_vegetarian": True},
    {"name": "Red Velvet cake", "price": 6.99, "category": "dessert", "is_vegetarian": True},
    {"name": "Fruit Cake", "price": 5.50, "category": "dessert", "is_vegetarian": True}
]

# 1. GET /menu - Welcome message[span_2](start_span)[span_2](end_span)
@app.get("/menu")
def get_welcome_message():
    return {"message": "Welcome to our Restaurant!"}

# 2. GET /appetizers - List of 4 appetizer names[span_3](start_span)[span_3](end_span)
@app.get("/appetizers")
def get_appetizers():
    return [item["name"] for item in menu_items if item["category"] == "appetizer"]

# 3. GET /main-courses - List of 5 main course names[span_4](start_span)[span_4](end_span)
@app.get("/main-courses")
def get_main_courses():
    return [item["name"] for item in menu_items if item["category"] == "main"]

# 4. GET /desserts - List of 3 dessert names[span_5](start_span)[span_5](end_span)
@app.get("/desserts")
def get_desserts():
    return [item["name"] for item in menu_items if item["category"] == "dessert"]

# 8. GET /vegetarian-options - List of all vegetarian items[span_6](start_span)[span_6](end_span)
@app.get("/vegetarian-options")
def get_vegetarian_options():
    return [item for item in menu_items if item["is_vegetarian"]]

# 9. GET /most-expensive - Details of the most expensive item[span_7](start_span)[span_7](end_span)
@app.get("/most-expensive")
def get_most_expensive():
    return max(menu_items, key=lambda item: item["price"])

# 10. GET /total-items - Dictionary with item counts[span_8](start_span)[span_8](end_span)
@app.get("/total-items")
def get_total_items():
    total_appetizers = len([i for i in menu_items if i["category"] == "appetizer"])
    total_mains = len([i for i in menu_items if i["category"] == "main"])
    total_desserts = len([i for i in menu_items if i["category"] == "dessert"])
    return {
        "total_appetizers": total_appetizers,
        "total_mains": total_mains,
        "total_desserts": total_desserts,
        "total_all": len(menu_items)
    }

# 5. GET /item/{item_name} - Details for a specific item[span_9](start_span)[span_9](end_span)
@app.get("/item/{item_name}")
def get_item(item_name: str):
    for item in menu_items:
        if item["name"].lower() == item_name.lower():
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# 6. GET /category/{category_name} - All items in a category[span_10](start_span)[span_10](end_span)
@app.get("/category/{category_name}")
def get_category(category_name: str):
    matching_items = [
        item for item in menu_items 
        if item["category"].lower() == category_name.lower()
    ]
    return matching_items

# 7. GET /price/{item_name} - Price of a specific item as a string[span_11](start_span)[span_11](end_span)
@app.get("/price/{item_name}")
def get_price(item_name: str):
    for item in menu_items:
        if item["name"].lower() == item_name.lower():
            return f"${item['price']:.2f}"
    raise HTTPException(status_code=404, detail="Item not found")
