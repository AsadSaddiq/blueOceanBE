 echo "BUILD START"
 /usr/bin/python3.9 -m ensurepip
 /usr/bin/python3.9 --version
 /usr/bin/python3.9 -m pip --version
 source /path/to/your/venv/bin/activate
 echo python
 python3.9 -m pip install -r requirements.txt
 python3.9 manage.py collectstatic --noinput --clear
 echo "BUILD END"