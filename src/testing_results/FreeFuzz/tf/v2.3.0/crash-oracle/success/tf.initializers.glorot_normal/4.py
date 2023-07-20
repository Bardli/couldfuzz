import tensorflow as tf
try:
  results["res"] = tf.initializers.glorot_normal()
except Exception as e:
  results["err"] = "Error:"+str(e)
