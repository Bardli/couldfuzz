import tensorflow as tf
try:
  minval = -63.0
  maxval = 0.05
  seed_tensor = tf.random.uniform([2, 1], minval=-256, maxval=257, dtype=tf.int32)
  seed = tf.identity(seed_tensor)
  seed = tf.Variable(seed)
  results["res"] = tf.compat.v1.keras.initializers.uniform(minval=minval,maxval=maxval,seed=seed,)
except Exception as e:
  results["err"] = "Error:"+str(e)
