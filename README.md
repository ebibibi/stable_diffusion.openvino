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
docker build . -t stable_diffusion.openvino:latest
docker run --rm -p 8501:8501 stable_diffusion.openvino:latest
```

上記コマンドを実行してしばらく（環境によりますが1時間くらい待つつもりでよいと思います）待つと「You can now view your Streamlit app in your browser.」と表示されます。

その後、ブラウザを使って http://localhost:8501 にアクセスすれば利用可能です。