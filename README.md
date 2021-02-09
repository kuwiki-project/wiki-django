## 環境構築手順


1. pipenv を導入
```
$ pip install pipenv
```
pipenvとは，パッケージ管理ツール

1. パッケージをインストール
```
$ pipenv sync --dev
```
Pipfile にもとづき pipenv がパッケージをインストール

1. mysql 導入
```
$ brew install mysql
$ mysql --version
```

1. mysql サーバー起動
```
$ mysql.server start
```

1. mysql サーバー作成
```
$ mysql -u root
mysql> create database kuwiki;
mysql> show databases;
```

1. データベースのテーブルを作成
```
$ pipenv shell
(wiki-django)$ python manage.py migrate
(wiki-django)$ exit
```

1. django サーバー起動
```
$ pipenv shell
(wiki-django)$ python manage.py runserver
```
pipenv のパッケージを利用しつつdjangoサーバーを起動
以下のコマンドに省略できる
```
$ pipenv run server
```

1. 管理者作成
```
$ python manage.py createsuperuser
```

1. .envファイル作成
`.env.sample`ファイルと同階層に`.env`ファイルを作成する
