# Alpenists_project

### Запуск в среде разработки:
- Запуск mysql в контейнере:
> utils/ $ `docker-compose -f docker-compose.mysql.yml up` 
- Миграция БД (если БД не запускалась ранее):
> app/ $ `flask db upgrade`
- Запуск приложения:
> app/ $ `flask run`

