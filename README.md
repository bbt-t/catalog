> Необходимо прописать переменные окружения

`SECRET_KEY='ЗДЕСЬ КЛЮЧ'`

    POSTGRES_DB
    POSTGRES_USER
    POSTGRES_PASSWORD
    POSTGRES_HOST
    POSTGRES_PORT

    EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD 

> Для работы без доступа к интернету необходимо:

- скачать -> [bootstrap](https://getbootstrap.com/docs/5.2/getting-started/download/)
- положить папки `css` и `js` в static
- заменить (закомментировать или удалить) в base.html `CDN` на закомментированный код (static link)
