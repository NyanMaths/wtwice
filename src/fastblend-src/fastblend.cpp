#include <iostream>

#include "fastblend.hpp"

using namespace cv;


Fastblend::Fastblend () : Upscaler()
{

}
Fastblend::~Fastblend ()
{

}


Image* Fastblend::upscalePicture(Image* picture, const size_t, const int8_t)
{
    const Size picture_size(picture->size());
    const Size output_picture_size(picture_size.width * 2 - 1, picture_size.height * 2 - 1);

    Image* output_picture(new Image(output_picture_size, CV_32FC3));


    for (size_t row(0) ; row < picture_size.height ; row++)
    {
        for (size_t col(0) ; col < picture_size.width ; col++)
        {
            output_picture->pixel(row * 2, col * 2) = picture->pixel(row, col);
        }
    }


    for (size_t row(1) ; row < output_picture_size.height - 1 ; row += 2)
    {
        for (size_t col(1) ; col < output_picture_size.width - 1 ; col += 2)
        {
            const Vec3f a(output_picture->pixel(row - 1, col - 1));
            const Vec3f b(output_picture->pixel(row - 1, col + 1));
            const Vec3f c(output_picture->pixel(row + 1, col - 1));
            const Vec3f d(output_picture->pixel(row + 1, col + 1));


            output_picture->pixel(row, col) = (a + b + c + d) / 4.0;
        
            output_picture->pixel(row - 1, col) = (a + b) / 2.0;
            output_picture->pixel(row, col + 1) = (b + d) / 2.0;
        }
    }

    for (size_t row(1) ; row < output_picture_size.height - 1 ; row += 2)
        output_picture->pixel(row, 0) = (output_picture->pixel(row - 1, 0) + output_picture->pixel(row + 1, 0)) / 2.0;

    size_t last_pixel_height(output_picture_size.height - 1);
    for (size_t col(1) ; col < output_picture_size.width - 1 ; col += 2)
        output_picture->pixel(col, last_pixel_height) = (output_picture->pixel(last_pixel_height, col - 1) + output_picture->pixel(last_pixel_height, col + 1)) / 2.0;


    return output_picture;
}


int main (int argc, char** argv)
{
    Fastblend upscaler;

    if (argc < 3)
    {
        std::cout<<"a bit too few arguments to make this program work"<<std::endl;
        return 1;
    }
    else if (argc < 4)
        return upscaler.start(argv[1], argv[2]);

    else if (argc < 5)
        return upscaler.start(argv[1], argv[2], std::stoi(argv[3]));

    return upscaler.start(argv[1], argv[2], std::stoi(argv[3]), std::stoi(argv[4]));
}
