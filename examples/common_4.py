from __future__ import absolute_import, division, print_function
import sys, cv2, math, time, datetime, os, glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
import cvlib as cvl
import PIL.Image as pil
import torch
from cvlib.object_detection import draw_bbox
from timeout_decorator import timeout, TimeoutError
from djitellopy import Tello
from pprint import pprint
from create_caption_text import *
from get_mask_rcnn_image import *
from depth_frame import *
from torchvision import transforms, datasets
from timeout_decorator import timeout, TimeoutError
from djitellopy import Tello

# Esc キー
ESC_KEY = 0x1b
# モーションの残存期間(sec)
DURATION = 1.0
# 全体の方向を表示するラインの長さ
LINE_LENGTH_ALL = 60
# 座標毎の方向を表示するラインの長さ
LINE_LENGTH_GRID = 20
# 座標毎の方向を計算する間隔
GRID_WIDTH = 40
# 方向を表示するラインの丸の半径
CIRCLE_RADIUS = 2
