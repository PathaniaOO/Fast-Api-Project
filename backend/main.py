from fastapi import Depends,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session,engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_methods = ["*"]
)

database_models.Base.metadata.create_all(bind = engine)


@app.get("/")
def greet():
    return "It is going to start"

products = [
    Product(id=1,name="phone",description="Moto",price=633,quantity=100),
    Product(id=2,name="Laptop",description="Acer",price=1000,quantity=30),
    Product(id=3,name="Monitor",description="Lenovo",price=500,quantity=10),
]

def get_db():
    db = session()
    try:
        yield db # waiting for other to use db
    finally:
        db.close()


def init_db():
    db = session()
    count = db.query(database_models.Product).count
    try:
        if count == 0:
            for product in products:
                db.add(database_models.Product(**product.model_dump()))
            db.commit()
            print("Products added successfully!")  # ← check this prints
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")  # ← will tell you exactly what's wrong
    finally:
        db.close()

init_db()

# @app.get("/products")
# def get_all_products():
#     # # db connection
#     # db = session()
#     # db.query()
#     # # query
#     return products

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

# @app.get("/product/{id}")  ----->normal pydantic
# def get_product_by_id(id: int):
#     for product in products:
#         if product.id == id:
#             return product
#     return "product not found"


@app.get("/products/{id}") # ----> database 
def get_product_by_id(id: int,db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return "product not found"


@app.post("/products")
def add_product(product: Product,db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product


# @app.put("/product")
# def update_product(id: int,product: Product,):
#     for i in range(len(products)):
#         if products[i].id == id:
#             products[i] = product
#             return product
#     return {"error": "Product not found"}

@app.put("/products/{id}")
def update_product(id: int,product: Product,db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name 
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Updated"
    else:
        return {"error": "Product not found"}


# @app.delete("/product")
# def delete_product(id: int):
#     for i in range(len(products)):
#         if products[i].id == id:
#             del products[i]
#             return "Product Deleted"
#     return {"error: Product not found"}     


@app.delete("/products/{id}")
def delete_product(id: int,db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Deleted the product"
    else:
        return {"error: Product not found"}   