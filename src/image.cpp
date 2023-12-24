#include "image.hpp"


Image::Image () : cv::Mat()
{

}
Image::Image (cv::Mat picture_matrix) : cv::Mat(picture_matrix)
{

}
Image::Image (cv::Size picture_size, int depth) : cv::Mat(picture_size, depth)
{

}


Image::~Image ()
{

}


cv::Vec3f& Image::pixel(const size_t row, const size_t column)
{
    return at<cv::Vec3f>(cv::Point(column, row));
}
