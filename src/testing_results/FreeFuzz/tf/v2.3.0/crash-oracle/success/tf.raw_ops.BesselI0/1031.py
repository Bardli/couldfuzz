import tensorflow as tf
try:
  x_tensor = tf.random.uniform([5], dtype=tf.float64)
  x = tf.identity(x_tensor)
  name = None
  results["res"] = tf.raw_ops.BesselI0(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)