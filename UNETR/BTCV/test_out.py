
from monai.data import load_decathlon_datalist
data_dir = "Task09_Spleen"
datalist_json="Task09_Spleen/dataset.json"
val_files=load_decathlon_datalist(datalist_json, True, "validation", base_dir=data_dir)
#val_ds = data.Dataset(data=val_files, transform=val_transform)
print(val_files)	