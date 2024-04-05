echo "BUILD START"
/usr/bin/python3.9 -m ensurepip
/usr/bin/python3.9 --version
/usr/bin/python3.9 -m pip --version
echo python
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput

echo BASE_DIR
echo "Files in deployment directory:"
ls -R
echo "BUILD END"
