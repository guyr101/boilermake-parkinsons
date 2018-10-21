# Spiro

Devpost:https://devpost.com/software/spiro

## Major platforms Used
- Python
  - Keras
  - Pandas
  - Numpy
  - Matplotlib
- Swift
- Google Cloud Platform
- Firebase

## Features
- Convert points into images
- Train and run machine learning algorithm
- App where a user can take the spiral test
- Return predictions to the app
- Current Model:
  - 32 Convolutions
  - 10x10 size
  - 40x40 pools
  - 0.2 dropout
  - 128 dense
  - sigmoid activation
  - 20 batch size
  - 100 epochs


## Future Improvements
- Front End
  - Plot r vs. theta graph to gain another angle on the deviation
- Back End
  - Calculate a "score" by using the predicted probability of the spiral being generated by someone with Parkinson's
  - Retrain model when enough new data is aggregated in the Firebase database


## Thoughts
- Treat data as image with pixel values vs. time series of the spiral path points
- Pixel value from 500x500 to 125x125
- The model initially assumed that everyone had Parkinson's, so it would have a 75% accuracy due to the makeup of our initial dataset.
- For the machine learning model, we duplicated the data points of the control so we would have a 50-50 split between control and Parkinson's points. This should not contribute to overfitting because of the dropout, which adds a random perturbation in the model.
- There are many images in which the model has a better detection than human intuition, as seen in has_parkinsons.png and does_not_have_parkinsons.png
