# Define critical settings and/or override defaults specified in
# settings.py. Copy this file to settings_local.py in the same
# directory as settings.py and edit. Any settings defined here
# will override those defined in settings.py



# Set this to point to your compiled checkout of caffe
caffevis_caffe_root      = '/home/xu/soft/caffe'

# Load model: caffenet-yos
# Path to caffe deploy prototxt file. Minibatch size should be 1.
caffevis_deploy_prototxt = '/home/xu/projects/dai/robocupspl/notebooks/ball_caffe.prototxt'

# Path to network weights to load.
caffevis_network_weights = '/home/xu/projects/dai/robocupspl/notebooks/ball_caffe.caffemodel'

# Other optional settings; see complete documentation for each in settings.py.
caffevis_data_mean       = '/home/xu/projects/dai/robocupspl/notebooks/ball_train.mean.npy'
caffevis_labels          = '/home/xu/projects/dai/robocupspl/notebooks/ball_labels.txt'

static_files_dir = '/home/xu/projects/dai/robocupspl_db/ball_mix'

caffevis_label_layers    = ('ip2', 'prob')
caffevis_prob_layer      = 'prob'
caffevis_unit_jpg_dir    = '%DVT_ROOT%/models/caffenet-yos/unit_jpg_vis'
caffevis_jpgvis_layers   = ['conv1', 'ip1', 'ip2', 'prob']
caffevis_jpgvis_remap    = {'pool1': 'conv1'}
def caffevis_layer_pretty_name_fn(name):
    return name.replace('pool','p').replace('norm','n')

# Use GPU? Default is True.
caffevis_mode_gpu = False
# Display tweaks.
# Scale all window panes in UI by this factor
#global_scale = 1.0
# Scale all fonts by this factor    
#global_font_size = 1.0
