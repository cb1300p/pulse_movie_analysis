# pulse_movie_analysis

## 概要
右手の人差し指をノートPCのカメラで動画撮影したものを,フレームごとに画像で分け, 輝度値等を分析する.
輝度値の微妙な変化により, 脈拍を視認する.
輝度値の変化からその値をグラフにプロットし, 脈の変化を示す.

## movie_preserve.pyの説明

### 動画からフレームごとに画像を保存する
画像処理を行うので, osとOpenCVの一種であるcv2をimportする.  
動画ファイルを読み込み, スクリーンキャプチャ（フレームごとの画像）を保存するディレクトリを作成.  
フレーム数を取得し, それぞれ "番号.png" の形で保存する.

### キャプチャ画像の輝度値平均を計算する
numpyを利用可能な環境にする.  
保存された'0.png'ファイルから'99.png'ファイルをimreadを用いて読み込む.  
(※また, 使用した動画は3.6sec(60fps)であったため, 3.6*60=216枚の画像が保存されていたが, 数が多かったため,100枚の写真に限定した(0.png~99.png). 60fpsなので100枚の写真ということは, 1.67secの動画分の画像を処理したことになる.)
for文等を用いてシンプルにコードを表現可能であるはずなのだが, 力量不足であり実現できなかった.
xに100個の配列を用意, yには1次元ベクトルに, 0.pngから99.pngの画像のそれぞれの平均輝度値を代入した.(.mean()関数利用)  
"plt.plot"でグラフをプロット. それより下の125〜129行でグラフのパラメータ等, 詳細を設定.  
131行目, plt.plotでグラフを表示.

### それぞれの画像の平均輝度値を出力
134~136行目のコードは, imreadした100枚のそれぞれの平均輝度値を出力するコードである.  
for文を用いて, シンプルにコードを記した.

## 実行結果
グラフは正しくプロットされた.
輝度値は256階調のうち, 73~78付近を上下した.(Max:77.7, Min:73.5)
脈を打つ度に肌表面の色が若干変化するためこのような結果になると推測できる.
先ほど述べた通り, このグラフは計測時間1.67秒分のグラフである.
グラフの山と谷を観察すると, 1.67秒でおよそ3.5周期していた.
1周期ごとに脈拍を1回打っていると仮定すると, 125bpmとなり, 動画を撮影した際の脈拍とは大きく値が異なる. 
2周期ごとに脈拍を1回打っていると仮定すると, 半分の63bpmとなり, これは動画を撮影した際の脈拍とほぼ同様の値となる.


## 参考URL/参考文献
動画をフレームごとに保存するPython Code ↓  
"Pythonでの動画の取り扱い（OpenCVで再生とキャプチャ生成）"
動画を1フレームごとに画像へ変換
https://www.tech-tech.xyz/opencv_video.html

## Python 実行環境
Microsoft Azure Notebooks Python3
Powered by Jupyter

## 追加で実行したモジュール等（余分なものが入っている可能性あり）
!pip install scikit-image==0.12.3
import numpy as np
from numpy.random import rand
from numpy import uint8, float32, float64, log, pi, sin, cos, abs, sqrt
import matplotlib.pyplot as plt
%matplotlib inline
plt.gray();
from matplotlib.pyplot import imshow
from skimage.io import imread, imsave
from skimage.color import rgb2gray, rgb2hsv
from skimage.transform import rotate, resize
import skimage
skmajor, skminor, sknumber = skimage.__version__.split(".")
if int(skminor) >= 11:
    from skimage.filters import threshold_otsu # version 0.11 and after
else:
    from skimage.filter import threshold_otsu # version 0.10 and before
from scipy.ndimage.filters import convolve
from __future__ import print_function, division
from os.path import getsize
from time import time
