import tensorflow as tf
try:
  seed_0 = -1
  seed_1 = 1
  seed = [seed_0,seed_1,]
  results["res"] = tf.keras.initializers.GlorotUniform(seed=seed,)
except Exception as e:
  results["err"] = "Error:"+str(e)
