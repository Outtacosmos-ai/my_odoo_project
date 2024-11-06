# Base image for Python 2.7 on Debian
FROM python:2.7-slim-buster

# Update system dependencies and install necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python-dev \
    libxml2-dev \
    libxslt1-dev \
    libldap2-dev \
    libsasl2-dev \
    libtiff5-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libxcb1-dev \
    node-less \
    npm \
    git \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip for compatibility with dependencies
RUN pip install --upgrade pip

# Install Odoo dependencies
RUN pip install --no-cache-dir \
    Babel==2.3.4 \
    decorator==4.0.10 \
    docutils==0.12 \
    feedparser==5.2.1 \
    gevent==1.1.2 \
    greenlet==0.4.10 \
    jcconv==0.2.3 \
    Jinja2==2.8 \
    lxml==3.5.0 \
    Mako==1.0.4 \
    MarkupSafe==0.23 \
    mock==2.0.0 \
    ofxparse==0.16 \
    passlib==1.6.5 \
    Pillow==4.0.0 \
    psutil==4.3.1 \
    psycopg2==2.7.3.1 \
    pydot==1.2.3 \
    pyldap==2.4.28 \
    pyparsing==2.1.10 \
    PyPDF2==1.26.0 \
    pyserial==3.1.1 \
    python-dateutil==2.5.3 \
    pytz==2016.7 \
    pyusb==1.0.0 \
    PyYAML==3.12 \
    qrcode==5.3 \
    reportlab==3.3.0 \
    requests==2.11.1 \
    suds-jurko==0.6 \
    vatnumber==1.2 \
    vobject==0.9.3 \
    Werkzeug==0.11.11 \
    XlsxWriter==0.9.3 \
    xlwt==1.3.* \
    xlrd==1.0.0

# Set Git buffer size
RUN git config --global http.postBuffer 524288000

# Clone Odoo repository
RUN git clone https://github.com/odoo/odoo --depth 1 --branch 11.0 /opt/odoo

# Set the working directory
WORKDIR /opt/odoo

# Copy configuration file and addons
RUN mkdir -p /etc/odoo /mnt/extra-addons
COPY ./config/odoo.conf /etc/odoo/odoo.conf
COPY ./addons /mnt/extra-addons

# Create odoo user and set permissions
RUN useradd -ms /bin/bash odoo
RUN chown -R odoo:odoo /etc/odoo /mnt/extra-addons /opt/odoo

# Expose Odoo default ports
EXPOSE 8069 8071

# Set the default user to 'odoo' and define the entrypoint
USER odoo
CMD ["/opt/odoo/odoo-bin", "-c", "/etc/odoo/odoo.conf"]
