import tensorflow as tf
try:
  x_tensor = tf.complex(tf.random.uniform([3, 50], dtype=tf.float64),tf.random.uniform([3, 50], dtype=tf.float64))
  x = tf.identity(x_tensor)
  results["res"] = tf.compat.v1.tan(x=x,)
except Exception as e:
  results["err"] = "Error:"+str(e)
