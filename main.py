import cv2
from src.pose_detector import PoseDetector


def main():

    # Webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot access webcam")
        return

    detector = PoseDetector()

    captured = False
    frozen_result = None

    while True:

        # ==========================
        # LIVE PREVIEW MODE
        # ==========================

        if not captured:

            ret, frame = cap.read()

            if not ret:
                break

            # Mirror view
            frame = cv2.flip(frame, 1)

            # Instructions
            cv2.putText(
                frame,
                "Press SPACE to Capture",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.imshow("PoseGuide", frame)

        # ==========================
        # FROZEN ANALYSIS MODE
        # ==========================

        else:

            cv2.imshow("PoseGuide", frozen_result["frame"])
            cv2.imshow("Segmentation Mask", frozen_result["mask"])

        # ==========================
        # KEYBOARD CONTROLS
        # ==========================

        key = cv2.waitKey(1)

        # SPACE → Capture
        if key == 32 and not captured:

            result = detector.detect_pose(frame)

            frozen_result = result

            captured = True

            print("\n===== LANDMARKS =====")

            for name, coords in result["landmarks"].items():
                print(f"{name}: {coords}")

        # R → Reset
        elif key == ord('r'):

            captured = False
            frozen_result = None

        # Q → Quit
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()