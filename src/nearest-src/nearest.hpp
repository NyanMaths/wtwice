#ifndef NEAREST_HPP
#define NEAREST_HPP

#include <cinttypes>

#include "../upscaler.hpp"


class Nearest : public Upscaler
{
    public:
        explicit Nearest();
        virtual ~Nearest() override;

    private:
        virtual Image* upscalePicture(Image* picture, const size_t ratio=2u, const int8_t denoising=0) override;
};


#endif  // NEAREST_HPP
