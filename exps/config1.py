#coding:utf8
from __future__ import print_function
import warnings
import getpass
import os

# ----------------------------------------------
# exp_id = 1,   pretrain_wo_imp
# LUT = Lookup Table
exp_desc_LUT = ['','pretrain_wo_imp',]


class DefaultConfig(object):
    GPU_HPC = (getpass.getuser() == 'zhangwenqiang')

    input_4_ch = False
    only_init_val = False # not train, only eval
    init_val = True
    # exp_desc = "pretrain_wo_impmap_128"
    # yolo rate loss and weighted mse loss
    # exp_desc = "yrl2_and_wml_r=0.2_gm=0.2"    
    # exp_desc = 'pretrain_w_impmap_64_r=0.2_gm=0.2'
    # exp_desc = "yrl2_nml_12"
    # exp_desc = "wml_w=500_no_imp_4ch_pn0.5"
    exp_id = 1
    exp_desc = exp_desc_LUT[exp_id]
    # resume = ""
    # exp_desc = "yrl_noimp_w=50"


    dataset_enable_bbox_center_crop = False
# lr decay controlled by file created
    use_file_decay_lr = True
    lr_decay_file = "signal/lr_decay_" + exp_desc

# model
    model = "ContentWeightedCNN"
    use_imp = False
    feat_num = 64  # defaut is 64

    # contrastive_degree = 0  # yrlv2 required
    input_original_bbox_inner = 25
    input_original_bbox_outer = 1

    mse_bbox_weight = 5
    rate_loss_weight = 0.2
    rate_loss_threshold = 0.12      # 0.12 | 0.17 | 0.32 | 0.49 |


# save path
    # test_imgs_save_path = ("/home/snk/Desktop/CNN-based-Image-Compression-Guided-by-YOLOv2/logs/test_imgs_" if not GPU_HPC else "/home/zhangwenqiang/jobs/CNN-based-Image-Compression-Guided-by-YOLOv2/logs/test_imgs_") + exp_desc
    test_imgs_save_path = "test_imgs_saved/"
    save_test_img = True

# datasets
    local_ds_root = "/home/snk/WindowsDisk/Download/KITTI/cmpr_datasets/"
    hpc_ds_root = "/share/Dataset/KITTI/"
    train_data_list = os.path.join(local_ds_root,"traintest.txt") if not GPU_HPC else os.path.join(hpc_ds_root, "traintest.txt")
    val_data_list = os.path.join(local_ds_root,"val_subset.txt") if not GPU_HPC else os.path.join(hpc_ds_root, "val.txt")
    test_data_list = os.path.join(local_ds_root,"test_subset.txt") if not GPU_HPC else os.path.join(hpc_ds_root,"test.txt")
# training
    batch_size = 32
    use_gpu = True
    num_workers = 8
    max_epoch = 200*3
    lr = 1e-4
    lr_decay = 0.1
    lr_anneal_epochs = 200
    use_early_adjust = False
    tolerant_max = 3
    weight_decay = 0
# display
    print_freq = 1 # by iteration
    eval_interval = 1 # by epoch
    save_interval = 1 # by epoch
    print_smooth = True

    plot_path = 'plot'
    log_path = 'log' 
# debug
    debug_file = "debug/info"
# finetune
    # resume = ""

    finetune = False  # continue training or finetune when given a resume file

# ---------------------------------------------------------
    def __getattr__(self, attr_name):
        return None
    
    def parse(self, kwargs={}):
        for k,v in kwargs.items():
            if not hasattr(self, k):
                warnings.warn("Warning: opt has not attribute %s" % k)
                print ("Warning: opt has not attribute %s" % k)
            setattr(self, k, v)
        
        print('User Config:\n')
        print('-' * 30)
        for k,v in self.__class__.__dict__.items():
            if not k.startswith('__') and k != 'parse':
                print(k,":",getattr(self, k))
        print('-' * 30)
        print('Good Luck!')
        
opt = DefaultConfig()
if not os.path.exists(opt.plot_path):
    print ('mkdir', opt.plot_path)
    os.makedirs(opt.plot_path)

if not os.path.exists(opt.log_path):
    print ('mkdir', opt.log_path)
    os.makedirs(opt.log_path)

if __name__ == '__main__':
    opt.parse()