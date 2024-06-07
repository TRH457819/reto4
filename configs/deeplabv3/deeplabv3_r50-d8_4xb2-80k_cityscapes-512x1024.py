_base_ = [
    '../_base_/models/deeplabv3_r50-d8.py', '../_base_/datasets/retotec_dataset.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
]
crop_size = (256, 256)
data_preprocessor = dict(size=crop_size)
model = dict(data_preprocessor=data_preprocessor)
