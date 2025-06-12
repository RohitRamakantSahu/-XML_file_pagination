import streamlit as st
from PIL import Image
from io import BytesIO
from main import parse_xml_feed  # Import the logic

def display_images(images, items_per_page=12):
    if not images:
        st.warning("No images found in the feed.")
        return
    
    # Display total count
    st.success(f"✅ Found {len(images)} image URLs")
    
    # Calculate total pages
    total_pages = (len(images) + items_per_page - 1) // items_per_page
    
    # Add pagination controls
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        page = st.selectbox("Page", range(1, total_pages + 1), index=0)
    
    # Calculate start and end indices for current page
    start_idx = (page - 1) * items_per_page
    end_idx = min(start_idx + items_per_page, len(images))
    
    # Display images in a grid
    cols = st.columns(4)  # 4 images per row
    for idx, image_url in enumerate(images[start_idx:end_idx]):
        col_idx = idx % 4
        with cols[col_idx]:
            try:
                import requests
                response = requests.get(image_url)
                if response.status_code == 200:
                    img = Image.open(BytesIO(response.content))
                    st.image(img)
                else:
                    st.error(f"Failed to load image: {image_url}")
            except Exception as e:
                st.error(f"Error loading image: {str(e)}")

def main():
    st.title("📸 XML Feed Image Viewer")
    
    # Input for feed URL
    feed_url = st.text_input(
        "📥 Paste your XML URL here",
        value="https://sparkiq-generated-images.s3.amazonaws.com/feeds/94e90189-9987-4e62-b0e3-d77c84140bbd.xml"
    )
    
    # Initialize session state for images
    if "images" not in st.session_state:
        st.session_state.images = []

    if st.button("Load Feed"):
        with st.spinner("Loading feed..."):
            try:
                images = parse_xml_feed(feed_url)
                st.session_state.images = images
            except Exception as e:
                st.error(str(e))

    # Use images from session state for display and pagination
    images = st.session_state.get("images", [])
    if images:
        display_images(images)
    else:
        st.info("No images loaded yet. Paste a feed URL and click 'Load Feed'.")

if __name__ == "__main__":
    main() 
