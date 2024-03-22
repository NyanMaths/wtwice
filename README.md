Wtwice is aimed at upscaling videos frame by frame, that is, without temporal coherence.
This is not ready yet, still, we implemented some decent algorithms to upscale single pictures and added an easy way to compare upscalers.
We are reimplementing even basic algorithms because this is a school project.

Note about the SRCNN : it is trained using <a href="https://www.kaggle.com/datasets/aditmagotra/gameplay-images">a gaming screenshots dataset</a> from Kaggle.

Available algorithms :
 - nearest
 - dokidoki
 - fasblend (bilinear is far better)
 - bilinear
 - wthrice (a simple SRCNN)

Already done :
 - an easy to use image upscaler
 - an acceptable codebase
 - removed those terrible eval() calls

To do :
 - video upscaler
 - bicubic implementation
 - documentation ?
