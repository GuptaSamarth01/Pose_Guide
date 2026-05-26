import streamlit as st
import cv2
import tempfile
import os
import glob

from src.pose_detector import PoseDetector


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="PoseGuide",
    layout="wide"
)


# =====================================
# CUSTOM CSS
# =====================================

st.markdown(
    """
    <style>

    .main {
        background-color: #0f172a;
    }

    h1 {
        text-align: center;
        color: white;
    }

    .body-type {
        font-size: 32px;
        font-weight: bold;
        color: #38bdf8;
        text-align: center;
        margin-top: 20px;
    }

    .confidence {
        font-size: 22px;
        color: #facc15;
        text-align: center;
        margin-bottom: 30px;
    }

    .card {
        background-color: #1e293b;
        padding: 10px;
        border-radius: 16px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =====================================
# TITLE
# =====================================

st.title("PoseGuide: AI Pose Recommendation Engine")

st.markdown(
    """
    <div style='text-align:center;color:lightgray;'>
    Upload a full body image and get pose recommendations.
    </div>
    """,
    unsafe_allow_html=True
)


# =====================================
# LOAD DETECTOR
# =====================================

@st.cache_resource
def load_detector():

    return PoseDetector()


detector = load_detector()


# =====================================
# POSE FOLDERS
# =====================================

POSE_FOLDERS = {
    "Oval": "poses/oval",
    "Triangle": "poses/triangle",
    "Rectangle": "poses/rectangle",
    "Trapezium": "poses/trapezium",
    "Inverted Triangle": "poses/inverted_triangle"
}


# =====================================
# FILE UPLOADER
# =====================================

uploaded_file = st.file_uploader(
    "Upload Full Body Image",
    type=["jpg", "jpeg", "png"]
)


# =====================================
# PROCESS IMAGE
# =====================================

if uploaded_file is not None:

    # =====================================
    # SAVE TEMP FILE
    # =====================================

    temp_file = tempfile.NamedTemporaryFile(
        delete=False
    )

    temp_file.write(uploaded_file.read())

    # =====================================
    # READ IMAGE
    # =====================================

    frame = cv2.imread(temp_file.name)

    if frame is None:

        st.error("Failed to read image.")

    else:

        # =====================================
        # RUN DETECTOR
        # =====================================

        result = detector.detect_pose(frame)

        # =====================================
        # CONVERT IMAGE FOR STREAMLIT
        # =====================================

        display_frame = cv2.cvtColor(
            result["frame"],
            cv2.COLOR_BGR2RGB
        )

        # =====================================
        # SHOW ANALYSIS IMAGE
        # =====================================

        st.image(
            display_frame,
            caption="Body Analysis",
            use_container_width=True
        )

        # =====================================
        # BODY TYPE
        # =====================================

        body_type = result["body_type"]

        confidence = result["confidence"]

        body_ratio = result["body_ratio"]

        # =====================================
        # DISPLAY BODY DETAILS
        # =====================================

        st.markdown(
            f'''
            <div class="body-type">
            Detected Body Type: {body_type}
            </div>
            ''',
            unsafe_allow_html=True
        )

        st.markdown(
            f'''
            <div class="confidence">
            Confidence Score: {confidence}%
            </div>
            ''',
            unsafe_allow_html=True
        )

        if body_ratio is not None:

            st.markdown(
                f"""
                <div style='text-align:center;
                            color:white;
                            font-size:20px;
                            margin-bottom:20px;'>
                Shoulder/Waist Ratio: {body_ratio:.2f}
                </div>
                """,
                unsafe_allow_html=True
            )

        # =====================================
        # LOAD RECOMMENDATIONS
        # =====================================

        folder = POSE_FOLDERS.get(body_type)

        if folder and os.path.exists(folder):

            image_paths = glob.glob(
                os.path.join(folder, "*.jpg")
            )

            image_paths.extend(
                glob.glob(
                    os.path.join(folder, "*.png")
                )
            )

            if len(image_paths) > 0:

                st.subheader(
                    "Recommended Poses"
                )

                cols = st.columns(3)

                for index, image_path in enumerate(image_paths):

                    image = cv2.imread(image_path)

                    if image is None:
                        continue

                    image = cv2.cvtColor(
                        image,
                        cv2.COLOR_BGR2RGB
                    )

                    with cols[index % 3]:

                        st.markdown(
                            "<div class='card'>",
                            unsafe_allow_html=True
                        )

                        st.image(
                            image,
                            use_container_width=True
                        )

                        st.markdown(
                            f"""
                            <div style='text-align:center;
                                        color:white;
                                        margin-top:10px;'>
                            Pose {index + 1}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                        st.markdown(
                            "</div>",
                            unsafe_allow_html=True
                        )

            else:

                st.warning(
                    f"No pose images found for {body_type}"
                )

        else:

            st.warning(
                f"Pose folder not found for {body_type}"
            )