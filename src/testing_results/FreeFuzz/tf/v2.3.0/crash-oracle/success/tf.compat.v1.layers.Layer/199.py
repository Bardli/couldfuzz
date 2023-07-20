import tensorflow as tf
try:
  trainable = True
  name = None
  dtype = tf.int64
  results["res"] = tf.compat.v1.layers.Layer(trainable=trainable,name=name,dtype=dtype,)
except Exception as e:
  results["err"] = "Error:"+str(e)
