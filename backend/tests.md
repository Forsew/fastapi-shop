# Руководство по настройке окружения и тестированию FastAPI Shop в Postman

## 📋 Содержание
1. [Настройка окружения](#настройка-окружения)
2. [Создание коллекции Postman](#создание-коллекции-postman)
3. [Базовые эндпоинты](#базовые-эндпоинты)
4. [Категории](#категории)
5. [Продукты](#продукты)
6. [Корзина](#корзина)
7. [Автоматические тесты](#автоматические-тесты)
8. [Сценарии тестирования](#сценарии-тестирования)

---

## Настройка окружения

### Шаг 1: Установка Python и зависимостей

#### 1.1 Проверка Python
```bash
python --version
# или
python3 --version
```
Требуется Python 3.8 или выше.

#### 1.2 Создание виртуального окружения
```bash
cd backend
python -m venv .venv
```

#### 1.3 Активация виртуального окружения

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

После активации в командной строке должно появиться `(.venv)`.

#### 1.4 Установка зависимостей
Создайте файл `backend/requirements.txt`:
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.0
pydantic-settings==2.1.0
```

Установите зависимости:
```bash
pip install -r requirements.txt
```

### Шаг 2: Исправление ошибок в коде

Перед запуском нужно исправить найденные ошибки:

#### 2.1 Файл `backend/seed_data.py` (строка 1)
**Было:**
```python
from app.database import Sessionlocal, init_db
```

**Должно быть:**
```python
from app.database import SessionLocal, init_db
```

#### 2.2 Файл `backend/seed_data.py` (строка 65)
**Было:**
```python
db = Sessionlocal()
```

**Должно быть:**
```python
db = SessionLocal()
```

#### 2.3 Файл `backend/app/repositories/category_repository.py` (строка 23)
**Было:**
```python
self.db.refresh()
```

**Должно быть:**
```python
self.db.refresh(db_category)
```

#### 2.4 Файл `backend/app/services/cart_service.py` (строка 47)
**Было:**
```python
product_ids = list(cart_data.keys)
```

**Должно быть:**
```python
product_ids = list(cart_data.keys())
```

#### 2.5 Файл `backend/app/services/cart_service.py` (строка 59)
**Было:**
```python
image_url=product.image)
```

**Должно быть:**
```python
image_url=product.image_url)
```

### Шаг 3: Заполнение базы данных

```bash
cd backend
python seed_data.py
```

**Ожидаемый вывод:**
```
🚀 Starting database seeding...
✅ Database tables created
📁 Creating categories...
✅ Created 4 categories
📦 Creating products...
✅ Created 13 products
🎉 Database seeding completed successfully!
```

### Шаг 4: Запуск API сервера

```bash
cd backend
python run.py
```

**Ожидаемый вывод:**
```
INFO:     Will watch for changes in these directories: ['/path/to/backend']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using StatReload
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Шаг 5: Проверка работы API

Откройте браузер и перейдите по адресу:
```
http://127.0.0.1:8000/api/docs
```

Вы должны увидеть автоматическую документацию Swagger UI.

---

## Создание коллекции Postman

### Шаг 1: Создание окружения (Environment)

1. Откройте Postman
2. Нажмите на **Environments** в левой панели
3. Нажмите кнопку **+** или **Create Environment**
4. Назовите окружение: `FastAPI Shop Local`
5. Добавьте следующие переменные:

| Variable | Type | Initial Value | Current Value |
|----------|------|---------------|---------------|
| `base_url` | default | `http://127.0.0.1:8000` | `http://127.0.0.1:8000` |
| `product_id` | default | `1` | `1` |
| `category_id` | default | `1` | `1` |
| `cart` | default | `{}` | `{}` |

6. Нажмите **Save**
7. Выберите это окружение в выпадающем списке в правом верхнем углу

### Шаг 2: Создание коллекции

1. Нажмите **Collections** в левой панели
2. Нажмите кнопку **+** или **Create Collection**
3. Назовите коллекцию: `FastAPI Shop API`
4. Добавьте описание: `E-commerce API для тестирования`

### Шаг 3: Настройка коллекции

1. Выберите созданную коллекцию
2. Перейдите во вкладку **Variables**
3. Можно добавить переменные уровня коллекции (опционально)

---

## Базовые эндпоинты

### Папка: Health & Root

Создайте папку (folder) в коллекции с названием **Health & Root**.

#### 1. Health Check

**Создание запроса:**
1. Нажмите **Add request** в папке
2. Название: `Health Check`
3. Метод: `GET`
4. URL: `{{base_url}}/health`
5. **Save**

**Ожидаемый ответ (200 OK):**
```json
{
  "sattus": "healthy"
}
```

#### 2. Root

**Создание запроса:**
1. Нажмите **Add request**
2. Название: `Root`
3. Метод: `GET`
4. URL: `{{base_url}}/`
5. **Save**

**Ожидаемый ответ (200 OK):**
```json
{
  "message": "welcome to fastApi shop API",
  "docs": "api/docs"
}
```

---

## Категории

### Папка: Categories

Создайте папку **Categories** в коллекции.

#### 1. Get All Categories

**Создание запроса:**
1. Название: `Get All Categories`
2. Метод: `GET`
3. URL: `{{base_url}}/api/categories/`
4. **Save**

**Ожидаемый ответ (200 OK):**
```json
[
  {
    "name": "Electronics",
    "slug": "electronics",
    "id": 1
  },
  {
    "name": "Clothing",
    "slug": "clothing",
    "id": 2
  },
  {
    "name": "Books",
    "slug": "books",
    "id": 3
  },
  {
    "name": "Home & Garden",
    "slug": "home-garden",
    "id": 4
  }
]
```

#### 2. Get Category by ID

**Создание запроса:**
1. Название: `Get Category by ID`
2. Метод: `GET`
3. URL: `{{base_url}}/api/categories/{{category_id}}`
4. **Save**

**Ожидаемый ответ (200 OK):**
```json
{
  "name": "Electronics",
  "slug": "electronics",
  "id": 1
}
```

#### 3. Get Category by ID (Not Found)

**Создание запроса:**
1. Название: `Get Category by ID (404)`
2. Метод: `GET`
3. URL: `{{base_url}}/api/categories/999`
4. **Save**

**Ожидаемый ответ (404 Not Found):**
```json
{
  "detail": "Category with 999 not found"
}
```

---

## Продукты

### Папка: Products

Создайте папку **Products** в коллекции.

#### 1. Get All Products

**Создание запроса:**
1. Название: `Get All Products`
2. Метод: `GET`
3. URL: `{{base_url}}/api/products`
4. **Save**

**Ожидаемый ответ (200 OK):**
```json
{
  "products": [
    {
      "name": "Wireless Headphones",
      "description": "High-quality wireless headphones...",
      "price": 299.99,
      "category_id": 1,
      "image_url": "https://images.unsplash.com/...",
      "id": 1,
      "created_at": "2025-10-26T10:30:00",
      "category": {
        "name": "Electronics",
        "slug": "electronics",
        "id": 1
      }
    }
  ],
  "total": 13
}
```

#### 2. Get Product by ID

**Создание запроса:**
1. Название: `Get Product by ID`
2. Метод: `GET`
3. URL: `{{base_url}}/api/products/{{product_id}}`
4. **Save**

#### 3. Get Product by ID (Not Found)

**Создание запроса:**
1. Название: `Get Product by ID (404)`
2. Метод: `GET`
3. URL: `{{base_url}}/api/products/999`
4. **Save**

**Ожидаемый ответ (404 Not Found):**
```json
{
  "detail": "Product with id 999 not found"
}
```

#### 4. Get Products by Category

**Создание запроса:**
1. Название: `Get Products by Category`
2. Метод: `GET`
3. URL: `{{base_url}}/api/products/category/{{category_id}}`
4. **Save**

**Ожидаемый ответ (200 OK):**
```json
{
  "products": [
    {
      "name": "Wireless Headphones",
      "description": "High-quality wireless headphones...",
      "price": 299.99,
      "category_id": 1,
      "image_url": "https://images.unsplash.com/...",
      "id": 1,
      "created_at": "2025-10-26T10:30:00",
      "category": {
        "name": "Electronics",
        "slug": "electronics",
        "id": 1
      }
    }
  ],
  "total": 5
}
```

#### 5. Get Products by Category (Not Found)

**Создание запроса:**
1. Название: `Get Products by Category (404)`
2. Метод: `GET`
3. URL: `{{base_url}}/api/products/category/999`
4. **Save**

---

## Корзина

### Папка: Cart

Создайте папку **Cart** в коллекции.

#### 1. Add to Cart

**Создание запроса:**
1. Название: `Add to Cart`
2. Метод: `POST`
3. URL: `{{base_url}}/api/cart/add`
4. Перейдите во вкладку **Body**
5. Выберите **raw** и **JSON**
6. Введите:
```json
{
  "product_id": 1,
  "quantity": 2,
  "cart": {}
}
```
7. **Save**

**Ожидаемый ответ (200 OK):**
```json
{
  "cart": {
    "1": 2
  }
}
```

**Для сохранения корзины в переменную окружения:**
1. Перейдите во вкладку **Tests**
2. Добавьте:
```javascript
pm.test("Save cart to environment", function () {
    var jsonData = pm.response.json();
    pm.environment.set("cart", JSON.stringify(jsonData.cart));
});
```

#### 2. Add Another Product to Cart

**Создание запроса:**
1. Название: `Add Another Product to Cart`
2. Метод: `POST`
3. URL: `{{base_url}}/api/cart/add`
4. Body:
```json
{
  "product_id": 2,
  "quantity": 1,
  "cart": {{cart}}
}
```
5. **Save**

#### 3. Add to Cart (Product Not Found)

**Создание запроса:**
1. Название: `Add to Cart (404)`
2. Метод: `POST`
3. URL: `{{base_url}}/api/cart/add`
4. Body:
```json
{
  "product_id": 999,
  "quantity": 1,
  "cart": {}
}
```
5. **Save**

**Ожидаемый ответ (404 Not Found):**
```json
{
  "detail": "Product with id 999 not found"
}
```

#### 4. Get Cart Details

**Создание запроса:**
1. Название: `Get Cart Details`
2. Метод: `POST`
3. URL: `{{base_url}}/api/cart`
4. Body:
```json
{
  "1": 2,
  "2": 1
}
```
5. **Save**

**Ожидаемый ответ (200 OK):**
```json
{
  "items": [
    {
      "product_id": 1,
      "name": "Wireless Headphones",
      "price": 299.99,
      "quantity": 2,
      "subtotal": 599.98,
      "image_url": "https://images.unsplash.com/..."
    },
    {
      "product_id": 2,
      "name": "Smart Watch Pro",
      "price": 399.99,
      "quantity": 1,
      "subtotal": 399.99,
      "image_url": "https://images.unsplash.com/..."
    }
  ],
  "total": 1000.0,
  "items_count": 3
}
```

#### 5. Get Empty Cart

**Создание запроса:**
1. Название: `Get Empty Cart`
2. Метод: `POST`
3. URL: `{{base_url}}/api/cart`
4. Body:
```json
{}
```
5. **Save**

**Ожидаемый ответ (200 OK):**
```json
{
  "items": [],
  "total": 0.0,
  "items_count": 0
}
```

#### 6. Update Cart Item

**Создание запроса:**
1. Название: `Update Cart Item`
2. Метод: `PUT`
3. URL: `{{base_url}}/api/cart/update`
4. Body:
```json
{
  "product_id": 1,
  "quantity": 5,
  "cart": {
    "1": 2,
    "2": 1
  }
}
```
5. **Save**

**Ожидаемый ответ (200 OK):**
```json
{
  "cart": {
    "1": 5,
    "2": 1
  }
}
```

#### 7. Update Cart Item (Not Found)

**Создание запроса:**
1. Название: `Update Cart Item (404)`
2. Метод: `PUT`
3. URL: `{{base_url}}/api/cart/update`
4. Body:
```json
{
  "product_id": 999,
  "quantity": 1,
  "cart": {
    "1": 2
  }
}
```
5. **Save**

**Ожидаемый ответ (404 Not Found):**
```json
{
  "detail": "Product with id 999 not found in cart"
}
```

#### 8. Remove from Cart

**Создание запроса:**
1. Название: `Remove from Cart`
2. Метод: `DELETE`
3. URL: `{{base_url}}/api/cart/remove/1`
4. Body:
```json
{
  "cart": {
    "1": 2,
    "2": 1
  }
}
```
5. **Save**

**Ожидаемый ответ (200 OK):**
```json
{
  "cart": {
    "2": 1
  }
}
```

#### 9. Remove from Cart (Not Found)

**Создание запроса:**
1. Название: `Remove from Cart (404)`
2. Метод: `DELETE`
3. URL: `{{base_url}}/api/cart/remove/999`
4. Body:
```json
{
  "cart": {
    "1": 2
  }
}
```
5. **Save**

---

## Автоматические тесты

### Общие тесты для всех запросов

Добавьте во вкладку **Tests** на уровне коллекции:

```javascript
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

pm.test("Content-Type is application/json", function () {
    pm.expect(pm.response.headers.get("Content-Type")).to.include("application/json");
});
```

### Специфичные тесты

#### Для GET /api/products

```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response has products array", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('products');
    pm.expect(jsonData.products).to.be.an('array');
});

pm.test("Response has total", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('total');
    pm.expect(jsonData.total).to.be.a('number');
});

pm.test("Products count matches total", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.products.length).to.equal(jsonData.total);
});

pm.test("Each product has required fields", function () {
    var jsonData = pm.response.json();
    jsonData.products.forEach(function(product) {
        pm.expect(product).to.have.property('id');
        pm.expect(product).to.have.property('name');
        pm.expect(product).to.have.property('price');
        pm.expect(product).to.have.property('category');
        pm.expect(product.category).to.have.property('id');
        pm.expect(product.category).to.have.property('name');
    });
});
```

#### Для POST /api/cart/add

```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response has cart", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('cart');
    pm.expect(jsonData.cart).to.be.an('object');
});

pm.test("Product added to cart", function () {
    var jsonData = pm.response.json();
    var requestBody = JSON.parse(pm.request.body.raw);
    var productId = requestBody.product_id.toString();
    pm.expect(jsonData.cart).to.have.property(productId);
});

pm.test("Quantity is correct", function () {
    var jsonData = pm.response.json();
    var requestBody = JSON.parse(pm.request.body.raw);
    var productId = requestBody.product_id.toString();
    pm.expect(jsonData.cart[productId]).to.be.a('number');
});

// Сохраняем корзину в переменную окружения
pm.environment.set("cart", JSON.stringify(pm.response.json().cart));
```

#### Для GET /api/categories

```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response is array", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array');
});

pm.test("Array is not empty", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.length).to.be.above(0);
});

pm.test("Each category has required fields", function () {
    var jsonData = pm.response.json();
    jsonData.forEach(function(category) {
        pm.expect(category).to.have.property('id');
        pm.expect(category).to.have.property('name');
        pm.expect(category).to.have.property('slug');
        pm.expect(category.id).to.be.a('number');
        pm.expect(category.name).to.be.a('string');
        pm.expect(category.slug).to.be.a('string');
    });
});
```

#### Для POST /api/cart (Get Cart Details)

```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response has required fields", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('items');
    pm.expect(jsonData).to.have.property('total');
    pm.expect(jsonData).to.have.property('items_count');
});

pm.test("Items is an array", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.items).to.be.an('array');
});

pm.test("Total is a number", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.total).to.be.a('number');
    pm.expect(jsonData.total).to.be.at.least(0);
});

pm.test("Items count matches sum of quantities", function () {
    var jsonData = pm.response.json();
    var sum = jsonData.items.reduce((acc, item) => acc + item.quantity, 0);
    pm.expect(jsonData.items_count).to.equal(sum);
});

pm.test("Each item has correct structure", function () {
    var jsonData = pm.response.json();
    jsonData.items.forEach(function(item) {
        pm.expect(item).to.have.property('product_id');
        pm.expect(item).to.have.property('name');
        pm.expect(item).to.have.property('price');
        pm.expect(item).to.have.property('quantity');
        pm.expect(item).to.have.property('subtotal');
        pm.expect(item.subtotal).to.equal(item.price * item.quantity);
    });
});
```

#### Для ошибок 404

```javascript
pm.test("Status code is 404", function () {
    pm.response.to.have.status(404);
});

pm.test("Response has error detail", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('detail');
    pm.expect(jsonData.detail).to.be.a('string');
});
```

---

## Сценарии тестирования

### Использование Collection Runner

1. Выберите коллекцию `FastAPI Shop API`
2. Нажмите **Run** (или три точки → **Run collection**)
3. Откроется **Collection Runner**

### Сценарий 1: Полный цикл работы с магазином

**Порядок запросов:**
1. Health Check
2. Get All Categories
3. Get Products by Category
4. Add to Cart
5. Add Another Product to Cart
6. Get Cart Details
7. Update Cart Item
8. Get Cart Details (проверка обновления)
9. Remove from Cart
10. Get Cart Details (проверка удаления)

**Настройка Runner:**
1. Отметьте нужные запросы в правильном порядке
2. Установите **Iterations**: `1`
3. Установите **Delay**: `100ms` (задержка между запросами)
4. Нажмите **Run FastAPI Shop API**

### Сценарий 2: Тестирование ошибок

**Порядок запросов:**
1. Get Product by ID (404)
2. Get Category by ID (404)
3. Get Products by Category (404)
4. Add to Cart (404)
5. Update Cart Item (404)
6. Remove from Cart (404)

### Сценарий 3: Нагрузочное тестирование

**Настройка Runner:**
1. Выберите все GET запросы
2. Установите **Iterations**: `10`
3. Установите **Delay**: `50ms`
4. Нажмите **Run**

Проверьте, что все запросы выполняются за разумное время (< 500ms).

---

## 🎯 Чек-лист перед тестированием

- [ ] Python установлен (версия ≥ 3.8)
- [ ] Виртуальное окружение создано и активировано
- [ ] Все зависимости установлены
- [ ] Ошибки в коде исправлены
- [ ] База данных заполнена (seed_data.py выполнен успешно)
- [ ] API сервер запущен и доступен на http://127.0.0.1:8000
- [ ] Postman установлен
- [ ] Окружение создано и активировано
- [ ] Коллекция создана
- [ ] Все запросы добавлены и сохранены

---

## 🚀 Быстрый старт

```bash
# 1. Создать и активировать виртуальное окружение
cd backend
python -m venv .venv
source .venv/bin/activate  # или .venv\Scripts\activate на Windows

# 2. Установить зависимости
pip install -r requirements.txt

# 3. Заполнить базу данных
python seed_data.py

# 4. Запустить сервер
python run.py

# 5. Открыть Postman и начать тестирование!
```

---

## 📊 Экспорт результатов

После выполнения Collection Runner:

1. Нажмите **Export Results**
2. Выберите формат: JSON
3. Сохраните файл с результатами тестов

Результаты можно использовать для отчетности или CI/CD интеграции.