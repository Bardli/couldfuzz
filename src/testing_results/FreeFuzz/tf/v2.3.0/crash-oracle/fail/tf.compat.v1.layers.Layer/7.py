import tensorflow as tf
try:
  trainable = True
  name = None
  dtype_tensor = tf.random.uniform([2, 1], minval=-256, maxval=257, dtype=tf.int32)
  dtype = tf.identity(dtype_tensor)
  results["res"] = tf.compat.v1.layers.Layer(trainable=trainable,name=name,dtype=dtype,)
except Exception as e:
  results["err"] = "Error:"+str(e)
