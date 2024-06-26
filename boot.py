import storage
storage.remount("/", readonly=True)
m = storage.getmount("/")
m.label = "LULUR"
storage.remount("/", readonly=False)
storage.enable_usb_drive()
