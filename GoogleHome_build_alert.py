# Standard
import time, urllib, re

# Third party
import pychromecast
import pafy

def main(test_run:bool, device_name:str = "None", start_time:int = 0, duration:int = 30):
    """
    Main function that plays a YouTube video on your Google device when triggered

    Input
     : Test_Run: bool - Boolean to trigger true or false chime. Intended to be hooked up to pytest asserts
     : device_name: str  - Name of particular Chromecast/GoogleHomeMini device on the same network. If the name
    isn't known, print all devices using the get_chromecasts() function and correspondingly filter
     : Start Time: In seconds of when to skip forward to in the video
     : Duration: Time to play before interrupting

    Returns: None
    """

    # Get all chromecast devices on the same network
    chromecasts = pychromecast.get_chromecasts()
    cast_device = next(dev for dev in chromecasts if dev.device.friendly_name == device_name)

    mc = cast_device.media_controller

    # Set up the device and wait for an instruction
    cast_device.wait()

    if test_run:
        # Success
        media_metadata = pafy.new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        url = media_metadata.getbest('mp4').url_https
        mc.play_media(url, 'video/mp4', current_time=start_time)
        time.sleep(duration)
        mc.stop()
        
    else:
        # Failure
        media_metadata = pafy.new("https://www.youtube.com/watch?v=LukyMYp2noo")
        url = media_metadata.getbest('mp4').url_https
        mc.play_media(url, 'video/mp4')
        mc.stop()


if __name__ == '__main__':
    main(test_run=True, device_name="Test_Device")

