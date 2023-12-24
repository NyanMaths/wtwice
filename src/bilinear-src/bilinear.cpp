/*
This is a bilinear filter, a better version of fastblend, much faster than the previous Python implementation.
Author : Turbo Giga Chad
*/

#include <iostream>

#include "bilinear.hpp"

using namespace cv;


Bilinear::Bilinear () : Upscaler()
{

}
Bilinear::~Bilinear ()
{

}


Image* Bilinear::upscalePicture(Image* picture, const size_t ratio, const int8_t)
{
    const Size input_size(picture->size());
    const Size output_size(input_size.width * ratio, input_size.height * ratio);
    const float ratio_c(float(input_size.height - 1) / float(output_size.height - 1));

    Image* output_picture(new Image(output_size, CV_32FC3));


    for (size_t i(0) ; i < output_size.height ; i++)
    {
        for (size_t j(0) ; j < output_size.width ; j++)
        {
            const size_t x_low(std::floor(ratio_c * j)), y_low(std::floor(ratio_c * i));
            const size_t x_high(std::ceil(ratio_c * j)), y_high(std::ceil(ratio_c * i));

            const float x_weight(ratio_c*j - x_low), y_weight(ratio_c * i - y_low);

            const Vec3f a(picture->pixel(y_low, x_low));
            const Vec3f b(picture->pixel(y_low, x_high));
            const Vec3f c(picture->pixel(y_high, x_low));
            const Vec3f d(picture->pixel(y_high, x_high));


            const Vec3f output_pixel(a*(1-x_weight)*(1-y_weight) + b*x_weight*(1-y_weight) + c*(1-x_weight)*y_weight + d*x_weight*y_weight);

            output_picture->pixel(i, j) = output_pixel;
        }
    }


    return output_picture;
}


int main (int argc, char** argv)
{
    Bilinear upscaler;

    if (argc < 3)
    {
        std::cout<<"u should get sudo rm -rf / ed for this";
        return 1;
    }
    else if (argc < 4)
        return upscaler.start(argv[1], argv[2]);

    else if (argc < 5)
        return upscaler.start(argv[1], argv[2], std::stoi(argv[3]));

    return upscaler.start(argv[1], argv[2], std::stoi(argv[3]), std::stoi(argv[4]));
}
