import pytest
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, inference, compute_model_metrics
from train_model import X_train, y_train, X_test, y_test
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_output():
    """
    # Test that train_model returns a trained model object.
    """
    # Your code here
    model = train_model(X_train, y_train)
    assert model is not None
    assert hasattr(model, "predict")


# TODO: implement the second test. Change the function name and input as needed
def test_metrics():
    """
    # Test that returns expected metric types.
    """
    # Your code here
    model = train_model(X_train, y_train)
    prediction = inference(model, X_test)
    precision, recall, f1 = compute_model_metrics(y_test, prediction)
    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(f1, float)


# TODO: implement the third test. Change the function name and input as needed
def test_length():
    """
    # Test if output length matches input sample size.
    """
    # Your code here
    model = train_model(X_train, y_train)
    prediction = inference(model, X_train)
    assert len(prediction) == len(X_train), "Inference output should match the number of input samples"
