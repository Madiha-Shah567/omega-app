import streamlit as st
import os

# Get current script directory
image_folder = os.getcwd()  # ✅ Fix: Streamlit me file use nahi hota
rolex_image = os.path.join(image_folder, "rolex.jpg")
omega_image = os.path.join(image_folder, "omega.jpg")

# Watch data
watches = {
    "Rolex Submariner": {
        "image": rolex_image,
        "features": [
            "Waterproof up to 300m",
            "Automatic movement",
            "Stainless steel case",
            "Ceramic bezel",
        ],
    },
    "Omega Speedmaster": {
        "image": omega_image,
        "features": [
            "Chronograph function",
            "Manual winding movement",
            "Hesalite crystal",
            "Moonwatch edition",
        ],
    },
}

# App Layout
st.title("Luxury Watches Showcase")
st.header("Select and View Your Favorite Watch")

# Watch Selection Dropdown
selected_watch = st.selectbox("Select a Watch", list(watches.keys()))

# Display selected watch details
if selected_watch:
    watch_data = watches[selected_watch]

    # ✅ Load Image Properly
    if os.path.exists(watch_data["image"]):
        with open(watch_data["image"], "rb") as img_file:
            img_bytes = img_file.read()
        st.image(img_bytes, caption=selected_watch, use_container_width=True)

    else:
        st.error(f"⚠ Image not found: {watch_data['image']}")

    st.subheader("Features")
    st.write("\n".join([f"- {feature}" for feature in watch_data["features"]]))

# Toggle for Contact Info
if st.checkbox("Show Contact Info"):
    st.write("📧 Email: example@example.com")
    st.write("📞 Phone: +1234567890")

# Styling for better UI
st.markdown(
    """
    <style>
    .stImage img {
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True,
)