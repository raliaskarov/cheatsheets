Code snippets for machine learning


# Data

## Preparing train and test data sets

```
from sklearn.model_selection import train_test_split
X = apple_df.drop(['% Change in Quarterly EPS (Target Output)'], axis = 1)
y = apple_df['% Change in Quarterly EPS (Target Output)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, shuffle = True )
print(f"X_train: {X_train.shape}\nX_test: {X_test.shape}\ny_train: {y_train.shape}\ny_test: {y_test.shape}")
# comment --> test is now larger
```
