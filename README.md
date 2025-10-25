# Electronic Shop (FastAPI)

✨ Ключевые возможности
🛒 Управление корзиной - добавление, удаление, изменение количества товаров
📦 Каталог товаров - просмотр товаров с фильтрацией по категориям
🔍 Детальная информация - подробные страницы товаров
💾 Персистентность данных - сохранение корзины в localStorage
🎨 Современный UI - адаптивный дизайн на Tailwind CSS
🚀 Production-ready - автоматический деплой с SSL сертификатами

🔍 Назначение компонентов
Backend (FastAPI)

models/	SQLAlchemy модели для работы с БД (ORM)

schemas/	Pydantic схемы для валидации входящих/исходящих данных

repositories/	Инкапсуляция логики работы с БД (Repository Pattern)

services/	Бизнес-логика приложения (Service Layer)

routes/	HTTP endpoints и маршрутизация (Controllers)

config.py	Настройки приложения (CORS, DB, пути)

database.py	Конфигурация SQLAlchemy и управление сессиями

main.py	Инициализация FastAPI, подключение middleware и роутеров

