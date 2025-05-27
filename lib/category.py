
from db.models import Category

def view_categories(session, user):
    categories = session.query(Category).filter_by(user_id=user.id).all()

    if categories:
        for c in categories:
            print(f"ID: {c.id} | Name: {c.name}")
    else:
        print("No categories found.")
    input("Press Enter to continue...")
