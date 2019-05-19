echo "[+] Starting Setup"
python manage.py migrate
npm install -g algopack
echo "[+] Installed Algopack api builder"
echo "[+] Building Fresh API"
algopack build
echo "[+] Builded Fresh Algopack API"]
python create_db_from_repo.py
echo "[+] Created Database "