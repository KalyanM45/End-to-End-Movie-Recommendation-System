import os
from pathlib import Path

list_of_files=[
    "Artifacts/__init__.py",
    "NoteBook_Experiments/Movie_Recommendation_System.ipynb",
    "NoteBook_Experiments/Sentimental_Analysis_on_reviews.ipynb",
    "static/style.css",
    "templates/index.html",
    "templates/recommend.html",
    "app.py",
    "Dockerfile",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
            with open (filepath, 'w') as f:
                pass