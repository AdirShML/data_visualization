from fastapi import FastAPI, HTTPException
import logging
from app.searchmodel import show_product

# Initialize FastAPI
app = FastAPI()


@app.get('/search/{product}')
def search_product(product: str):
    try:
        context = show_product(product)
        return context
    except Exception as e:
        logging.error(f"Error searching for product: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


    
    
    
    
    
    
    

    
    
    
    
    
        