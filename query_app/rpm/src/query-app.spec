Name:           query
Version:        1.0
Release:        0.1
Summary:        rpm pac for our project

Group:          query_app
BuildArch:      noarch
License:        GPL
URL:            https://github.com/c4n2012/python_hw/tree/flask_app/query_app
Source0:        query-1.0.tar.gz

%description
rpm package with 5 files

%prep

%setup -q -c

%build

%install

install -m 0755 -d %{buildroot}/opt/query-1.0
install -m 0755 queryapp.service  %{buildroot}/opt/query-1.0/queryapp.service
install -m 0775 query_class.py  %{buildroot}/opt/query-1.0/query_class.py
install -m 0775 flask_query_api.py %{buildroot}/opt/query-1.0/flask_query_api.py
install -m 0775 requirements.txt %{buildroot}/opt/query-1.0/requirements.txt

%files

/opt/query-1.0/*

%pre
getent group webapp >/dev/null || groupadd -r webapp
getent passwd webapp >/dev/null || \
useradd -r -g webapp -d /home/webapp -s /sbin/nologin \
    -c "This account was created to run query python service" webapp
exit 0
%post
/usr/local/bin/pip3 install -r /opt/query-1.0/requirements.txt
mv /opt/query-1.0/queryapp.service /etc/systemd/system
chmod 644 /etc/systemd/system/queryapp.service
systemctl enable queryapp
systemctl start queryapp
%preun
rm /opt/query-1.0/*
rmdir /opt/query-1.0
systemctl stop queryapp
systemctl enable queryapp
rm /etc/systemd/system/queryapp.service
userdel webapp --remove

%changelog
* Tue Jul 16 2019 Sergey Yanc  1.0.0.0
 - Initial rpm release

