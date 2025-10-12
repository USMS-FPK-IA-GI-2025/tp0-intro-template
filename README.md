# TP0 — Introduction à Python pour la Data Science

**Organisation : USMS-FPK-IA-GI-2025**  
**Module : Python pour les Sciences de Données**  
**Type : TP individuel**

## 🎯 Objectifs
- Vérifier que l'environnement de travail (Git/GitHub/pytest) est opérationnel.
- Réviser les bases de Python (variables, fonctions) et un tout petit peu NumPy.
- Apprendre le workflow Classroom : *accept → clone → coder → tester → commit/push*.

## 📦 Contenu du dépôt
```
tp0-intro-template/
├── starter/TP0_Intro_Python_Data_Science.ipynb   # Notebook d'énoncé guidé
├── src/answers.py                                # Fichier à compléter (évalué)
├── tests/                                        # Tests automatiques (pytest)
├── data/                                         # (optionnel) jeux de données
├── requirements.txt
└── README.md
```

## 🚀 Démarrage rapide

### Option A — Google Colab (recommandée)
1. Ouvrez le notebook : `starter/TP0_Intro_Python_Data_Science.ipynb`.
2. Montez votre repo GitHub (ou importez le notebook via URL).
3. Exécutez les cellules et complétez le fichier `src/answers.py` (voir TODOs).

### Option B — Local (VS Code/Jupyter)
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q          # Lance les tests (au début, ils échouent)
jupyter lab        # Pour ouvrir le notebook
```

## ✅ À faire (critères minimum)
- Renseigner `STUDENT_GITHUB` dans `src/answers.py`.
- Implémenter `add(a, b)`.
- Créer un array NumPy `arr = np.array([1, 2, 3])` et sa moyenne `arr_mean`.
- Implémenter `normalize(x)` (min-max), en gérant le cas `max==min`.

Les tests automatiques vérifient ces éléments.

## 🧪 Lancer les tests
- Local : `pytest -q`
- Colab : exécuter `!pip install -r requirements.txt` puis `!pytest -q`

## 📝 Barème indicatif
- Mise en place de l'env & variables : 30 %
- Fonctions correctes + style : 50 %
- Respect du workflow Git (commits clairs) : 20 %

## 🔄 Workflow Classroom
1. Accepter l'invitation Classroom
2. Cloner le repo
3. Coder & tester
4. Commit/push
5. Vérifier sur GitHub (Actions / autograding le cas échéant)

Bon TP !
