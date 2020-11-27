# ex2localejson.pyの使い方

## 前準備

### 下記をインストール
- python3

pythonについては、各環境に対して検索してインストールしてください。
(ubuntu環境でも動きます)
```
検索用語
windows python install 
または 
ubuntu python3 install
など
```

- openpyxl (python excel操作用)
pythonインストール後に下記を実行(ubuntuの場合)
```
sudo apt-get update
sudo apt install python3-pip
pip3 --version 
pip3 install openpyxl
```

### 実行

Excelファイルをpythonファイルと同じdirectoryに置いておく
ターミナルやコマンドプロンプトで下記を実行
```
python3 ex2localejson.py locale.xlsx
-> complete!
```

---

## ローカルにPythonを入れたくない場合

- docker環境があれば実行可能
- docker desktop for Windowsなどをインストール

### 下記順番で実行

```
docker-compose up -d # python実行用containerの起動
docker exec -it app /bin/sh #container内に入る
python ex2localejson.py locale.xlsx #python実行
-> complete!
exit
docker-compose down
```
これで、localesの中にlocale.jsonが2ファイルできるはず


