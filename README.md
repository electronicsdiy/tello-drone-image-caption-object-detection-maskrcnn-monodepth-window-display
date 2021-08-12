# tello-drone-image-caption-object-detection-maskrcnn-monodepth-window-display

![frame_img_shot_2021年08月12日14:41:58](https://user-images.githubusercontent.com/87643752/129156669-ae8d8fb2-1346-4463-9c11-10019e67105c.jpg)

![frame_img_shot_2021年08月12日14:41:25](https://user-images.githubusercontent.com/87643752/129156906-2a0dc44a-7112-41b1-b910-6ab00291665a.jpg)

![frame_img_shot_2021年08月12日14:41:40](https://user-images.githubusercontent.com/87643752/129156798-1c969b82-b7e1-4800-ba81-a53854fc0781.jpg)

![frame_img_shot_2021年08月12日14:42:19](https://user-images.githubusercontent.com/87643752/129156693-02e7a2f9-505a-45af-a2e6-e407393d2616.jpg)

## 実行方法

ます最初に、Telloに電源のオンにします。
MacbookとTelloをWifiで接続してください。
（Tello: Wifi親機（ホスト）、Macbook：Wifi子機(クライアント)）

__**examples/直下で、次を実行してください、**__

> python3 tello_camera_image_captioned_description_masked_rcnn_depth_window.py

* Terminalに大量のメッセージが吐き出され始めます。
* しばらく待つと、ウィンドウが立ち上がります。
* キーボードの**i**を押下すると、Telloが離陸します。
* キーボードの**g**を押下すると、Telloが離陸します。
* 終了させるときは、Terminalで**CTRL-C**もしくは**CTRL-Z**を押してください。


## 事前準備

**MASK-RCNN**の実装コードは、次のリポジトリのものを使っています。

* https://github.com/spmallick/learnopencv/blob/master/Mask-RCNN/README.md

### examples/直下で以下を実行してください

**上記のspmallick/learnopencv/blob/master/Mask-RCNNリポジトリの指示に従い、次のコマンドを実行する。**

```bash:
wget http://download.tensorflow.org/models/object_detection/mask_rcnn_inception_v2_coco_2018_01_28.tar.gz
tar zxvf mask_rcnn_inception_v2_coco_2018_01_28.tar.gz
```

### ezamples/models/直下で以下を実行してください

画像のキャプション文を生成する処理は、次のリポジトリの資源を借用しています。

次のリポジトリの指示通り、DropBoxから学習済みのモデルとボキャブラリファイルをダウンロードしてください。
ダウンロード後、次に述べるディレクトリに格納します。

* https://github.com/yunjey/pytorch-tutorial/tree/master/tutorials/03-advanced/image_captioning

> **Pretrained model**
>
> If you do not want to train the model from scratch, you can use a pretrained model. You can download the pretrained model **here** and the vocabulary file **here**. You should extract pretrained_model.zip to ./models/ and vocab.pkl to ./data/ using unzip command.

#### **1. 以下から学習済みのモデルファイル（pretrained_modex.zip）をダウンロードし、zipを解凍後、中にある以下の２つのファイルを、example/modelsの直下に格納してください。**

- decoder-5-3000.pkl
- encoder-5-3000.pkl

https://www.dropbox.com/s/ne0ixz5d58ccbbz/pretrained_model.zip?dl=0

#### **2. 2つのファイルをコピーして、以下の別名で同じディレクトリ（example/modelsの直下）に保存する。最初の「5-3000」名の2つのファイルは削除しない。**

- encoder-5-3000.ckpt → encoder-2-1000.ckpt
- decoder-5-3000.ckpt → decoder-2-1000.ckpt

#### **2. 以下から学習済みのボキャブラリファイル（vpcap.zip）をダウンロードして、zipファイルを解凍後、中にあるvocab.pklファイルを、example/dataの直下に格納してください。**

https://www.dropbox.com/s/26adb7y9m98uisa/vocap.zip?dl=0


#### **3. 外部のURLから、zipファイルをダウンロードして下さい。zipファイルのまま、解答せずにコードは動きます。**

単眼カメラ画像の深度推定を行う部分は、次のリポジトリの実装コードを利用しています。

* https://github.com/nianticlabs/monodepth2

このリポジトリには、次の一文があります。

> On its first run either of these commands will download the mono+stereo_640x192 pretrained model (99MB) into the models/ folder. We provide the following options for --model_name:

上記の指示に従い、次のURLから、zipファイルをダウンロードして下さい。zipは解凍せずに、zipファイルのまま格納してください。

* https://storage.googleapis.com/niantic-lon-static/research/monodepth2/mono_640x192.zip

このzipファイルは、次のスクリプトファイルの104行目にあるメソッドから読み込まれます。

**呼び出し元のスクリプトファイル**

* tello-drone-image-caption-object-detection-maskrcnn-monodepth-window-display/examples/utils.py

**104行目**

> download_model_if_doesnt_exist
>    urllib.request.urlretrieve(model_url, model_path + ".zip")
