import tensorflow as tf
try:
  name = "global_average_pooling2d"
  trainable = False
  dtype = "float32"
  data_format = "channels_first"
  results["res"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,dtype=dtype,data_format=data_format,)
except Exception as e:
  results["err"] = "Error:"+str(e)
