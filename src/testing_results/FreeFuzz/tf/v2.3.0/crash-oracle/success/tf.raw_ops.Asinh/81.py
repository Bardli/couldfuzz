import tensorflow as tf
try:
  x_tensor = tf.random.uniform([440, 512], dtype=tf.float32)
  x = tf.identity(x_tensor)
  name = -1067.0
  results["res"] = tf.raw_ops.Asinh(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
