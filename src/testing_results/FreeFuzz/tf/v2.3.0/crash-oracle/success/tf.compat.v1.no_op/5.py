import tensorflow as tf
try:
  name = None
  results["res"] = tf.compat.v1.no_op(name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
