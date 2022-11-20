# Stripe_test

Тестовое задание по платёжной системе Stripe.

*Реализованы order, tax, discount и поддержка валют для одиночных товаров.  
Проект временно доступен по адресу:*  
http://abp-yc.mooo.com/



#

## Как запустить проект:

### Опция I (если установлен docker).
Запустить докер контейнер:
```
docker run -p 80:8000 abpdock/stripe-test
```
*Superuser - admin, password - admin.
В базе есть тестовые данные (для order.id = 1 и item.id = 1 или 2).

Протестировать ендпоинты:
- http://localhost/item/{id}/
- http://localhost/order/{id}/

### Опция II.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/abp-ce/rishat.git

cd rishat
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv

source venv/bin/activate
```

Обновить pip и установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

Создать базу, superuser и .env файл, переместившись в директорию проекта:

```
cd stripe_test

python manage.py migrate

python manage.py createsuperuser

nano .env
```
Содерживое .env:
```
STRIPE_API_KEY = sk_test_4eC39HqLyjWDarjtT1zdp7dc
DJANGO_SECRET_KEY = "секретный ключ джанги"
```
*Команда для генерации секретного ключа джанги*
```
python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
```


Запустить проект:

```
python manage.py runserver
```

Внести товары, валюты, скидки, налоги и создать заказ в admin панели.

Протестировать ендпоинты:
- http://localhost:8000/item/{id}/
- http://localhost:8000/order/{id}/

