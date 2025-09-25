# AoL-AI_VGG16
Deepfake Detector using VGG16 model

## dataset 
There is an ipynb file that contains code for training the VGG16 model with a dataset from kaggle : https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images

## model and setup
Deepfake_Detector folder and its zipped files is a folder that can be run using streamlit with the command ‘streamlit run main.py’. The model ‘best_model.tflite’ can be downloaded at https://huggingface.co/MichaelIvanS/VGG16-Deepfake/resolve/main/best_model.tflite and then put into the 'assets' folder before running streamlit

## mobile app
We also created a mobile application using Android Studio with this model that can be downloaded as the APK file of the application via this following link: https://huggingface.co/MichaelIvanS/VGG16-Deepfake/resolve/main/deepfakedetector.apk . The folder named DeepfakeDetector contains several files from Android Studio that are considered important, not all files or folders are provided because the size will be too large. However, there is a drawback in this project where the dataset used is less suitable for its use, namely detecting deepfakes so that it will be less accurate in practice. So I and my new team created a similar project but with a better dataset and model creation to detect waste classification: organic or recyclable which can be accessed at the following link: https://github.com/Mis-291205/AoL-MachineLearning
