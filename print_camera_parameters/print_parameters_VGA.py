import pyzed.sl as sl

def print_camera_information(camera):
    # Retrieve camera information
    cam_info = camera.get_camera_information()

    # Access calibration data
    left_camera_calibration = cam_info.camera_configuration.calibration_parameters.left_cam
    right_camera_calibration = cam_info.camera_configuration.calibration_parameters.right_cam

    # Print left camera information
    print("Left Camera:")
    print(f"FX: {left_camera_calibration.fx}, FY: {left_camera_calibration.fy}")
    print(f"CX: {left_camera_calibration.cx}, CY: {left_camera_calibration.cy}")
    print("Distortion Coefficients:", left_camera_calibration.disto)

    # Print right camera information
    print("\nRight Camera:")
    print(f"FX: {right_camera_calibration.fx}, FY: {right_camera_calibration.fy}")
    print(f"CX: {right_camera_calibration.cx}, CY: {right_camera_calibration.cy}")
    print("Distortion Coefficients:", right_camera_calibration.disto)

def main():
    zed = sl.Camera()

    # Set camera resolution to VGA as the closest approximation to 360p
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.VGA  # Adjusted to VGA for lower resolution
    # resolution is 672 * 376
    init_params.camera_fps = 60  # Adjust FPS if needed based on the capabilities at VGA resolution

    if zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
        print("Failed to open the camera")
        exit(1)
        
    print_camera_information(zed)

    zed.close()

if __name__ == "__main__":
    main()
