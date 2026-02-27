


##### without threading ######
import time
import requests

def download(url):
    start = time.time()
    try:
        r = requests.get(url, timeout=10)
        status = r.status_code
        msg = "OK"
    except Exception as e:
        status = ""
        msg = f"ERROR: {e}"
    seconds = round(time.time() - start, 3)
    print(url, "->", status, "|", seconds, "sec |", msg)

# read urls
with open("urls.txt", "r") as f:
    urls = [line.strip() for line in f if line.strip()]

total_start = time.time()

for url in urls:
    download(url)

total_seconds = round(time.time() - total_start, 3)
print("TOTAL TIME:", total_seconds, "sec")