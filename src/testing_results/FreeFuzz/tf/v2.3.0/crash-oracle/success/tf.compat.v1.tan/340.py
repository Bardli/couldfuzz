import tensorflow as tf
try:
  x_tensor = tf.random.uniform([380, 384], dtype=tf.float32)
  x = tf.identity(x_tensor)
  name = 77.0
  results["res"] = tf.compat.v1.tan(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
