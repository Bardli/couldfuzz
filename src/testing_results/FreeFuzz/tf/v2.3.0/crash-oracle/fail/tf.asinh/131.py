import tensorflow as tf
try:
  x_tensor = tf.random.uniform([412, 511], dtype=tf.float16)
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.asinh(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
