results = dict()
import tensorflow as tf
import time
try:
  try:
    params_tensor = tf.random.uniform([1, 246534], dtype=tf.float16)
    params = tf.identity(params_tensor)
    indices_tensor = tf.saturate_cast(tf.random.uniform([1, 246534], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int8)
    indices = tf.identity(indices_tensor)
    axis = -2
    batch_dims = 1
    name = None
    results["res_low"] = tf.raw_ops.GatherV2(params=params,indices=indices,axis=axis,batch_dims=batch_dims,name=name,)
    t_start = time.time()
    results["res_low"] = tf.raw_ops.GatherV2(params=params,indices=indices,axis=axis,batch_dims=batch_dims,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    params = tf.identity(params_tensor)
    params = tf.cast(params, tf.float32)
    indices = tf.identity(indices_tensor)
    indices = tf.cast(indices, tf.int32)
    results["res_high"] = tf.raw_ops.GatherV2(params=params,indices=indices,axis=axis,batch_dims=batch_dims,name=name,)
    t_start = time.time()
    results["res_high"] = tf.raw_ops.GatherV2(params=params,indices=indices,axis=axis,batch_dims=batch_dims,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
