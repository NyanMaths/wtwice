#include <iostream>

#include "nearest.hpp"

using namespace cv;


Nearest::Nearest () : Upscaler()
{

}
Nearest::~Nearest ()
{

}


Mat* Nearest::upscalePicture(Mat* picture, const size_t ratio, const int8_t denoising)
{
    const Size picture_size(picture->size());

    Mat* output_picture(new Mat(Size(picture_size.width * ratio, picture_size.height * ratio), CV_32FC3));


    for (size_t row(0) ; row < picture_size.height ; row++)
    {
        for (size_t col(0) ; col < picture_size.width ; col++)
        {
            const auto current_pixel(picture->at<Vec3f>(Point(col, row)));


            for (size_t i(0) ; i < ratio ; i++)
                for (size_t j(0) ; j < ratio ; j++)
                    output_picture->at<Vec3f>(Point(ratio * col + j, ratio * row + i)) = current_pixel;
        }
    }


    return output_picture;
}


int main (int argc, char** argv)
{
    Nearest upscaler;

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
