import tensorflow as tf
try:
  minval = -0.05
  maxval = 5.049999999999997
  seed = None
  results["res"] = tf.compat.v1.keras.initializers.uniform(minval=minval,maxval=maxval,seed=seed,)
except Exception as e:
  results["err"] = "Error:"+str(e)
