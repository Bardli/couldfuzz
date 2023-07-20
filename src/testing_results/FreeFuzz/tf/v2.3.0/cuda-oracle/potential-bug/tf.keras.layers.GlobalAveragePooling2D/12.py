results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      name = "global_average_pooling2d_1"
      trainable = True
      batch_input_shape_0 = 4
      batch_input_shape_1 = 3
      batch_input_shape_2 = 6
      batch_input_shape_3 = 5
      batch_input_shape = [batch_input_shape_0,batch_input_shape_1,batch_input_shape_2,batch_input_shape_3,]
      dtype = None
      data_format = "channels_last"
      results["res_cpu"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,batch_input_shape=batch_input_shape,dtype=dtype,data_format=data_format,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      batch_input_shape = [batch_input_shape_0,batch_input_shape_1,batch_input_shape_2,batch_input_shape_3,]
      results["res_gpu"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,batch_input_shape=batch_input_shape,dtype=dtype,data_format=data_format,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
