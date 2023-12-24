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
        virtual Image* upscalePicture(Image* picture, const size_t ratio=2u, const int8_t denoising=0) override;
};


#endif  // FASTBLEND_HPP
