#ifndef BILINEAR_HPP
#define BILINEAR_HPP

#include <cinttypes>

#include "../upscaler.hpp"
 

class Bilinear : public Upscaler
{
    public:
        explicit Bilinear();
        virtual ~Bilinear() override;

    private:
        virtual cv::Mat* upscalePicture(cv::Mat* picture, const size_t ratio=2u, const int8_t denoising=0) override;
};


#endif  // BILINEAR_HPP
