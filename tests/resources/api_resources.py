import json
import os

def get_test_data(filename):
    """Charge les données de test depuis le fichier JSON"""
    filepath = os.path.join('data_generation/output', filename)
    with open(filepath, 'r') as f:
        return json.load(f)