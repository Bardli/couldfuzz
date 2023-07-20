import tensorflow as tf
try:
  map_func_0_tensor = tf.complex(tf.random.uniform([10, 5], dtype=tf.float32),tf.random.uniform([10, 5], dtype=tf.float32))
  map_func_0 = tf.identity(map_func_0_tensor)
  map_func_1_tensor = tf.saturate_cast(tf.random.uniform([10, 5], minval=-128, maxval=128, dtype=tf.int64), dtype=tf.int8)
  map_func_1 = tf.identity(map_func_1_tensor)
  map_func = [map_func_0,map_func_1,]
  cycle_length = "/cpu:0"
  block_length = ""
  sloppy = None
  results["res"] = tf.data.experimental.parallel_interleave(map_func=map_func,cycle_length=cycle_length,block_length=block_length,sloppy=sloppy,)
except Exception as e:
  results["err"] = "Error:"+str(e)
