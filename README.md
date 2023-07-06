## Example Mediator Patter in Django

It's a simple example with Django Rest Framework to try to explain the 
mediator patter with DDD.


```
    |-- ddd
    |   |-- ddd (core Django App)
    |   |-- product (App Django)
    |   |-- |-- aplication
    |   |   |   |-- command
    |   |   |   |-- queries
    |   |   |   |-- services
    |   |   |   |   mediator.py
    |   |   |-- domain
    |   |   |   |-- model
    |   |   |   |-- repository
    |   |   |-- infrastructure
    |   |   |-- presentation
    |   |   manager.py
    |-- test
```

### Requirements
You will need:

```
Python ^3.10 
Poetry 1.4.1
Git
```

### Dependencies

Install all dependencies with the next poetry command and after that 
you will need setup the python interpreter and it have to with poetry.

```
poetry install
```

### Test
Ru the follow command in the main folder root.
```
 poetry run pytest
```

### Classes Repository

```
+---------------------+         +-----------------------+
| AbstractRepository  |<------  |AbstractRepositoryImpl |
+---------------------+         +-----------------------+
|                     |         | - _model_class        |
|                     |         |                       |
| +get_by_id()        |         | +get_by_id()          |
| +get_all()          |         | +get_all()            |
| +create()           |         | +create()             |
| +update()           |         | +update()             |
| +delete()           |         | +delete()             |
| +filter()           |         | +filter()             |
|                     |         | - _get_model()        |
+---------------------+         +-----------------------+
            ^
            |
            |       +-----------------+
            |       |ProductRepository|
            |<------|RepositoryImpl   |
                    +-----------------+
```

### Classes Mediator

In this case we have to build two classes the first one is an AddProductCommand dataclasses that it will receive 
properties the second class is AddProductCommandHandler that it has to implement a execute method who might have a 
responsibility to connect with the repository.

```
+------------------------+
|       Mediator         |
+------------------------+
| - handlers: Dict       |
+------------------------+
| + register()           |
| + execute()            |
+------------------------+
        ^
        |___________________________________________
                                                   | uses                  
+------------------------+                +-----------------------------+
|  AddProductCommand     |                |  AddProductCommandHandler   |
+------------------------+                +-----------------------------+
| - title: str           |                |                             |
| - description: str     |                |                             |
| - price: decimal       |                | + execute(AddProductCommand)|
+------------------------+                +-----------------------------+


+---------------------------------------+
|   ProductServices                     |
+---------------------------------------+
| + mediator.execute(AddProductCommand) |
+---------------------------------------+

```
