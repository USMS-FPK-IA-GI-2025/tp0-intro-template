import numpy as np
import src.answers as A

def test_student_github():
    assert isinstance(A.STUDENT_GITHUB, str) and A.STUDENT_GITHUB.strip() != "", \        "Renseignez votre identifiant GitHub dans STUDENT_GITHUB (chaîne non vide)."

def test_add():
    # fonction add
    assert callable(A.add)
    assert A.add(2, 3) == 5
    assert A.add(-1, 1) == 0
