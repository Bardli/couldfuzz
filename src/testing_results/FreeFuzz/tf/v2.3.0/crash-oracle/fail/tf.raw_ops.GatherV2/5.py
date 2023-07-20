import tensorflow as tf
try:
  params_tensor = tf.random.uniform([1, 40478], dtype=tf.float32)
  params = tf.identity(params_tensor)
  indices_tensor = tf.saturate_cast(tf.random.uniform([1, 40478], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint32)
  indices = tf.identity(indices_tensor)
  axis = -1
  batch_dims = 1024
  name = None
  results["res"] = tf.raw_ops.GatherV2(params=params,indices=indices,axis=axis,batch_dims=batch_dims,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
