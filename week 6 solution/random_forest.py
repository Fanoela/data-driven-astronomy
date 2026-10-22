import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from support_functions import generate_features_targets, plot_confusion_matrix, calculate_accuracy

np.random.seed(0)


# copy your generate_features_targets function here
def generate_features_targets(data):
  # complete the function by calculating the concentrations
  conc_u = data['petroR50_u'] / data['petroR90_u']
  conc_r = data['petroR50_r'] / data['petroR90_r']
  conc_z = data['petroR50_z'] / data['petroR90_z']
  targets = data['class']

  features = np.empty(shape=(len(data), 13))
  features[:, 0] = data['u-g']
  features[:, 1] = data['g-r']
  features[:, 2] = data['r-i']
  features[:, 3] = data['i-z']
  features[:, 4] = data['ecc']
  features[:, 5] = data['m4_u']
  features[:, 6] = data['m4_g']
  features[:, 7] = data['m4_r']
  features[:, 8] = data['m4_i']
  features[:, 9] = data['m4_z']

  # fill the remaining 3 columns with concentrations in the u, r and z filters
  # concentration in u filter
  features[:, 10] = conc_u
  # concentration in r filter
  features[:, 11] = conc_r
  # concentration in z filter
  features[:, 12] = conc_z

  return features, targets


def calculate_accuracy(predicted, actual):
  accuracy = np.mean(predicted == actual)
  return accuracy

# complete this function to get predictions from a random forest classifier
def rf_predict_actual(data, n_estimators):
  #np.shuffle(data)
  # generate the features and targets
  features, targets = generate_features_targets(data)
  # instantiate a random forest classifier using n estimators
  model = RandomForestClassifier(n_estimators=n_estimators)
  # get predictions using 10-fold cross validation with cross_val_predict
  predictions = cross_val_predict(model, X = features, y = targets, cv = 10)
  # return the predictions and their actual classes
  return predictions, targets

if __name__ == "__main__":
  data = np.load('galaxy_catalogue.npy')

  # get the predicted and actual classes
  number_estimators = 50              # Number of trees
  predicted, actual = rf_predict_actual(data, number_estimators)

  # calculate the model score using your function
  accuracy = calculate_accuracy(predicted, actual)
  print("Accuracy score:", accuracy)

  # calculate the models confusion matrix using sklearns confusion_matrix function
  class_labels = list(set(actual))
  model_cm = confusion_matrix(y_true=actual, y_pred=predicted, labels=class_labels)

  # plot the confusion matrix using the provided functions.
  plt.figure()
  plot_confusion_matrix(model_cm, classes=class_labels, normalize=False)
  plt.show()

