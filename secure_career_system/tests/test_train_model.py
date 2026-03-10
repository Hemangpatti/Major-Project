from secure_career_system import train_model
import os


def test_generate_and_train():
    path = 'test_data.csv'
    train_model.generate_synthetic(path=path, n=50)
    assert os.path.exists(path)
    # clean up
    os.remove(path)
