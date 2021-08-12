# tello-drone-image-caption-object-detection-maskrcnn-monodepth-window-display

**MASK-RCNN**の実装コードは、次のリポジトリのものを使っています。

* https://github.com/spmallick/learnopencv/blob/master/Mask-RCNN/README.md

#### examples/直下で以下を実行してください

**上記のspmallick/learnopencv/blob/master/Mask-RCNNリポジトリの指示に従い、次のコマンドを実行する。**

```bash:
wget http://download.tensorflow.org/models/object_detection/mask_rcnn_inception_v2_coco_2018_01_28.tar.gz
tar zxvf mask_rcnn_inception_v2_coco_2018_01_28.tar.gz
```

#### models/直下で以下を実行してください

画像のキャプション文を生成する処理は、次のリポジトリの資源を借用しています。

次のリポジトリの指示通り、DropBoxから学習済みのモデルとボキャブラリファイルをダウンロードしてください。
ダウンロード後、次に述べるディレクトリに格納します。

* https://github.com/yunjey/pytorch-tutorial/tree/master/tutorials/03-advanced/image_captioning

**1. 以下から学習済みのモデルファイルをダウンロードし、ファイル名を変更後、example/modelsの直下に格納してください。**

- decoder-5-3000.pkl
- encoder-5-3000.pkl

https://www.dropbox.com/s/ne0ixz5d58ccbbz/pretrained_model.zip?dl=0

ファイル名の変更

- encoder-5-3000.pkl → encoder-2-1000.ckpt
- decoder-5-3000.pkl → decoder-2-1000.ckpt

**2. 以下から学習済みのボキャブラリファイルをダウンロードし、example/dataの直下に格納してください。**

https://www.dropbox.com/s/26adb7y9m98uisa/vocap.zip?dl=0


