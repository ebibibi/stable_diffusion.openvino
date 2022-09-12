# このレポジトリについて
[bes-dev/stable_diffusion.openvin](https://github.com/bes-dev/stable_diffusion.openvino)からforkしてほんの少しだけ修正したものです。

# 使い方
## 前提条件
- dockerが動く環境
- Intel CPU
- それなりのメモリ（16GBあれば動くことは確認しました）

## コンテナーのビルドと実行
```
git clone https://github.com/ebibibi/stable_diffusion.openvino.git
cd stable_diffusion.openvino
sudo docker build . -t stable_diffusion.openvino:latest
sudo docker run --rm -p 8501:8501 stable_diffusion.openvino:latest
```

上記コマンドを実行してしばらく待つと（環境によりますが1時間くらい待つつもりでよいと思います）「You can now view your Streamlit app in your browser.」と表示されます。

その後、ブラウザを使って http://localhost:8501 にアクセスすれば利用可能です。
もちろん同一ネットワーク上のほかのホストから http://IPアドレス:8501 or http://ホスト名:8501 等でもアクセス可能です。

画像を大量に生成したい場合には一番最後の行を下記のように変更してcreateimages.pyを実行すると捗ります。

```
# Linxの場合
sudo docker run -v $(pwd)/output:/tmp/output stable_diffusion.openvino:latest python3 createimages.py "ここにPromptを書く"

# Windowsの場合
sudo docker run -v "$(pwd)\output":/tmp/output stable_diffusion.openvino:latest python3 createimages.py "ここにPromptを書く"
```