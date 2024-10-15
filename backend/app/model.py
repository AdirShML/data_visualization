import psycopg2

    
def db_conn():
    conn = psycopg2.connect(
        dbname = 'dataset',
        user = 'postgres',
        password = 'admin',
        host = 'localhost',
        port = '5432'
    ) 
    cursor = conn.cursor()
    return cursor, conn
    
    
    
    
        
        
        
        
    
    

