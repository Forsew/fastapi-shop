# Electronic Shop (FastAPI)

✨ Ключевые возможности
🛒 Управление корзиной - добавление, удаление, изменение количества товаров
📦 Каталог товаров - просмотр товаров с фильтрацией по категориям
🔍 Детальная информация - подробные страницы товаров
💾 Персистентность данных - сохранение корзины в localStorage
🎨 Современный UI - адаптивный дизайн на Tailwind CSS
🚀 Production-ready - автоматический деплой с SSL сертификатами
📁 Структура проекта
fastapi-shop/
│
├── backend/                      # Backend часть (FastAPI)
│   ├── app/
│   │   ├── models/              # SQLAlchemy модели БД
│   │   │   ├── category.py     # Модель категорий
│   │   │   └── product.py      # Модель товаров
│   │   │
│   │   ├── schemas/             # Pydantic схемы для валидации
│   │   │   ├── cart.py         # Схемы корзины
│   │   │   ├── category.py     # Схемы категорий
│   │   │   └── product.py      # Схемы товаров
│   │   │
│   │   ├── repositories/        # Слой работы с БД (Repository Pattern)
│   │   │   ├── category_repository.py
│   │   │   └── product_repository.py
│   │   │
│   │   ├── services/            # Бизнес-логика приложения
│   │   │   ├── cart_service.py
│   │   │   ├── category_service.py
│   │   │   └── product_service.py
│   │   │
│   │   ├── routes/              # API endpoints (Controllers)
│   │   │   ├── cart.py         # Эндпоинты корзины
│   │   │   ├── categories.py   # Эндпоинты категорий
│   │   │   └── products.py     # Эндпоинты товаров
│   │   │
│   │   ├── config.py            # Конфигурация приложения
│   │   ├── database.py          # Настройка SQLAlchemy
│   │   └── main.py              # Точка входа FastAPI
│   │
│   ├── static/images/           # Статические файлы (изображения)
│   ├── Dockerfile               # Docker образ backend
│   ├── requirements.txt         # Python зависимости
│   ├── run.py                   # Скрипт запуска сервера
│   └── seed_data.py            # Заполнение БД тестовыми данными
│
├── frontend/                     # Frontend часть (Vue.js 3)
│   ├── src/
│   │   ├── components/          # Vue компоненты
│   │   │   ├── CartItem.vue    # Элемент корзины
│   │   │   ├── CategoryFilter.vue  # Фильтр категорий
│   │   │   ├── Header.vue      # Шапка сайта
│   │   │   └── ProductCard.vue # Карточка товара
│   │   │
│   │   ├── views/               # Страницы приложения
│   │   │   ├── HomePage.vue    # Главная (каталог)
│   │   │   ├── ProductDetailPage.vue  # Детали товара
│   │   │   └── CartPage.vue    # Страница корзины
│   │   │
│   │   ├── stores/              # Pinia stores (State Management)
│   │   │   ├── cart.js         # Store корзины
│   │   │   └── products.js     # Store товаров
│   │   │
│   │   ├── services/            # API клиенты
│   │   │   └── api.js          # Axios конфигурация и методы
│   │   │
│   │   ├── router/              # Vue Router конфигурация
│   │   │   └── index.js        # Определение маршрутов
│   │   │
│   │   ├── assets/              # Статические ресурсы
│   │   ├── App.vue              # Корневой компонент
│   │   └── main.js              # Точка входа приложения
│   │
│   ├── Dockerfile               # Docker образ frontend
│   ├── nginx.conf               # Конфигурация Nginx для SPA
│   ├── package.json             # NPM зависимости
│   └── vite.config.js          # Конфигурация Vite
│
├── nginx/                        # Reverse proxy конфигурация
│   └── nginx.conf               # Главная конфигурация Nginx
│
├── docker-compose.yml            # Оркестрация Docker контейнеров
├── deploy.sh                     # Скрипт автоматического деплоя
└── README.md                     # Документация проекта
🔍 Назначение компонентов
Backend (FastAPI)
Компонент	Назначение
models/	SQLAlchemy модели для работы с БД (ORM)
schemas/	Pydantic схемы для валидации входящих/исходящих данных
repositories/	Инкапсуляция логики работы с БД (Repository Pattern)
services/	Бизнес-логика приложения (Service Layer)
routes/	HTTP endpoints и маршрутизация (Controllers)
config.py	Настройки приложения (CORS, DB, пути)
database.py	Конфигурация SQLAlchemy и управление сессиями
main.py	Инициализация FastAPI, подключение middleware и роутеров
Frontend (Vue.js 3)
Компонент	Назначение
components/	Переиспользуемые UI компоненты
views/	Страницы приложения (роутинг)
stores/	Глобальное состояние приложения (Pinia)
services/	HTTP клиент для взаимодействия с API
router/	Конфигурация маршрутизации (Vue Router)
🛠 Технологический стек
Backend
FastAPI 0.119.0 - современный, быстрый web-framework
SQLAlchemy 2.0.44 - ORM для работы с базой данных
Pydantic 2.12.1 - валидация данных и настроек
SQLite - легковесная реляционная СУБД
Uvicorn - ASGI сервер для production
Frontend
Vue.js 3.5.22 - прогрессивный JavaScript фреймворк
Pinia 3.0.3 - официальный state management для Vue 3
Vue Router 4.5.1 - роутинг для SPA
Axios 1.12.2 - HTTP клиент
Tailwind CSS - utility-first CSS фреймворк
Vite 7.1.7 - быстрый build tool
DevOps
Docker - контейнеризация приложений
Docker Compose - оркестрация multi-container приложений
Nginx - reverse proxy и веб-сервер
Let's Encrypt - бесплатные SSL сертификаты
Certbot - автоматическое обновление сертификатов
🚀 Быстрый старт
Предварительные требования
Python 3.11+
Node.js 20+
npm/yarn
Git
Локальная разработка
1️⃣ Клонирование репозитория
git clone https://github.com/yourusername/fastapi-shop.git
cd fastapi-shop
2️⃣ Запуск Backend
# Переход в директорию backend
cd backend

# Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

# Установка зависимостей
pip install -r requirements.txt

# Заполнение базы данных тестовыми данными
python seed_data.py

# Запуск сервера разработки
python run.py
Backend будет доступен по адресу: http://localhost:8000 API документация (Swagger UI): http://localhost:8000/api/docs

3️⃣ Запуск Frontend
# Переход в директорию frontend (новый терминал)
cd frontend

# Установка зависимостей
npm install

# Запуск dev сервера
npm run dev
Frontend будет доступен по адресу: http://localhost:5173
