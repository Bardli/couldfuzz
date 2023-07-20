import tensorflow as tf
try:
  x_tensor = tf.random.uniform([410, 512], dtype=tf.float32)
  x = tf.identity(x_tensor)
  name_tensor = tf.random.uniform([2, 2], dtype=tf.float64)
  name = tf.identity(name_tensor)
  results["res"] = tf.asin(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
