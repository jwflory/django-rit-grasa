# Local development container. Includes development dependencies.

FROM python:3.6                                                                                                                                                                                         
                                                                                 
RUN apt-get update \                                                             
    && apt-get install -y --no-install-recommends \                              
        postgresql-client \                                                      
    && rm -rf /var/lib/apt/lists/*
                                                          
WORKDIR /usr/src/app                                                             

COPY . /usr/src/app

RUN pip3 install pipenv \
    && pipenv install --system --deploy --dev
                                                                                 
EXPOSE 8000                                                                        
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
