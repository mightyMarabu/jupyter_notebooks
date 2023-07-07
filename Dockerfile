FROM jupyter/base-notebook:latest

USER root

#SHELL ["/bin/sh", "-c"]

# install base utilities
RUN apt update && apt upgrade -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y gcc

# install gdal
RUN apt-get install -y gdal-bin
RUN apt-get install -y libgdal-dev libgl1-mesa-glx
RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal
RUN apt-get install -y build-essential
RUN apt-get install -y wget


#COPY requirements.txt /tmp/

# upgrade pip and install python libraries
RUN pip3 install --upgrade pip
RUN pip3 install tensorflow keras segmentation-models
#RUN pip3 install tensorflow_hub tensorflow_datasets
RUN pip3 install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"
RUN pip3 install numpy matplotlib boto3 rasterio shapely scikit-learn scikit-image opencv-python patchify geopandas
#RUN pip3 install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

#RUN pip install --requirement /tmp/requirements.txt

RUN mkdir notebooks
RUN chmod a+rwx /home/jovyan/notebooks
RUN mkdir satData
RUN chmod a+rwx /home/jovyan/satData
RUN mkdir results
RUN chmod a+rwx /home/jovyan/results