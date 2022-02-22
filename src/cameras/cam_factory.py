from src.cameras.cam_singleton import get_or_create_cams
from src.cameras.opencv_camera import OpenCVCamera


def create_opencv_cams():
    cams = get_or_create_cams()
    raw_webcam_obj = cams.cams_to_use
    cv_cams = [
        OpenCVCamera(webcam_id=webcam.webcam_id)
        for webcam in raw_webcam_obj
        if int(webcam.webcam_id) < 3
    ]
    for cv_cam in cv_cams:
        cv_cam.connect()
    return cv_cams
