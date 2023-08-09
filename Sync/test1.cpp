#include <iostream>
#include <opencv2/opencv.hpp>

bool hasSingleColor(const cv::Mat& image) {
    cv::Mat flatImage = image.reshape(1, image.total());
    cv::Mat uniqueColors;
    cv::reduce(flatImage, uniqueColors, 0, cv::REDUCE_UNIQUE);

    return uniqueColors.rows <= 1;
}