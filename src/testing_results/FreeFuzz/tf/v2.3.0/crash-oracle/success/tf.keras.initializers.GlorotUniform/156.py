import tensorflow as tf
try:
  seed = 1
  results["res"] = tf.keras.initializers.GlorotUniform(seed=seed,)
except Exception as e:
  results["err"] = "Error:"+str(e)
