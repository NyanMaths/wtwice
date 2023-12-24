#include <iostream>
#include <cstring>
#include <opencv4/opencv2/opencv.hpp>

#include "upscaler.hpp"
#include "image.hpp"

using namespace cv;


Upscaler::Upscaler ()
{

}

Upscaler::~Upscaler ()
{

}


Image* Upscaler::getPicture (std::string picture_path)
{
    Image* picture(new Image(imread(picture_path, IMREAD_ANYCOLOR)));  // assumes 8bit RGB

    if (picture->empty())
    {
        std::cout<<"Error trying to read image "<<picture_path<<std::endl;
        std::exit(1);
    }

    return picture;
}

int Upscaler::start(const std::string input_picture_path, const std::string output_picture_path, const size_t ratio, const int8_t denoising)
{
    Image* picture(getPicture(input_picture_path));
    Image* input_picture(new Image);
    picture->convertTo(*input_picture, CV_32FC3);

    Image* upscaled_picture(upscalePicture(input_picture, ratio, denoising));

    Image converted_upscaler_picture;
    upscaled_picture->convertTo(converted_upscaler_picture, CV_8UC3);


    if (!imwrite(output_picture_path, converted_upscaler_picture))
    {
        std::cout<<"Error trying to save image "<<output_picture_path<<std::endl;

        return 1;
    }


    return 0;
}
