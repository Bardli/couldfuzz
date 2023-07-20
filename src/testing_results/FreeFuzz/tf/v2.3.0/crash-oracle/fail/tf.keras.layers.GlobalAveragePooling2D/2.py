import tensorflow as tf
try:
  data_format = "1"
  results["res"] = tf.keras.layers.GlobalAveragePooling2D(data_format=data_format,)
except Exception as e:
  results["err"] = "Error:"+str(e)
