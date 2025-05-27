import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf # TensorFlow Lite Interpreter

def homePage():
        # Fungsi untuk memuat model .tflite
    def load_model(model_path):
        interpreter = tf.lite.Interpreter(model_path=model_path) #interpreter agar model bisa digunakan di python, karena model .tflite berisi kode biner yang tidak bisa digunakan secara langsung
        interpreter.allocate_tensors() #mengalokasikan tensor(struktur data) yang diperlukan model untuk bekerja 
        return interpreter

    # Fungsi untuk memproses gambar
    def preprocess_image(image, target_size):
        # Ubah ukuran gambar sesuai ukuran input model
        img = image.resize(target_size) #diubah jadi ukuran yang diminta model (VGG-16 menggunakan 224*224)
        img_array = np.array(img) / 255.0  # Normalisasi = proses mengubah nilai dalam dataset ke dalam skala tertentu untuk memastikan distribusi data konsisten dan cocok untuk model atau analisis tertentu
        img_array = np.expand_dims(img_array, axis=0).astype(np.float32)  # Tambahkan dimensi batch
        return img_array

    # Fungsi untuk prediksi dengan model .tflite
    def predict_image(interpreter, image):
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        # Ambil ukuran input yang diharapkan model
        input_shape = input_details[0]['shape']  #memuat input yang diharapkan model {1 x 224 x 224 x 3}
        target_size = (input_shape[1], input_shape[2])  # Width x Height

        # Proses gambar sesuai ukuran model
        input_data = preprocess_image(image, target_size)
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()

        # Ambil output prediksi
        output_data = interpreter.get_tensor(output_details[0]['index'])

        # Tentukan label berdasarkan probabilitas
        labels = ["FAKE", "REAL"]  # Sesuaikan label dengan urutan output model
        predicted_label = labels[np.argmax(output_data)]  # Ambil indeks probabilitas tertinggi
        return predicted_label, output_data

    # Muat model TensorFlow Lite
    model_path = 'assets\\best_model.tflite'  # Ganti dengan path model Anda
    interpreter = load_model(model_path)

    # Antarmuka pengguna Streamlit
    st.title('Deepfake Detector')
    uploaded_image = st.file_uploader("Unggah gambar", type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Gambar yang diunggah", use_container_width=True)

        # Prediksi dan tampilkan hasil
        predicted_label, prediction = predict_image(interpreter, image)
        if predicted_label == "REAL":
            st.markdown(f"""
                    <h2 style='color: green;
                    font-size: 42px;
                    text-align: center;'
                    >Result: {predicted_label}</h2>""", unsafe_allow_html=True)
            st.markdown("""
                    <h2 style='color: green;
                    font-size: 28px;
                    text-align: center;'
                    >Congratulations! Your image is safe and can be trusted</h2>""", unsafe_allow_html=True)
            
        else:
            st.markdown(f"""
                    <h2 style='color: red;
                    font-size: 42px;
                    text-align: center;'
                    >Result: {predicted_label}</h2>""", unsafe_allow_html=True)
            st.markdown("""
                    <h2 style='color: red;
                    font-size: 28px;
                    text-align: center;'
                    >This is an AI Image, be careful of fraud using AI images! If you feel this image is dangerous, please notify the authorities.</h2>""", unsafe_allow_html=True)
        st.write("*Deepfake Detector is not 100% accurate, please recheck and validate the result with the authorities")
        
