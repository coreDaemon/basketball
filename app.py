import streamlit as st

# Set page config
st.set_page_config(
    page_title="Basketball",
    page_icon="🏀",
    layout="wide"
)

# Main title
st.title("🏀 Basketball")

# Video upload section
st.header("Upload Video")

uploaded_file = st.file_uploader(
    "Choose a video file",
    type=['mp4', 'avi', 'mov', 'mkv', 'wmv'],
    help="Upload a basketball video for analysis"
)

if uploaded_file is not None:
    # Display video details
    st.success(f"Video uploaded: {uploaded_file.name}")
    st.write(f"File size: {uploaded_file.size} bytes")
    
    # Display the video
    st.video(uploaded_file)
    
    # Additional options when video is uploaded
    st.subheader("Video Options")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Analyze Video"):
            st.info("Video analysis feature coming soon!")
    
    with col2:
        if st.button("Download Video"):
            st.download_button(
                label="Download",
                data=uploaded_file.getvalue(),
                file_name=uploaded_file.name,
                mime="video/mp4"
            )
else:
    st.info("Please upload a video file to get started.")

# Sidebar with additional info
st.sidebar.header("About")
st.sidebar.write("This is a basketball video analysis app. Upload your basketball videos to get started!")