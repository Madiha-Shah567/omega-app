import streamlit as st
import os

# ✅ Local Image Handling
image_folder = os.getcwd()
watches = {
    "Rolex Submariner": {
        "image": os.path.join(image_folder, "roni.jpg"),
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
        "image": os.path.join(image_folder, "omega.jpg"),
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

    # ✅ Show Image
    if os.path.exists(watch_data["image"]):
        st.image(watch_data["image"], caption=selected_watch, use_container_width=True)
    else:
        st.error("⚠ Image not found!")

    # ✅ Show Features
    st.subheader("Features")
    st.write("\n".join(watch_data["features"]))

# ✅ Toggle Button for Contact Info
if st.checkbox("Show Contact Info"):
    st.subheader("📞 Contact Information")
    st.write("📧 Email: example@example.com")
    st.write("📞 Phone: +1234567890")

# ✅ UI Styling
st.markdown(
    """
    <style>
    .stImage img {
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
    }
    .stRadio div[role=radio] {
        background: #f0f0f0;
        border-radius: 10px;
        padding: 10px;
        margin: 5px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True,
)