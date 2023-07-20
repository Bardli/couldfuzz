import tensorflow as tf
try:
  data_format = "zeros"
  keepdims = False
  results["res"] = tf.compat.v1.keras.layers.GlobalMaxPooling2D(data_format=data_format,keepdims=keepdims,)
except Exception as e:
  results["err"] = "Error:"+str(e)
