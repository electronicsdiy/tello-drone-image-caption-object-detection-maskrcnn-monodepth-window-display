import sys, cv2, math, time, datetime
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cvl
import time
import math
from timeout_decorator import timeout, TimeoutError
from djitellopy import Tello
from cvlib.object_detection import draw_bbox
from pprint import pprint
from create_caption_text import *

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
