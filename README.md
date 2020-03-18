# Assembly 22

Приложение для записи на доступные мероприятия.

### Установка

Для работы приложения требуется **Docker** и **Docker Compose**.

Инициализация:
```
make init
```

### Запуск

Запуск:

```
make start
```

После запуска приложение доступно по адресу - [http://localhost:5000/api/v1](http://localhost:5000/api/v1)

Документация по API доступна по адресу - [http://localhost:5000](http://localhost:5000)

Панель администратора доступна по адресу - [http://localhost:5000/admin](http://localhost:5000/admin)

Остановка:
```
make stop
```
Просмотр логов приложения:
```
make logs
```

Удаление файлов приложения, которые создал Docker:
```
make flush
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе [Flask с нуля до 4 проектов в портфолио](https://academy.stepik.org/flask) в [Stepik Academy](https://academy.stepik.org/).
