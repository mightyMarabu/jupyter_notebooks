# jupyter_notebooks
``` 
podman run -d -p 8889:8888 -v .:/home/jovyan/notebooks --name sat_book sat_book

```

```
podman cp sat_books:cropData.ipynb jupyter_notebooks/
```