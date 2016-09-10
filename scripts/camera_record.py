import picamera
import uuid

with picamera.PiCamera() as camera:
  camera.resolution = (1920, 1080)
  guid = str(uuid.uuid4())
  print('recording...')
  camera.start_recording('/home/pi/video/out/vid_' + guid + '.h264')
  camera.wait_recording(600)
  camera.stop_recording()
  print('recording ended.')

