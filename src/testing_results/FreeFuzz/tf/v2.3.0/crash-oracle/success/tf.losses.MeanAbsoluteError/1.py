import tensorflow as tf
try:
  results["res"] = tf.losses.MeanAbsoluteError()
except Exception as e:
  results["err"] = "Error:"+str(e)
