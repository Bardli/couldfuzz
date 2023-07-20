results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      seed_0 = 1
      seed_1 = 2
      seed = [seed_0,seed_1,]
      results["res_cpu"] = tf.keras.initializers.GlorotUniform(seed=seed,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      seed = [seed_0,seed_1,]
      results["res_gpu"] = tf.keras.initializers.GlorotUniform(seed=seed,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
