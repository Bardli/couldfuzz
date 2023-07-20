import tensorflow as tf
try:
  minval = -1024.0
  maxval = 1e+20
  seed = None
  results["res"] = tf.compat.v1.keras.initializers.uniform(minval=minval,maxval=maxval,seed=seed,)
except Exception as e:
  results["err"] = "Error:"+str(e)