import tensorflow as tf
try:
  seed = 122
  results["res"] = tf.initializers.glorot_normal(seed=seed,)
except Exception as e:
  results["err"] = "Error:"+str(e)
