results = dict()
import tensorflow as tf
import time
try:
  try:
    map_func_0_tensor = tf.saturate_cast(tf.random.uniform([10, 5], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint16)
    map_func_0 = tf.identity(map_func_0_tensor)
    map_func_1_tensor = tf.cast(tf.random.uniform([10, 5], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
    map_func_1 = tf.identity(map_func_1_tensor)
    map_func = [map_func_0,map_func_1,]
    cycle_length = "1"
    block_length = None
    sloppy = None
    results["res_low"] = tf.data.experimental.parallel_interleave(map_func=map_func,cycle_length=cycle_length,block_length=block_length,sloppy=sloppy,)
    t_start = time.time()
    results["res_low"] = tf.data.experimental.parallel_interleave(map_func=map_func,cycle_length=cycle_length,block_length=block_length,sloppy=sloppy,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    map_func_0 = tf.identity(map_func_0_tensor)
    map_func_0 = tf.cast(map_func_0, tf.uint16)
    map_func_1 = tf.identity(map_func_1_tensor)
    map_func_1 = tf.cast(map_func_1, tf.bool)
    map_func = [map_func_0,map_func_1,]
    results["res_high"] = tf.data.experimental.parallel_interleave(map_func=map_func,cycle_length=cycle_length,block_length=block_length,sloppy=sloppy,)
    t_start = time.time()
    results["res_high"] = tf.data.experimental.parallel_interleave(map_func=map_func,cycle_length=cycle_length,block_length=block_length,sloppy=sloppy,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)