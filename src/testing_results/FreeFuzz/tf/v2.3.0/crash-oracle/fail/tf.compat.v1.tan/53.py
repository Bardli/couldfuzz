import tensorflow as tf
try:
  x_tensor = tf.saturate_cast(tf.random.uniform([364, 384], minval=-128, maxval=128, dtype=tf.int64), dtype=tf.int8)
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.compat.v1.tan(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
