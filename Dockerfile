FROM ubuntu:20.04
RUN apt update
RUN apt install -y python3-pip git libexpat1
RUN DEBIAN_FRONTEND=noninteractive TZ=EST apt install -y tzdata
RUN apt install -y apache2 --no-install-recommends
RUN apt install -y libapache2-mod-wsgi-py3 --no-install-recommends
RUN apt install -y apache2-dev
RUN pip3 install mod_wsgi
RUN a2enmod proxy proxy_http proxy_balancer lbmethod_byrequests wsgi
#RUN echo "\nWSGIPythonHome /usr/lib/python3.8" >> /etc/apache2/httpd.conf
ADD . /work
WORKDIR /work
#RUN python3 setpath.py
RUN cp aop.wizdev.co.conf /etc/apache2/httpd.conf
#RUN a2ensite aop.wizdev.co.conf
RUN service apache2 restart
RUN pip3 install virtualenv
RUN virtualenv venv
RUN chmod -R 777 .
RUN venv/bin/activate
RUN pip3 install -r requirements.txt
RUN python3 manage.py collectstatic --noinput
#ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
#RUN chmod +x /wait
# Run migrations manually in docker
#RUN /wait && python3 manage.py makemigrations
#RUN python3 migrate
# Remember to create superurser as defined in onepassword after this
#CMD ["python3", "manage.py", "runserver"]
