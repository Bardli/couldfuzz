import tensorflow as tf
try:
  trainable = 1024
  name = None
  dtype = None
  results["res"] = tf.compat.v1.layers.Layer(trainable=trainable,name=name,dtype=dtype,)
except Exception as e:
  results["err"] = "Error:"+str(e)
