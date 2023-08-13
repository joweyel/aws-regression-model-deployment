from util import get_data

def test_get_data_shape():
    X_train, y_train, X_test, y_test = get_data()
    assert X_train.shape[0] == y_train.shape[0]
    assert X_test.shape[0] == y_test.shape[0]

def test_get_data_split():
    assert 4 == len(get_data(0.5))

    train_split = 0.7
    N = 150
    X_train, y_train, X_test, y_test = get_data(train_split=train_split, N=N)
    n_train = int(N * train_split)
    assert X_train.shape[0] == n_train
    assert y_train.shape[0] == n_train
    assert X_test.shape[0] == N - n_train
    assert y_test.shape[0] == N - n_train
