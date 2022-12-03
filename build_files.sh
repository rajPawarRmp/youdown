echo "BUILD START"
python3.6 -m pip install -r requirements.txt
python3.6 manage.py collectstatic --noinput --clear
echo "BUILD END"