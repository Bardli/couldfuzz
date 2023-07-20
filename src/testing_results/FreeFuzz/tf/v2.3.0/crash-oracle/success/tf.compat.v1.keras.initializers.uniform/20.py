import tensorflow as tf
try:
  minval = 10.950000000000003
  maxval = 0.05
  seed = None
  results["res"] = tf.compat.v1.keras.initializers.uniform(minval=minval,maxval=maxval,seed=seed,)
except Exception as e:
  results["err"] = "Error:"+str(e)
