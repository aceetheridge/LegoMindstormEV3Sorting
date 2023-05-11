import os

# All of the tensorflow models come from:
# https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md

#this is the name of the model that you will transfer learn too
CUSTOM_MODEL_NAME = 'my_ssd_mobnet' 
#this is the model you will be learning from, This model name needs to match the model zoo link 
PRETRAINED_MODEL_NAME = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8' 
# This is the model you will be cloning from the TensorFlow Model Zoo you can change it to any of the other ones you want to try.
PRETRAINED_MODEL_URL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz'
# This is a script to convert the .xml files in each class to .tfrecords for training tensorflow models.
TF_RECORD_SCRIPT_NAME = 'generate_tfrecord.py'
# This is a file that will be created to store the labels of the lego pieces or whatever you want to train against.
LABEL_MAP_NAME = 'label_map.pbtxt'

TEST = 'blah'

paths = {
    'WORKSPACE_PATH': os.path.join('Tensorflow', 'workspace'),
    'SCRIPTS_PATH': os.path.join('Tensorflow','scripts'),
    'APIMODEL_PATH': os.path.join('Tensorflow','models'),
    'ANNOTATION_PATH': os.path.join('tensorflow_config'),
    'IMAGES_PATH' : os.path.join('lego-mindstorm-ev3-pictures', 'yoloimages2'),
    'IMAGE_PATH': os.path.join('Tensorflow', 'workspace','images'),
    'MODEL_PATH': os.path.join('Tensorflow', 'workspace','models'),
    'PRETRAINED_MODEL_PATH': os.path.join('Tensorflow', 'workspace','pre-trained-models'),
    'CHECKPOINT_PATH': os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME), 
    'OUTPUT_PATH': os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'export'), 
    'TFJS_PATH':os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'tfjsexport'), 
    'TFLITE_PATH':os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'tfliteexport'), 
    'PROTOC_PATH':os.path.join('Tensorflow','protoc'),
 }

TENSORFLOW_CONFIG_FILES = os.path.join('tensorflow_config')

TRAIN_PATH = os.path.join(TENSORFLOW_CONFIG_FILES, 'train')
TEST_PATH = os.path.join(TENSORFLOW_CONFIG_FILES, 'test')
VALIDATION_PATH = os.path.join(TENSORFLOW_CONFIG_FILES, 'val')
TFLITE_DIR = os.path.join('RunTFLite')

files = {
    'PIPELINE_CONFIG':os.path.join('Tensorflow', 'workspace','models', CUSTOM_MODEL_NAME, 'pipeline.config'),
    'TF_RECORD_SCRIPT': os.path.join(paths['SCRIPTS_PATH'], TF_RECORD_SCRIPT_NAME), 
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_NAME)
}