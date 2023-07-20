import tensorflow as tf
try:
  x_tensor = tf.cast(tf.random.uniform([358, 384], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
  x = tf.identity(x_tensor)
  name = tf.uint8
  results["res"] = tf.asin(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
