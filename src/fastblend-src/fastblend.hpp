#ifndef FASTBLEND_HPP
#define FASTBLEND_HPP

#include <cinttypes>

#include "../upscaler.hpp"


class Fastblend : public Upscaler
{
    public:
        explicit Fastblend();
        virtual ~Fastblend() override;

    private:
        virtual cv::Mat* upscalePicture(cv::Mat* picture, const size_t ratio=2u, const int8_t denoising=0) override;
};


#endif  // FASTBLEND_HPP
