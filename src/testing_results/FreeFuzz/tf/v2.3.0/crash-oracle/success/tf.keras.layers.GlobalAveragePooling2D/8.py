import tensorflow as tf
try:
  data_format = "channels_last"
  results["res"] = tf.keras.layers.GlobalAveragePooling2D(data_format=data_format,)
except Exception as e:
  results["err"] = "Error:"+str(e)
