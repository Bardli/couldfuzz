import tensorflow as tf
try:
  minval = 1
  maxval = 1
  seed = 122
  results["res"] = tf.compat.v1.keras.initializers.uniform(minval=minval,maxval=maxval,seed=seed,)
except Exception as e:
  results["err"] = "Error:"+str(e)
