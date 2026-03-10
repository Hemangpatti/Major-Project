import os
import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def generate_placement_data(path='placement_data.csv', n=1000):
    # score in [0,1], cgpa in [0,10]
    rng = np.random.RandomState(0)
    score = rng.rand(n)
    cgpa = rng.uniform(4.0, 10.0, size=n)
    # label: higher score and cgpa more likely placed
    prob = 0.6 * score + 0.4 * (cgpa / 10.0)
    y = (prob > 0.55).astype(int)
    X = np.vstack([score, cgpa / 10.0]).T
    return X, y


def train(path=None):
    X, y = generate_placement_data()
    scaler = StandardScaler()
    Xs = scaler.fit_transform(X)
    model = LogisticRegression(solver='liblinear')
    model.fit(Xs, y)
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'placement_model.pkl')
    joblib.dump(scaler, 'placement_scaler.pkl')
    print('Saved placement_model.pkl and placement_scaler.pkl')


if __name__ == '__main__':
    train()
