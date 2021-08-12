from __future__ import absolute_import, division, print_function
from timeout_decorator import timeout, TimeoutError
from djitellopy import Tello
import cv2, math, time
import os
import sys
import glob
import argparse
import numpy as np
import PIL.Image as pil
import matplotlib as mpl
import matplotlib.cm as cm
import numpy
import torch
import cvlib as cvl
import datetime
from cvlib.object_detection import draw_bbox
from torchvision import transforms, datasets

TIMEOUT_SEC = 0.1

@timeout(TIMEOUT_SEC)
def input_with_timeout(msg=None):
   return input(msg)


tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

#tello.takeoff()

while True:
    # In reality you want to display frames in a seperate thread. Otherwise
    #  they will freeze while the drone moves.
    img = frame_read.frame
    original_image = img.copy()
    #bitwised_img = cv2.bitwise_not(img)
    
    #https://stackoverflow.com/questions/64546859/combine-several-canny-edge-detection-in-one-window-using-opencv-python
    b,g,r = cv2.split(img)
    b_edge = cv2.Canny(b,30,50)
    g_edge = cv2.Canny(g,30,50)
    r_edge = cv2.Canny(r,30,50)
    edge_img = cv2.merge([b_edge, g_edge, r_edge])
    #canny_img = cv2.Canny(img, 100, 200)
    #cv2.imshow("frame_canny", canny_img)
    #MonoDepth2モデル
    depth_image = mono_depth2(img)
    
    #フレーム画像の物体検出（輪郭線描画）及び指定オブジェクトの検出個数の説明文字列埋込み
    label_name  = "person"
    bbox, label, conf = cvl.detect_common_objects(img)
    output_image = draw_bbox(img, bbox, label, conf)
    #dt_now = datetime.datetime.now()
    message = "Num of detected {0}(s) is {1}".format(label_name, str(label.count(label_name)))
    input_text_0 = message
    cv2.putText(output_image, str(input_text_0), (0, 50), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

    #https://djitellopy.readthedocs.io/en/latest/tello/#djitellopy.tello.Tello.query_battery
    time_of_flight_distance_senser_val = tello.get_distance_tof()
    input_text_1 = "ToF Distane {0} cm".format(time_of_flight_distance_senser_val)

    height= tello.get_height()
    input_text_2 = "Height {0} cm".format(height)

    # カメラ画像にTelloの現在高度（ToFセンサ計測距離(cm)、高さ（cm)）を埋込む
    cv2.putText(output_image, str(input_text_1), (0, 100), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(output_image, str(input_text_2), (0, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
    
    #numpyのhstack, hstackでなくても、opencv2のcv2.vconcat, hconcatも使える
    merged_image_group_1 = cv2.hconcat((original_image, edge_img))
    merged_image_group_2 = cv2.hconcat((output_image, depth_image))
    finally_merged_image = cv2.vconcat((merged_image_group_1, merged_image_group_2))
    cv2.imshow("Windows", finally_merged_image)
    #次の行（key = cv2.・・・）を削除すると、画像が受信できなくなる。
    key = cv2.waitKey(1) & 0xff
    
    try:
        msg = input_with_timeout('\n{}秒以内に操作コマンドを入力して下さい :'.format(TIMEOUT_SEC))
        print('\n操作コマンド：　{} を受信しました。\n'.format(msg))
        if msg == "i":
            tello.takeoff()
        elif msg == "w":
            tello.move_forward(30)
        elif msg == "s":
            tello.move_back(30)
        elif msg == "a":
            tello.move_left(30)
        elif msg == "d":
            tello.move_right(30)
        elif msg == "e":
            tello.rotate_clockwise(30)
        elif msg == "q":
            tello.rotate_counter_clockwise(30)
        elif msg == "r":
            tello.move_up(30)
        elif msg == "f":
            tello.move_down(30)
        elif msg == "g":
            tello.land()
    except TimeoutError:
        print('\n操作コマンド入力時間切れ。次のフレーム画像を読み込みます。\n')

tello.land()
