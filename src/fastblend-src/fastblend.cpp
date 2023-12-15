#include <iostream>

#include "fastblend.hpp"

using namespace cv;


Fastblend::Fastblend () : Upscaler()
{

}
Fastblend::~Fastblend ()
{

}


Mat* Fastblend::upscalePicture(Mat* picture, const size_t, const int8_t)
{
    const Size picture_size(picture->size());
    const Size output_picture_size(picture_size.width * 2 - 1, picture_size.height * 2 - 1);

    Mat* output_picture(new Mat(output_picture_size, CV_32FC3));


    for (size_t row(0) ; row < picture_size.height ; row++)
    {
        for (size_t col(0) ; col < picture_size.width ; col++)
        {
            output_picture->at<Vec3f>(Point(col * 2, row * 2)) = picture->at<Vec3f>(Point(col, row));
        }
    }


    for (size_t row(1) ; row < output_picture_size.height - 1 ; row += 2)
    {
        for (size_t col(1) ; col < output_picture_size.width - 1 ; col += 2)
        {
            const auto a(output_picture->at<Vec3f>(Point(col - 1, row - 1)));
            const auto b(output_picture->at<Vec3f>(Point(col + 1, row - 1)));
            const auto c(output_picture->at<Vec3f>(Point(col - 1, row + 1)));
            const auto d(output_picture->at<Vec3f>(Point(col + 1, row + 1)));


            output_picture->at<Vec3f>(Point(col, row)) = (a + b + c + d) / 4.0;
        
            output_picture->at<Vec3f>(Point(col, row - 1)) = (a + b) / 2.0;
            output_picture->at<Vec3f>(Point(col + 1, row)) = (b + d) / 2.0;
        }
    }

    for (size_t row(1) ; row < output_picture_size.height - 1 ; row += 2)
        output_picture->at<Vec3f>(Point(0, row)) = (output_picture->at<Vec3f>(Point(0, row - 1)) + output_picture->at<Vec3f>(Point(0, row + 1))) / 2.0;

    size_t last_pixel_height(output_picture_size.height - 1);
    for (size_t col(1) ; col < output_picture_size.width - 1 ; col += 2)
        output_picture->at<Vec3f>(Point(col, last_pixel_height)) = (output_picture->at<Vec3f>(Point(col - 1, last_pixel_height)) + output_picture->at<Vec3f>(Point(col + 1, last_pixel_height))) / 2.0;


    return output_picture;
}


int main (int argc, char** argv)
{
    Fastblend upscaler;

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
