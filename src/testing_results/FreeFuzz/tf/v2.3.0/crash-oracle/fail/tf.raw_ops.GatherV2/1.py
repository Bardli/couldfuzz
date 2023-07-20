import tensorflow as tf
try:
  params_tensor = tf.random.uniform([1, 20, 512], dtype=tf.float32)
  params = tf.identity(params_tensor)
  indices_tensor = tf.random.uniform([4], minval=-256, maxval=257, dtype=tf.int32)
  indices = tf.identity(indices_tensor)
  axis = True
  batch_dims = 16
  name = None
  results["res"] = tf.raw_ops.GatherV2(params=params,indices=indices,axis=axis,batch_dims=batch_dims,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
