import tensorflow as tf
try:
  results["res"] = tf.compat.v1.layers.Layer()
except Exception as e:
  results["err"] = "Error:"+str(e)
