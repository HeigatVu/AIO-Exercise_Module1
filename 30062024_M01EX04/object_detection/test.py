import numpy as np
from PIL import Image
import streamlit as st
import object_detection


def main():
    st.title("Object Detection for Image")
    file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    if file is not None:
        st.image(file, caption="Upload Image")

        image = Image.open(file)
        image = np.array(image)
        detections = object_detection.process_image(image)
        processed_image = object_detection.annotate_image(image, detections)
        st.image(processed_image, caption="Processed Image")


if __name__ == "__main__":
    main()
