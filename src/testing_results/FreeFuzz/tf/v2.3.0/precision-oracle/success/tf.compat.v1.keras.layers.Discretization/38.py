results = dict()
import tensorflow as tf
import time
try:
  try:
    bin_boundaries = None
    num_bins = -16
    epsilon = None
    results["res_low"] = tf.compat.v1.keras.layers.Discretization(bin_boundaries=bin_boundaries,num_bins=num_bins,epsilon=epsilon,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.keras.layers.Discretization(bin_boundaries=bin_boundaries,num_bins=num_bins,epsilon=epsilon,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    results["res_high"] = tf.compat.v1.keras.layers.Discretization(bin_boundaries=bin_boundaries,num_bins=num_bins,epsilon=epsilon,)
    t_start = time.time()
    results["res_high"] = tf.compat.v1.keras.layers.Discretization(bin_boundaries=bin_boundaries,num_bins=num_bins,epsilon=epsilon,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
