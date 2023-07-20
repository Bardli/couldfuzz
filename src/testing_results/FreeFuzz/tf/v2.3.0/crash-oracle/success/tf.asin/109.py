import tensorflow as tf
try:
  x_tensor = tf.random.uniform([378, 384], dtype=tf.float32)
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.asin(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
