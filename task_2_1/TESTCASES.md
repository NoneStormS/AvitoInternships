# Создание объявления

## Предусловие
SellerID — использовать уникальный id (в диапазоне 111111-999999)

## Запрос
**Метод:** `POST`  
**URL:** `https://qa-internship.avito.com/api/1/item`  

### Хедеры:
```json
{
  "Accept": "application/json",
  "Content-Type": "application/json"
}
```
### Боди:
```json
{
  "sellerID": "int",
  "name": "str",
  "price": "int",
  "statistics": {
    "contacts": "int",
    "likes": "int",
    "viewCount": "int"
  }
}
```
### Ожидаемый результат:
200 OK
{
    "status": "Сохранили объявление - <id>"
}

# Получить объявления по его идентификатору 

## Запрос
**Метод:** `GET`  
**URL:** `https://qa-internship.avito.com/api/1/item/<id>`  

### Хедеры:
```json
{
  "Accept": "application/json"
}
```
### Ожидаемый результат:
200 OK
[
    {
        "createdAt": "2025-02-12 17:04:37.443654 +0300 +0300",
        "id": "str",
        "name": "str",
        "price": "int",
        "sellerId": "int",
        "statistics": {
            "contacts": "int",
            "likes": "int",
            "viewCount": "int"
        }
    }
]

# Получить объявление по несуществующему идентификатору

## Запрос
**Метод:** `GET`  
**URL:** `https://qa-internship.avito.com/api/1/<id>`  

### Хедеры:
```json
{
  "Accept": "application/json"
}
```
### Ожидаемый результат:
400 Bad Request
{
    "result": {
        "message": "передан некорректный идентификатор объявления",
        "messages": {}
    },
    "status": "400"
}

# Получить статистику по айтем id

## Запрос
**Метод:** `GET`  
**URL:** `https://qa-internship.avito.com/api/1/statistic/<id>`  

### Хедеры:
```json
{
  "Accept": "application/json"
}
```
### Ожидаемый результат:
[
    {
        "contacts": "int",
        "likes": "int",
        "viewCount": "int"
    }
]

# Получить все объявления по идентификатору продавца
    
## Запрос
**Метод:** `GET`  
**URL:** `https://qa-internship.avito.com/api/1/<sellerID>/item`  

### Хедеры:
```json
{
  "Accept": "application/json"
}
```
### Ожидаемый результат:
200 OK
[
    {
        "createdAt": "2025-02-12 17:04:37.443654 +0300 +0300",
        "id": "str",
        "name": "str",
        "price": "int",
        "sellerId": "int",
        "statistics": {
            "contacts": "int",
            "likes": "int",
            "viewCount": "int"
        }
    }
]

# Отправить запрос на получение объявлений несуществующего продавца
## Запрос
**Метод:** `GET`  
**URL:** `https://qa-internship.avito.com/api/1/<sellerID>/item`  

### Хедеры:
```json
{
  "Accept": "application/json"
}
```
### Ожидаемый результат:
200 OK
[]

# Валидация поля sellerID в запросе создания объявления

## Запрос
**Метод:** `POST`  
**URL:** `https://qa-internship.avito.com/api/1/item`  

### Хедеры:
```json
{
  "Accept": "application/json",
  "Content-Type": "application/json"
}
```
### Боди:
```json
{
  "name": "str",
  "price": "int",
  "statistics": {
    "contacts": "int",
    "likes": "int",
    "viewCount": "int"
  }
}
```
### Примеры значений sellerID и ожидаемые результаты:
- **sellerID:** "srt"  
  **Ожидаемый результат:** 400 Bad Request {
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявлени"
}
  
- **sellerID:** ""  
  **Ожидаемый результат:** 400 Bad Request {
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявлени"
}

- **sellerID:** отсутствует  
  **Ожидаемый результат:** 400 Bad Request {
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявлени"
}

# Валидация поля name в запросе создания объявления

## Запрос
**Метод:** `POST`  
**URL:** `https://qa-internship.avito.com/api/1/item`  

### Хедеры:
```json
{
  "Accept": "application/json",
  "Content-Type": "application/json"
}
```
### Боди:
```json
{
  "sellerID": "int",
  "price": "int",
  "statistics": {
    "contacts": "int",
    "likes": "int",
    "viewCount": "int"
  }
}
```
### Примеры значений name и ожидаемые результаты:
- **name:** "int"  
  **Ожидаемый результат:** 400 Bad Request {
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявлени"
}
  
- **name:** ""  
  **Ожидаемый результат:** 400 Bad Request {
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявлени"
}

- **name:** отсутствует  
  **Ожидаемый результат:** 400 Bad Request {
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявлени"
}

# Валидация поля price в запросе создания объявления

## Запрос
**Метод:** `POST`  
**URL:** `https://qa-internship.avito.com/api/1/item`  

### Хедеры:
```json
{
  "Accept": "application/json",
  "Content-Type": "application/json"
}
```
### Боди:
```json
{
  "sellerID": "int",
  "name": "str"
}
```
### Примеры значений price и ожидаемые результаты:
- **price:** "srt"  
  **Ожидаемый результат:** 400 Bad Request {
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявлени"
}
  
- **price:** ""  
  **Ожидаемый результат:** 400 Bad Request {
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявлени"
}

- **price:** отсутствует  
  **Ожидаемый результат:** 400 Bad Request {
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявлени"
}

# Создание объявления без необязательного параметра statistics

## Запрос
**Метод:** `POST`  
**URL:** `https://qa-internship.avito.com/api/1/item`  

### Хедеры:
```json
{
  "Accept": "application/json",
  "Content-Type": "application/json"
}
```
### Боди:
```json
{
  "sellerID": "int",
  "name": "str",
  "price": "int"
}
```
### Ожидаемый результат:
200 OK
{
    "status": "Сохранили объявление - <id>"
}



