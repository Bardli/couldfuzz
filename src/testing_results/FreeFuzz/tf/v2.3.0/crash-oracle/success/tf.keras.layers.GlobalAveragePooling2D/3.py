import tensorflow as tf
try:
  name = "global_average_pooling2d_1"
  trainable = False
  dtype = "float32"
  data_format = "channels_last"
  batch_input_shape_0 = 3
  batch_input_shape_1 = 5
  batch_input_shape_2 = 6
  batch_input_shape_3 = 4
  batch_input_shape = [batch_input_shape_0,batch_input_shape_1,batch_input_shape_2,batch_input_shape_3,]
  results["res"] = tf.keras.layers.GlobalAveragePooling2D(name=name,trainable=trainable,dtype=dtype,data_format=data_format,batch_input_shape=batch_input_shape,)
except Exception as e:
  results["err"] = "Error:"+str(e)
