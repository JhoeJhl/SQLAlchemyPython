from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///productos.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 🔹 MODELO PRODUCT
class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Product id={self.id} name='{self.name}' price={self.price} stock={self.stock}>"

#inicializar base de datos
def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos creada")

# Insertar productos
def create_products():
    with app.app_context():
        p1 = Product(name="Laptop", price=3500.50, stock=5)
        p2 = Product(name="Mouse", price=50.99, stock=20)
        p3 = Product(name="Teclado", price=120.00)
        p4 = Product(name="Audifono", price=250.00)
        p5 = Product(name="MousePad", price=149.90)


        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()

        print("Productos creados")

#Consultar
def read_products():
    with app.app_context():
        #Consultar todos los productos
        print("\nTodos los productos:")
        products = Product.query.all()
        for p in products:
            print(p)

        #Productos con precio mayor a 100
        print("\nProductos con precio > 240:")
        filtered = Product.query.filter(Product.price > 240).all()
        for p in filtered:
            print(p)

        #Consulta de un solo registro
        print("\nProducto con id=1:")
        product = Product.query.filter_by(id = 1).first()
        if product:
            print(product)
        else:
            print("Producto no encontrado")

#UPDATE 
def update_product():
    with app.app_context():
        print("\nActualizando producto...")

        product = Product.query.filter_by(id=2).first()
        if product:
            product.price = 3000
            product.stock = 10
            db.session.commit()

            print("Producto actualizado:", product)
        else:
            print("Producto no encontrado")

#DELETE
def delete_product():
    with app.app_context():
        print("\nEliminando producto...")

        product = Product.query.filter_by(id=3).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            print("Producto eliminado")
        else:
            print("Producto no encontrado")

if __name__ == '__main__':
    # init_db()
    # create_products()
    # read_products()
    # update_product()
    delete_product()