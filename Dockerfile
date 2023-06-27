FROM jupyter/base-notebook:latest

RUN conda install --yes --no-pin \
  geopandas \
  rasterio \
  scikit-learn \
  statsmodels \
  seaborn \
  gdal

RUN mkdir satData
RUN mkdir results