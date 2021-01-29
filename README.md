# django-crud-api

# Backend Python

## Requirements
- Python 3.8
- Django (3.1.5)
- Django REST Framework
- Django Rest Auth
- Django Restql (GraphQL)

to clone the repository
```
$ git clone https://github.com/uandisson/django-crud-api.git
```
create virtualenv named env and activate it
```
$ cd django-crud-api/
```
```
$ python3 -m venv env
```
```
$ source env/bin/activate 
```
- for deactivate env 
```
$ deactivate
```
install requirements packages
```
$ pip install -r requirements.txt
```
if you want to check if everything is OK so far. First migratation:
```
$ cd ecom_backend/
```
```
$ python3 manage.py makemigrations
```
```
$ python3 manage.py migrate 
```
```
then start the development server.
```
```
$ python3 manage.py runserver
```
if all is well, in the terminal: http://127.0.0.1:8000/

![](imgs/readme_assets/00.png)


in the browser


![](imgs/readme_assets/01.png)


## Structure

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`products` | GET | READ | Get all products
`products/:id` | GET | READ | Get a single product
`products`| POST | CREATE | Create a new product
`products/:id` | PUT | UPDATE | Update a product
`products/:id` | DELETE | DELETE | Delete a product
`categories` | GET | READ | Get all categories
`categories/:id` | GET | READ | Get a single category
`categories`| POST | CREATE | Create a new category
`categories/:id` | PUT | UPDATE | Update a category
`categories/:id` | DELETE | DELETE | Delete a category

## Use

Only authenticated:
```
	http  http://127.0.0.1:8000/api/v1/products/2
```
get:
```
 {  "detail":  "You must be authenticated"  }
```
Instead, if we try to access with credentials:
```
	http http://127.0.0.1:8000/api/v1/products/2 "Authorization: Token 7530ec9186a31a5b3dd8d03d84e34f80941391e3"
```
Get the product with id = 2
```
{"id":2,"name":"product B","description":"","price":0.0,"created_at":"2021-01-26T21:34:38.080139-03:00","updated_at":"2021-01-26T21:34:38.080203-03:00","category":null}

```
Category
```
curl -H "Authorization: Token 43541284e7c7a592d5ca00d25dd2906f8d8b87e1" -X GET http://127.0.0.1:8000/api/v1/categories/1
```

Get the category with id = 1
```
{"name":"Category 01"}

```



## Login and Tokens

To get a token first we have to login
```
	curl -X POST -d  "username=superuser&password=superuser"   http://127.0.0.1:8000/api/v1/rest-auth/login/ 
```
after that, we get the token
```
{
    "key": "43541284e7c7a592d5ca00d25dd2906f8d8b87e1"
}
```


### Pagination

```

curl -H "Authorization: Token 43541284e7c7a592d5ca00d25dd2906f8d8b87e1" -X GET http://127.0.0.1:8000/api/v1/products/?page=1

curl -H "Authorization: Token 43541284e7c7a592d5ca00d25dd2906f8d8b87e1" -X GET http://127.0.0.1:8000/api/v1/products/?page=1&page_size=1

curl -H "Authorization: Token 43541284e7c7a592d5ca00d25dd2906f8d8b87e1" -X GET http://127.0.0.1:8000/api/v1/categories/?page=1

curl -H "Authorization: Token 43541284e7c7a592d5ca00d25dd2906f8d8b87e1" -X GET http://127.0.0.1:8000/api/v1/categories/?page=1&page_size=1


```

### Swagger
```
http://127.0.0.1:8000/api/v1/swagger.json (or .yaml)

http://127.0.0.1:8000/api/v1/swagger/

http://127.0.0.1:8000/api/v1/redoc 

```

Swagger in the browser


![](imgs/readme_assets/02.png)
