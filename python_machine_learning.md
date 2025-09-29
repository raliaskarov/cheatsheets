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
### Dataset in numpy array

* data is in NumPy arrays (X_test, y_test),
* images are 32×32×3, and
* labels are one-hot (np.argmax(...)).

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


### Dataset in images
24×224 images (and integer labels 0/1) and a sigmoid output

#### 1) Evaluate any Keras model on a tf.data dataset
```
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

def evaluate_dataset(model, dataset, name=None):
    """Return (loss, accuracy) on a tf.data.Dataset."""
    loss, acc = model.evaluate(dataset, verbose=0)
    if name:
        print(f"{name}: accuracy={acc:.4f} | loss={loss:.4f}")
    return loss, acc
```

#### Compare models Side by Side
```
def compare_models(models: dict, dataset):
    """
    models: dict like {"MobileNetV2": model1, "ResNet50": model2, "VGG16": model3}
    dataset: tf.data.Dataset (validation or test)
    """
    results = {}
    for name, mdl in models.items():
        _, acc = evaluate_dataset(mdl, dataset, name)
        results[name] = acc

    # simple bar chart
    plt.figure(figsize=(6,4))
    names = list(results.keys())
    vals  = [results[k] for k in names]
    plt.bar(names, vals)
    plt.ylim(0, 1.0)
    plt.ylabel("Accuracy")
    plt.title("Model comparison (higher is better)")
    for i, v in enumerate(vals):
        plt.text(i, v + 0.01, f"{v:.3f}", ha="center")
    plt.show()

    # also return a sorted list
    return dict(sorted(results.items(), key=lambda kv: kv[1], reverse=True))
```

Usage
```
models = {
    "MobileNetV2": model_mobilenet,   # your trained feature-extraction model
    "ResNet50":    model_resnet50,
    "VGG16":       model_vgg16,
}

summary = compare_models(models, validation_dataset)
print("Ranked:", summary)
```

#### Plot Training Histories
```
def plot_histories(histories: dict):
    """
    histories: {"MobileNetV2": history_obj, "ResNet50": history_obj, ...}
    """
    plt.figure(figsize=(12,4))
    # Accuracy
    plt.subplot(1,2,1)
    for name, h in histories.items():
        plt.plot(h.history['val_accuracy'], label=f"{name} val_acc")
    plt.title("Validation Accuracy")
    plt.xlabel("Epoch"); plt.legend()

    # Loss
    plt.subplot(1,2,2)
    for name, h in histories.items():
        plt.plot(h.history['val_loss'], label=f"{name} val_loss")
    plt.title("Validation Loss")
    plt.xlabel("Epoch"); plt.legend()
    plt.show()
```

Usage
```
histories = {
    "MobileNetV2": history_mobilenet,
    "ResNet50": history_resnet50,
    "VGG16": history_vgg16,
}
plot_histories(histories)
```

#### Visual inspection of predictions
```
def show_predictions(model, dataset, class_names, n=20, threshold=0.5):
    """
    Show n predictions from a tf.data dataset for a binary sigmoid model.
    """
    imgs, labs = [], []
    for batch_imgs, batch_labs in dataset.unbatch().take(n):
        imgs.append(batch_imgs.numpy())
        labs.append(int(batch_labs.numpy()))
    imgs = np.stack(imgs)
    labs = np.array(labs)

    # model predicts probabilities in [0,1] for class 1
    probs = model.predict(imgs, verbose=0).reshape(-1)
    preds = (probs >= threshold).astype(int)

    plt.figure(figsize=(20,7))
    for i in range(min(n, 20)):
        ok = preds[i] == labs[i]
        plt.subplot(4,5,i+1)
        plt.imshow(imgs[i].astype("uint8"))
        title = f"Pred: {class_names[preds[i]]}\n(True: {class_names[labs[i]]})"
        plt.title(title, color=("green" if ok else "red"), fontsize=9)
        plt.axis('off')
    plt.tight_layout(); plt.show()
```

Usage
```
class_names = train_dataset.class_names  # ['cats','dogs']
show_predictions(model_mobilenet, validation_dataset, class_names, n=20)
```



