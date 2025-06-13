import streamlit as st
from app import process_image, show_transparent_mask

def main():
    st.set_page_config(page_title="Transparency Detector", layout="centered")

    st.title("🔍 Image Transparency Detector")
    st.write(
        "Upload an image (PNG, WebP, etc). The app will check for transparent pixels. "
        "Optionally, view a mask highlighting transparency."
    )

    uploaded = st.file_uploader("Choose an image file", type=["png", "webp"])

    if uploaded:
        # Process the image using the core functionality
        result = process_image(uploaded)
        
        # Display the uploaded image
        st.image(result['image'], caption="Uploaded Image", use_column_width=True)
        
        # Show transparency statistics
        st.markdown(
            f"**Transparent pixels:** `{result['transparent_pixels']}` out of "
            f"`{result['total_pixels']}` (`{100*result['transparent_pixels']/result['total_pixels']:.2f}%`)"
        )
        
        # Display transparency status
        if result['has_transparency']:
            st.success("This image HAS transparency!")
            if st.checkbox("Show transparent area mask?"):
                mask_img = show_transparent_mask(result['alpha'])
                st.image(mask_img, caption="Transparent Pixels Highlighted (Red)", use_column_width=True)
        else:
            st.info("This image does NOT have transparency.")

    st.caption("Built with ❤️ using Streamlit & Pillow")

if __name__ == "__main__":
    main() 