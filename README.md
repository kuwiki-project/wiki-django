## 環境構築手順

###### wiki-django フォルダに移動

```
$cd wiki-django
```

###### pipenv を導入

```
$ pip install pipenv
```

pipenv とは，パッケージ管理ツール

###### パッケージを一括インストール

```
$ pipenv sync --dev
```

Pipfile にもとづき pipenv がパッケージをインストール

###### mysql 導入

```
$ brew install mysql
$ mysql --version
```

###### mysql サーバー起動

```
$ mysql.server start
```

###### mysql サーバー作成

```
$ mysql -u root
mysql> create database kuwiki;
mysql> show databases;
```

###### データベースのテーブルを作成

```
$ pipenv shell
(wiki-django)$ python manage.py migrate
(wiki-django)$ exit
```

###### 管理者作成

```
$ python manage.py createsuperuser
```

###### .env ファイル作成

```
$cd kuwiki
$cp .env.sample .env
```

###### .env ファイルの中身を記入

###### django サーバー起動

```
$ pipenv shell
(wiki-django)$ python manage.py runserver
```

pipenv のパッケージを利用しつつ django サーバーを起動
以下のコマンドに省略できる

```
$ pipenv run server
```
