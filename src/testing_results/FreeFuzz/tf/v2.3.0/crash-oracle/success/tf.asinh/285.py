import tensorflow as tf
try:
  x_tensor = tf.random.uniform([376, 512], dtype=tf.float32)
  x = tf.identity(x_tensor)
  name = -1024
  results["res"] = tf.asinh(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)