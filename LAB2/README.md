Работаем в интерактивном режиме докера. 

Для этого собираем:

```
docker build -t hse .
```

Затем запускаем в не-detached режиме:

```
docker run -i -t hse
```

И запускаем скрипт:

```
python3 result.py <URL>
```
