#ifndef DOKIDOKI_HPP
#define DOKIDOKI_HPP

#include <cinttypes> 

#include "../upscaler.hpp"


class Dokidoki : public Upscaler
{
    public:
        explicit Dokidoki();
        virtual ~Dokidoki() override;

    private:
        virtual Image* upscalePicture(Image* picture, const size_t ratio=2u, const int8_t denoising=0) override;
};


#endif  // DOKIDOKI_HPP
