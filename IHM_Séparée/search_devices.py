class search_devices :
    def search_devices():
        global nearby_devices
        nearby_devices = bluetooth.discover_devices()
        update_devices_list()