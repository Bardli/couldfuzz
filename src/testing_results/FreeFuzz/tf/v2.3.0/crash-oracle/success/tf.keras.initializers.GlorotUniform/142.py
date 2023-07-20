import tensorflow as tf
try:
  seed = -4.0
  results["res"] = tf.keras.initializers.GlorotUniform(seed=seed,)
except Exception as e:
  results["err"] = "Error:"+str(e)
