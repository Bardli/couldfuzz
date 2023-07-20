import tensorflow as tf
try:
  seed_tensor = tf.random.uniform([2], minval=-256, maxval=257, dtype=tf.int32)
  seed = tf.identity(seed_tensor)
  results["res"] = tf.keras.initializers.GlorotUniform(seed=seed,)
except Exception as e:
  results["err"] = "Error:"+str(e)
