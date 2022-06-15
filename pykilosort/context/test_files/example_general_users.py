from pathlib import Path
from pykilosort import run, add_default_handler, np1_probe, np2_probe

# Run standard ks2.5 algorithm for a np1 probe
data_path = Path('path/to/data/data.bin')
dir_path = Path('path/to/output/folder') # by default uses the same folder as the dataset
add_default_handler(level='INFO') # print output as the algorithm runs
run(data_path, dir_path=dir_path, probe=np1_probe())

# Run chronic recordings for a np2 probe
# For now this still uses ks2.5 clustering, chronic clustering algorithm coming soon!
data_paths = [
    Path('path/to/first/dataset/dataset.bin'),
    Path('path/to/second/dataset/dataset.bin'),
    Path('path/to/third/dataset/dataset.bin'),
]
dir_path = Path('path/to/output/folder') # by default uses the same folder as the first dataset
add_default_handler(level='INFO')
run(data_paths, dir_path=dir_path, probe=np2_probe(), low_memory=True)
