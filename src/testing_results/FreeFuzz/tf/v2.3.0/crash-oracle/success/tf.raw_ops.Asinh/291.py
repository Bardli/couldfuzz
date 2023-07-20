import tensorflow as tf
try:
  x_tensor = tf.random.uniform([0, 384, 1], dtype=tf.float64)
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.raw_ops.Asinh(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
