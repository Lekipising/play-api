# Object Detection Flask API

This is a flask API that is used to detect objects in an image file. It was trained on CIFAR-10 dataset.
The Deep Learning model is a Convolutional Neural Network (CNN) that predicts 10 classes of objects.

The flask endpoint `/detect` accepts a image file and json with probabilities of the different classes.

The API is deployed on Render and can be accessed on https://play-api.onrender.com

The API is consumed by a frontend on the following link: [https://play-classify-score.vercel.app/](https://play-classify-score.vercel.app/)
