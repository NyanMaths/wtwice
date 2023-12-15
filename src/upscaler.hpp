#ifndef UPSCALER_HPP
#define UPSCALER_HPP

#include <cinttypes>
#include <opencv4/opencv2/opencv.hpp>


class Upscaler
{
    public:
        explicit Upscaler();
        virtual ~Upscaler() = 0;

        virtual int start(const std::string input_picture_path, const std::string output_picture_path, const size_t ratio=2u, const int8_t denoising=0);


    protected:
        virtual cv::Mat* upscalePicture(cv::Mat* image, size_t ratio, int8_t denoising) = 0;


    private:
        cv::Mat* getPicture(const std::string picture_path);
};


#endif  // UPSCALER_HPP
