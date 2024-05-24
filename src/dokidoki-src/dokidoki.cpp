/*
This algorithm takes the average of two pixels to put between them in order to get a smoother result
Not incredible, but still better than nearest for larger images.
Now worky, faster than fastblend(...), but much more blurry result.
I merely adapted his code to C++ because Python would have taken half a year to run it.
I fear no man, but that THING... It scares me. No idea how this works, ask him.
Author : Turbo Giga Chad
*/

#include <iostream> 

#include "dokidoki.hpp"

using namespace cv;


Dokidoki::Dokidoki () : Upscaler()
{

}
Dokidoki::~Dokidoki ()
{

}


Image* Dokidoki::upscalePicture(Image* picture, const size_t, const int8_t)
{
    const Size picture_size(picture->size());
    const Size output_size(picture_size.width * 2, picture_size.height * 2);
    const size_t n(picture_size.height);

    Image* output_picture(new Image(output_size, CV_32FC3));


    output_picture->pixel(0, 0) = picture->pixel(0, 0);
    output_picture->pixel(0, output_size.width - 1) = picture->pixel(0, picture_size.width - 1);
    output_picture->pixel(output_size.height - 1, 0) = picture->pixel(picture_size.height - 1, 0);
    output_picture->pixel(output_size.height - 1, output_size.width - 1) = picture->pixel(picture_size.height - 1, picture_size.width - 1);

    for (size_t j(0) ; j < n - 1 ; j++)
    {
        const Vec3f valr1(picture->pixel(0, j) + picture->pixel(0, j+1) / 2.0);
        const Vec3f valc1(picture->pixel(j, 0) + picture->pixel(j+1, 0) / 2.0);
        const Vec3f valr2(picture->pixel(n-1, j) + picture->pixel(n-1, j+1) / 2.0);
        const Vec3f valc2(picture->pixel(j, n-1) + picture->pixel(j+1, n-1) / 2.0);

        output_picture->pixel(0, 2*j + 1) = valr1;
        output_picture->pixel(0, 2*(j+1)) = valr1;

        output_picture->pixel(2*j + 1, 0) = valc1;
        output_picture->pixel(2*(j+1), 0) = valc1;

        output_picture->pixel(n-1, 2*j + 1) = valr2;
        output_picture->pixel(n-1, 2*(j+1)) = valr2;

        output_picture->pixel(2*j + 1, n-1) = valc2;
        output_picture->pixel(2*(j+1), n-1) = valc2;
    }

    for (size_t i(0) ; i < picture_size.height - 1 ; i++)
    {
        for (size_t j(0) ; j < picture_size.width - 1 ; j++)
        {
            const Vec3f val_bloc((picture->pixel(i, j) + picture->pixel(i+1, j) + picture->pixel(i, j+1) + picture->pixel(i+1, j+1)) / 4.0);
        
            output_picture->pixel(2*i + 1, 2*j + 1) = val_bloc;
            output_picture->pixel(2*i + 1, 2*(j+1)) = val_bloc;
            output_picture->pixel(2*(i+1), 2*j + 1) = val_bloc;
            output_picture->pixel(2*(i+1), 2*(j+1)) = val_bloc;
        }
    }


    return output_picture;
}


int main (int argc, char** argv)
{
    Dokidoki upscaler;

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
