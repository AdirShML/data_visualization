from .model import db_conn
import json
from key.searchkey import key_query
from key.reviewkey import review_query

# Establish connection and cursor
def connection():
    cursor, con = db_conn()
    return cursor, con

# Close connection and cursor
def close_connection(cursor, con):
    cursor.close()
    con.close()

# To create the table
def create_table():
    cursor, con = connection()
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                asin VARCHAR(30) NOT NULL,
                product_title TEXT NOT NULL,
                product_price VARCHAR(10) NOT NULL,
                product_original_price VARCHAR(10),
                currency VARCHAR(5) NOT NULL,
                product_star_rating VARCHAR(5),
                product_num_ratings INT,
                product_url VARCHAR(200) NOT NULL,
                product_num_offers INT,
                product_minimum_offer_price VARCHAR(10),
                is_best_seller BOOLEAN,
                is_amazon_choice BOOLEAN,
                is_prime BOOLEAN,
                climate_pledge_friendly BOOLEAN,
                sales_volume VARCHAR(50),
                delivery VARCHAR(50),
                has_variations BOOLEAN,
                PRIMARY KEY (asin)
            )
        ''')
        con.commit()
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        close_connection(cursor, con)

# To show product details after searching
def show_product(product):
    data = key_query(product)  # Assuming key_query returns a dict or JSON string
    print("Product data:", data)  # Add this to inspect the data structure
    # If key_query returns a string, convert it to a dictionary
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON data: {e}")
            return {"error": "Invalid data format from key_query"}
        
    return data

# Save the product to the database
def save_product(data):
    cursor, con = connection()

    # Ensure data is a list of dicts
    if isinstance(data, dict):
        save_content = [data]
    else:
        save_content = data

    query = '''
        INSERT INTO products (asin, product_title, product_price, product_original_price, currency, 
        product_star_rating, product_num_ratings, product_url, product_num_offers, 
        product_minimum_offer_price, is_best_seller, is_amazon_choice, is_prime, 
        climate_pledge_friendly, sales_volume, delivery, has_variations)
        VALUES (%(asin)s, %(product_title)s, %(product_price)s, %(product_original_price)s, %(currency)s, 
                %(product_star_rating)s, %(product_num_ratings)s, %(product_url)s, %(product_num_offers)s,
                %(product_minimum_offer_price)s, %(is_best_seller)s, %(is_amazon_choice)s, %(is_prime)s, 
                %(climate_pledge_friendly)s, %(sales_volume)s, %(delivery)s, %(has_variations)s)
    '''

    try:
        # Insert product data into the database
        cursor.executemany(query, save_content)
        con.commit()
    except Exception as e:
        print(f"Error saving product data: {e}")
    finally:
        close_connection(cursor, con)
   
   
        
        
    
        
    
    