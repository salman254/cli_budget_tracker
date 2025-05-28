from db.models import Category

def category_menu(session, user):
    while True:
        print("\nCategory Management:")
        categories = session.query(Category).filter_by(user_id=user.id).all()
        if categories:
            for c in categories:
                print(f"ID: {c.id} | Name: {c.name}")
        else:
            print("No categories found.")

        print("\nOptions:")
        print("1. Add Category")
        print("2. Edit Category")
        print("3. Delete Category")
        print("4. Return to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_category(session, user)
        elif choice == "2":
            edit_category(session, user)
        elif choice == "3":
            delete_category(session, user)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def add_category(session, user):
    name = input("Enter new category name: ").strip()
    if name:
        new_category = Category(name=name, user=user)
        session.add(new_category)
        session.commit()
        print("Category added successfully.")
    else:
        print("Category name cannot be empty.")
    input("Press Enter to continue...")

def edit_category(session, user):
    cat_id = input("Enter the ID of the category to edit: ").strip()
    category = session.query(Category).filter_by(id=cat_id, user_id=user.id).first()
    if category:
        new_name = input("Enter new category name: ").strip()
        if new_name:
            category.name = new_name
            session.commit()
            print("Category updated.")
        else:
            print("New name cannot be empty.")
    else:
        print("Category not found.")
    input("Press Enter to continue...")

def delete_category(session, user):
    cat_id = input("Enter the ID of the category to delete: ").strip()
    category = session.query(Category).filter_by(id=cat_id, user_id=user.id).first()
    if category:
        session.delete(category)
        session.commit()
        print("Category deleted.")
    else:
        print("Category not found.")
    input("Press Enter to continue...")
