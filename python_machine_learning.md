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


# Models
## Libraries
```
# import libraries
import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input, Dropout
from tensorflow.keras import layers # added later to improve efficiency
import matplotlib.pyplot as plt
import numpy as np
```

## Assessment

```
# support function to plot classification results
def evaluate(X_test, y_test, model):
  # evaluate
  test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
  print("Test accuracy:", test_acc)
  return test_acc

# support function to plot classification results
def test_model(X_test, y_test, model):
  # evaluate
  test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)

  # plot
  plt.figure(figsize=(20, 7))
  for i in range(20):
      pred = np.argmax(model.predict(X_test[i].reshape(1, 32, 32, 3)))
      true_idx = int(np.argmax(y_test[i]))
      plt.subplot(4, 5, i+1)
      plt.imshow(X_test[i])
      ok = (pred == true_idx)
      title_text = f"Predicted: {labels[pred]}\n(Correct: {labels[true_idx]})"
      plt.title(title_text, color=("green" if ok else "red"), fontsize=9)
      plt.axis('off')
  plt.subplots_adjust(hspace=0.5, wspace=0.3)
  plt.show()
  print("Test accuracy:", test_acc)

# test one image
def test_single_image(test_image_index):
  # show image
  plt.imshow(X_test[test_image_index])

  # predict
  pred = np.argmax(model.predict(X_test[test_image_index].reshape(1, 32, 32, 3)))

  # get right answer
  true_idx = int(np.argmax(y_test[test_image_index]))


  print("Predicted Label: ", labels[pred])
  print("Correct  Label: ", labels[true_idx])

# plot history
def plot_history(history):
  plt.figure(figsize=(6, 4))

  plt.plot(history.history['accuracy'], label='Training Accuracy')
  plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
  plt.title('Accuracy')
  plt.legend()

  plt.figure(figsize=(6, 4))
  plt.plot(history.history['loss'], label='Training Loss')
  plt.plot(history.history['val_loss'], label='Validation Loss')
  plt.title('Loss')
  plt.legend()
```
