import tensorflow as tf
try:
  x_tensor = tf.random.uniform([366, 512], dtype=tf.bfloat16)
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.asin(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
