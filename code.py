import pandas as pd
import math
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import getpass

# Função de cálculo de entropia (Método Shannon)
def calculate_entropy(password):
    char_count = {}
    for c in password:
        char_count[c] = char_count.get(c, 0) + 1
    entropy = 0.0
    for count in char_count.values():
        probability = count / len(password)
        entropy -= probability * math.log2(probability)
    return entropy

# Feature engineering com entropia
def extract_features(password):
    return {
        'length': len(password),
        'num_digits': sum(c.isdigit() for c in password),
        'num_upper': sum(c.isupper() for c in password),
        'num_lower': sum(c.islower() for c in password),
        'num_special': len([c for c in password if not c.isalnum()]),
        'entropy': calculate_entropy(password)
    }

# Carregar dados
data = pd.read_csv("data.csv", on_bad_lines='skip').dropna()
data["strength"] = data["strength"].map({0: "Weak", 1: "Medium", 2: "Strong"})

# Extrair features
X = pd.DataFrame([extract_features(pwd) for pwd in data['password']])
y = data['strength']

# Divisão treino/teste
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo e otimização
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5]
}

grid_search = GridSearchCV(
    RandomForestClassifier(class_weight='balanced'),
    param_grid,
    cv=5
)
grid_search.fit(xtrain, ytrain)
model = grid_search.best_estimator_

# Avaliação
ypred = model.predict(xtest)
print(classification_report(ytest, ypred))

# Predição
user = getpass.getpass("Senha: ")
user_features = pd.DataFrame([extract_features(user)])
print("Força:", model.predict(user_features)[0])
