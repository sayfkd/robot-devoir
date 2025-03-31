import pandas as pd
import numpy as np
from faker import Faker
import json
import os
from datetime import date

fake = Faker()

# Ajoutez ce convertisseur personnalisé pour les dates
def json_serializer(obj):
    """Convertit les objets non sérialisables en string"""
    if isinstance(obj, (date, pd.Timestamp)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def generate_users(num=20):
    """Génère des données utilisateur aléatoires"""
    users = []
    for _ in range(num):
        users.append({
            'id': fake.unique.random_number(digits=3),
            'name': fake.name(),
            'email': fake.email(),
            'status': np.random.choice(['active', 'inactive'], p=[0.7, 0.3]),
            'created_at': fake.date_this_decade()  # Ceci retourne un objet date
        })
    return users

def save_test_data(data, filename):
    """Sauvegarde les données dans un fichier JSON"""
    output_dir = 'data_generation/output'
    os.makedirs(output_dir, exist_ok=True)
    
    with open(f'{output_dir}/{filename}', 'w') as f:
        json.dump(data, f, indent=2, default=json_serializer)  # Utilisez le convertisseur

if __name__ == '__main__':
    # Génération des données de test
    users = generate_users()
    
    # Sauvegarde
    save_test_data(users, 'users.json')
    print(f"Données de test générées avec succès dans data_generation/output/users.json")