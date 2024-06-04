_base_ = [
    '../_base_/models/fcn_unet_s5-d16.py', '../_base_/datasets/retotec_dataset.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_5k.py'
]
crop_size = (1024, 1024)
data_preprocessor = dict(size=crop_size)
model = dict(
    data_preprocessor=data_preprocessor)
