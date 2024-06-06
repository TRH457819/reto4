_base_ = [
    '../_base_/models/fastfcn_r50-d32_jpu_psp.py', '../_base_/datasets/retotec_dataset.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_5k.py'
]
crop_size = (512, 1024)
data_preprocessor = dict(size=crop_size)
model = dict(
    data_preprocessor=data_preprocessor,
    decode_head=dict(num_classes=7),
    auxiliary_head=dict(num_classes=7),
    # model training and testing settings
    train_cfg=dict(),
    test_cfg=dict(mode='whole'))
train_dataloader = dict(batch_size=4, num_workers=4)
val_dataloader = dict(batch_size=1, num_workers=4)
test_dataloader = val_dataloader