from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_validate

def train_RFR(x, y, k: int = 5, **kwargs) -> RandomForestRegressor:
    """x = x data as array
    y = y data as array
    n_estimatores: int = amount of trees in RFR
    random_state: int = randomness
    k: int = number of folds in data for cross validation

    train data from trainingsset
    """

    RFR = RandomForestRegressor(**kwargs)

    cross_validation_score = cross_validate(RFR, x, y, cv=k, return_train_score=True)

    RFR.fit(x, y)

    return RFR, cross_validation_score

def apply_RFR(RFR: RandomForestRegressor, x):
    """RFR = trained RandomForestRegressor model
    x = predict data

    predict outcome y for x
    """

    y_predicted = RFR.predict(x)

    return y_predicted