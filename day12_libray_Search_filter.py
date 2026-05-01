found = False
books = [
    {"title": "Python Basics", "pages": 150, "category": "Programming"},
    {"title": "Rich Dad Poor Dad", "pages": 200, "category": "Finance"},
    {"title": "AI Revolution", "pages": 300, "category": "Technology"},
    {"title": "Learn SQL", "pages": 180, "category": "Programming"}
]

n = input("Enter book title")
for book in books:
    if book["title"] == n:
        print("Book found",book["title"],book["pages"],book["category"])
        found = True

if not found:
    print("Book not found")


print("Name of the Books which have more than 180 pages")
for book in books:
    if book["pages"] > 180:
        print(f"{book["title"]}  | {book["pages"]} | {book["category"]}")


category= input("Enter you category")
for book in books:
    
    if book["category"] == category:
        print(f"{book['title']} ")
       