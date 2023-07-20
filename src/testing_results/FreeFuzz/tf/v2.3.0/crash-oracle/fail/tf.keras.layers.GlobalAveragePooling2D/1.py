import tensorflow as tf
try:
  name = True
  trainable = True
  dtype = "float32"
  data_format = 0
  results["res"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,dtype=dtype,data_format=data_format,)
except Exception as e:
  results["err"] = "Error:"+str(e)
