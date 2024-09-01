from app import app, db

print("App name:", app.name)
with app.app_context():
    print("Creating tables...")
    db.create_all()
    print("Tables created.")