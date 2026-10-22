import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.tree import DecisionTreeClassifier
from support_functions import plot_confusion_matrix, generate_features_targets

np.random.seed(0)

# copy your splitdata_train_test function here
def splitdata_train_test(data, fraction_training):
  np.random.shuffle(data)
  # complete this function
  split = int(fraction_training*data.shape[0])
  training_set = data[:split]
  testing_set = data[split:]
  return training_set, testing_set

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



# complete this function by splitting the data set and training a decision tree classifier
def dtc_predict_actual(data):
  # split the data into training and testing sets using a training fraction of 0.7
  training_set, testing_set = splitdata_train_test(data, fraction_training = 0.7)
  # generate the feature and targets for the training and test sets
  # i.e. train_features, train_targets, test_features, test_targets
  train_features, train_targets = generate_features_targets(training_set)
  test_features, test_targets = generate_features_targets(testing_set)

  # instantiate a decision tree classifier
  model = DecisionTreeClassifier()
  # train the classifier with the train_features and train_targets
  model.fit(train_features, train_targets)
  # get predictions for the test_features
  predictions = model.predict(test_features)
  # return the predictions and the test_targets
  return predictions, test_targets


# Implement the following function
def calculate_accuracy(predicted, actual):
  accuracy = np.mean(predicted == actual)
  return accuracy


if __name__ == "__main__":
  data = np.load('galaxy_catalogue.npy')

  # split the data
  features, targets = generate_features_targets(data)

  # train the model to get predicted and actual classes
  dtc = DecisionTreeClassifier()
  predicted = cross_val_predict(dtc, features, targets, cv=10)

  # calculate the model score using your function
  model_score = calculate_accuracy(predicted, targets)
  print("Our accuracy score:", model_score)

  # calculate the models confusion matrix using sklearns confusion_matrix function
  class_labels = list(set(targets))
  model_cm = confusion_matrix(y_true=targets, y_pred=predicted, labels=class_labels)

  # Plot the confusion matrix using the provided functions.
  plt.figure()
  plot_confusion_matrix(model_cm, classes=class_labels, normalize=False)
  plt.show()

