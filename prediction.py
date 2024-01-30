import joblib

def predict(data):
    clf = joblib.load('lgr_model.sav')
    return clf.predict(data)