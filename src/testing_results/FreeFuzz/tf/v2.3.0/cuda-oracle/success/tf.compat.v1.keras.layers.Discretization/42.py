results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      bin_boundaries = None
      num_bins = -16
      epsilon = None
      results["res_cpu"] = tf.compat.v1.keras.layers.Discretization(bin_boundaries=bin_boundaries,num_bins=num_bins,epsilon=epsilon,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      results["res_gpu"] = tf.compat.v1.keras.layers.Discretization(bin_boundaries=bin_boundaries,num_bins=num_bins,epsilon=epsilon,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
