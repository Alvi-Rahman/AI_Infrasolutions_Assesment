# AI-Infrasolutions (Django GeoJSON Feature API)

The Django GeoJSON Feature API is a small Django REST API that serves vector features in a GeoJSON compatible format. It provides CRUD (Create, Read, Update, Delete) operations for GeoJSON feature objects, allowing filtering by bounding box and paging of results. The API uses JSON Web Tokens (JWT) for authorization. Additionally, it includes a simple HTML frontend page to visualize the data using OpenLayers, as well as a second frontend page for editing feature properties.

## Requirements

- Python 3.x
- Django 3.x
- Django REST Framework 3.x
- Django Rest Framework GIS 1.x
- PostGIS database 13.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Alvi-Rahman/AI_Infrasolutions_Assesment.git
    ```
   
    Go to the folder

    ```bash
   cd AI_Infrasolutions_Assesment 
   ```
   
### **Make Sure you Have PostGIS Installed
   
## Installation
    
### Using Docker Container

```bash
   docker-compose up -- build
   ```

This Should make things up and running

### Running Locally

    
activate venv and run

```bash
pip install -r requirements.txt
```

then run

```python
python manage.py migrate
```

and then create a superuser/user

```bash
python manage.py createsuperuser
```

and provide necessary info

then run

```python
python manage.py runserver
```

## You should be up and running!

# Before you start.

run 3 apis so that the files are loaded

1. Go to `https://localhost:8000/apis/` to see the list of all apis 
2. `/geojson_files/upload_geo_json_files/` and upload a geojson file
3. `/geojson_files/list_geo_json_files/` to see the list of files you have uploaded
4. `/geojson_files/import_geo_json_file_to_features/<int:id>/` To load the data in the models


# Now LogIn and View Features



