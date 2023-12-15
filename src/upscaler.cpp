#include <iostream>
#include <cstring>
#include <opencv2/core/matx.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv4/opencv2/opencv.hpp>

#include "upscaler.hpp"

using namespace cv;


Upscaler::Upscaler ()
{

}

Upscaler::~Upscaler ()
{

}


Mat* Upscaler::getPicture (std::string picture_path)
{
    Mat* picture(new Mat(imread(picture_path, IMREAD_ANYCOLOR)));  // assumes 8bit RGB

    if (picture->empty())
    {
        std::cout<<"Error trying to read image "<<picture_path<<std::endl;
        std::exit(1);
    }

    return picture;
}

int Upscaler::start(const std::string input_picture_path, const std::string output_picture_path, const size_t ratio, const int8_t denoising)
{
    Mat* picture(getPicture(input_picture_path));
    Mat* input_picture(new Mat);
    picture->convertTo(*input_picture, CV_32FC3);

    Mat* upscaled_picture(upscalePicture(input_picture, ratio, denoising));

    Mat converted_upscaler_picture;
    upscaled_picture->convertTo(converted_upscaler_picture, CV_8UC3);


    if (!imwrite(output_picture_path, converted_upscaler_picture))
    {
        std::cout<<"Error trying to save image "<<output_picture_path<<std::endl;

        return 1;
    }


    return 0;
}
