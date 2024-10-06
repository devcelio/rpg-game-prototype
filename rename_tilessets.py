import os

path = 'assets/tilessets'
for filename in os.listdir(path):
    os.rename(
        os.path.join(path, filename), 
        filename.lower().replace('-', '_')
    )