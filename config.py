import os

CAMERA_ID = 0 # 0 for integrated cam, 1 for first external can ....
GPU_UNIT = -1 # -1 for CPU, 0 for first gpu, 1 for second, etc

PRIMARY_COLOR = '#E3FF00'
CANVAS_MAX_FPS = 30
CANVAS_SHOW_FPS = True

TRANSFORMATION_DISPLAY_TIME = 2000

MOCK_TRANSFORMATION_APPLIER = False
MOCK_FACEBOOK_UPLOAD = True


IMAGES_SAVE_PATH=f"{os.path.dirname(os.path.abspath(__file__))}/saved-transfers/"
