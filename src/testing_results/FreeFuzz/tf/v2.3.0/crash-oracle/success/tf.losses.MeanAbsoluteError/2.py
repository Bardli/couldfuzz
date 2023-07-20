import tensorflow as tf
try:
  reduction = "none"
  results["res"] = tf.losses.MeanAbsoluteError(reduction=reduction,)
except Exception as e:
  results["err"] = "Error:"+str(e)
