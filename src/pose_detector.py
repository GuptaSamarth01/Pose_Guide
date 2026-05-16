import cv2
import mediapipe as mp
import numpy as np


class PoseDetector:

    def __init__(self):

        # MediaPipe Pose
        self.mp_pose = mp.solutions.pose

        # MediaPipe Drawing
        self.mp_drawing = mp.solutions.drawing_utils

        # MediaPipe Selfie Segmentation
        self.mp_selfie_segmentation = mp.solutions.selfie_segmentation

        # Pose Model
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        # Segmentation Model
        self.selfie_segmentation = self.mp_selfie_segmentation.SelfieSegmentation(
            model_selection=1
        )

        # Important landmarks
        self.landmark_ids = {
            "LEFT_SHOULDER": 11,
            "RIGHT_SHOULDER": 12,
            "LEFT_HIP": 23,
            "RIGHT_HIP": 24,
            "LEFT_ANKLE": 27,
            "RIGHT_ANKLE": 28
        }

    def detect_pose(self, frame):

        # Create copy
        output_frame = frame.copy()

        # Convert BGR → RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process pose detection
        pose_results = self.pose.process(rgb_frame)

        # Process segmentation
        segmentation_results = self.selfie_segmentation.process(rgb_frame)

        # Landmark dictionary
        landmarks = {}

        # Get image dimensions
        height, width, _ = frame.shape

        # ==========================
        # SEGMENTATION MASK
        # ==========================

        segmentation_mask = segmentation_results.segmentation_mask

        # Convert probability mask to binary mask
        condition = segmentation_mask > 0.5

        binary_mask = np.zeros((height, width), dtype=np.uint8)

        binary_mask[condition] = 255

        # ==========================
        # POSE LANDMARKS
        # ==========================

        if pose_results.pose_landmarks:

            # Draw skeleton
            self.mp_drawing.draw_landmarks(
                output_frame,
                pose_results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS
            )

            # Extract selected landmarks
            for name, idx in self.landmark_ids.items():

                landmark = pose_results.pose_landmarks.landmark[idx]

                # Convert normalized → pixel coordinates
                x = int(landmark.x * width)
                y = int(landmark.y * height)

                # Store coordinates
                landmarks[name] = (x, y)

                # Draw landmark point
                cv2.circle(output_frame, (x, y), 6, (0, 255, 0), -1)

                # Draw label
                cv2.putText(
                    output_frame,
                    name,
                    (x + 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 255),
                    1
                )

        return {
            "frame": output_frame,
            "mask": binary_mask,
            "landmarks": landmarks
        }