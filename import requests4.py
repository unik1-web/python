import requests
req = requests.post('<a href="https://en.wikipedia.org/w/index.php">https://en.wikipedia.org/w/index.php</a>', data = {'search':'Nanotechnology'})
req.raise_for_status()
with open('Nanotechnology.html', 'wb') as fd:
    for chunk in req.iter_content(chunk_size=50000):
        fd.write(chunk)