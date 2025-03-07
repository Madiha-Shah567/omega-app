import streamlit as st
import os

# ✅ GitHub Image Handling (Raw URLs)
GITHUB_USERNAME = "Madiha-Shah567"
GITHUB_REPO = "watches-app"
IMAGES_FOLDER = "images"
GITHUB_BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/main/{IMAGES_FOLDER}/"

# ✅ Watch Data with Images (Local + GitHub)
watches = {
    "Rolex Submariner": {
        "image": "images/roni.jpg",
        "features": [
            "✅ Waterproof up to 300m",
            "✅ Automatic movement",
            "✅ Stainless steel case",
            "✅ Ceramic bezel",
            "✅ Scratch-resistant sapphire crystal",
            "✅ Luminescent hour markers",
            "✅ Unidirectional rotatable bezel for diving safety"
        ],
    },
    "Omega Speedmaster": {
        "image": "images/omega.jpg",
        "features": [
            "✅ Chronograph function",
            "✅ Manual winding movement",
            "✅ Hesalite crystal",
            "✅ Moonwatch edition",
            "✅ Tachymeter scale for speed measurement",
            "✅ Shock-resistant movement",
            "✅ Anti-magnetic properties for enhanced durability"
        ],
    },
}

# ✅ Streamlit App Layout
st.title("⌚ Luxury Watches Showcase")
st.write("Select a watch to view its details.")

# ✅ Watch Selector (Scroller)
selected_watch = st.radio("Select a Watch", list(watches.keys()), horizontal=True)

# ✅ Display Selected Watch Details
if selected_watch:
    watch_data = watches[selected_watch]

    # ✅ Check if Local Image Exists, Else Use GitHub
    image_path = watch_data["image"]
    if os.path.exists(image_path):
        st.image(image_path, caption=selected_watch, use_container_width=True)
    else:
        st.image(f"{GITHUB_BASE_URL}{os.path.basename(image_path)}", caption=selected_watch, use_container_width=True)

    # ✅ Show Features
    st.subheader("Features")
    st.write("\n".join(watch_data["features"]))

# ✅ Toggle Button for Contact Info
if st.checkbox("Show Contact Info"):
    st.subheader("📞 Contact Information")
    st.write("📧 Email: example@example.com")
    st.write("📞 Phone: +1234567890")