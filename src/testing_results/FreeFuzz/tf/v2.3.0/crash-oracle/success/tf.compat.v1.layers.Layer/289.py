import tensorflow as tf
try:
  trainable = True
  name_tensor = tf.random.uniform([1, 1], minval=-256, maxval=257, dtype=tf.int32)
  name = tf.identity(name_tensor)
  dtype = None
  results["res"] = tf.compat.v1.layers.Layer(trainable=trainable,name=name,dtype=dtype,)
except Exception as e:
  results["err"] = "Error:"+str(e)
