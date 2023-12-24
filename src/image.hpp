#ifndef IMAGE_HPP
#define IMAGE_HPP

#include <cinttypes>
#include <opencv4/opencv2/opencv.hpp>


class Image : public cv::Mat
{
    public:
        explicit Image();
        explicit Image(cv::Mat picture_matrix);
        explicit Image(cv::Size picture_size, int depth);
        virtual ~Image();

        cv::Vec3f& pixel(const size_t row, const size_t column);
};


#endif  // IMAGE_HPP
