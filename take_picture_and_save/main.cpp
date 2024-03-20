#include <sl/Camera.hpp>
#include <iostream>

int main(int argc, char **argv) {
    sl::Camera zed;

    // Set configuration parameters
    sl::InitParameters init_params;
    init_params.camera_resolution = sl::RESOLUTION::HD720; // Use your specific resolution
    init_params.depth_mode = sl::DEPTH_MODE::NONE; // Assuming no depth is needed for this capture
    init_params.coordinate_units = sl::UNIT::METER; // Adjust as needed

    // Open the camera
    auto err = zed.open(init_params);
    if (err != sl::ERROR_CODE::SUCCESS) {
        std::cout << "Error opening ZED camera: " << sl::toString(err) << std::endl;
        return 1; // Exit if an error occurred
    }

    // Capture an image
    sl::Mat image;
    if (zed.grab() == sl::ERROR_CODE::SUCCESS) {
        zed.retrieveImage(image, sl::VIEW::LEFT); // Assuming you want the left image

        // Save the image to file
        sl::String image_filename = "zed_image.png"; // Use sl::String here
        if (image.write(image_filename) == sl::ERROR_CODE::SUCCESS) { // Check if the operation was successful
            std::cout << "Image saved to " << image_filename.get() << std::endl;
        } else {
            std::cout << "Failed to save image." << std::endl;
        }

    } else {
        std::cout << "Error capturing image." << std::endl;
    }

    // Close the camera
    zed.close();
    return 0;
}
