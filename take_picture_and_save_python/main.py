import pyzed.sl as sl
import cv2

def capture_image_in_vga():
    # Create a Camera object
    zed = sl.Camera()

    # Set initialization parameters
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.VGA  # Set camera to VGA resolution
    init_params.camera_fps = 15  # Set the frame rate (can adjust based on your requirements)

    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        print(f"Failed to open the camera: {err}")
        exit(1)

    # Create an image object to store captured image
    image = sl.Mat()

    # Capture an image
    if zed.grab() == sl.ERROR_CODE.SUCCESS:
        # Retrieve the captured image
        zed.retrieve_image(image, sl.VIEW.LEFT)

        # Get the image data in an OpenCV format
        image_ocv = image.get_data()

        # Save the image
        cv2.imwrite("captured_image_vga.jpg", image_ocv)
        print("Image has been saved as 'captured_image_vga.jpg'")

    # Close the camera
    zed.close()

if __name__ == "__main__":
    capture_image_in_vga()
