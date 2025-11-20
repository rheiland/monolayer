#include <iostream>
#include <random>
#include <iomanip> // For std::fixed and std::setprecision

int main() {
    // 1. Initialize a random number engine
    // std::random_device provides a non-deterministic seed if available
    std::random_device rd{}; 
    // std::mt19937 is a popular Mersenne Twister pseudo-random number generator
    std::mt19937 generator{rd()}; 

    // 2. Define the normal distribution parameters: Mean (mu) and Standard Deviation (sigma)
    const double mean = 2.0;
    const double stddev = 0.4;
    std::normal_distribution<double> distribution(mean, stddev);

    // 3. Generate and print some random numbers
    std::cout << std::fixed << std::setprecision(4);
    std::cout << "Generating 10 samples from N(" << mean << ", " << stddev << "^2):" << std::endl;
    for (int i = 0; i < 10; ++i) {
        double number = distribution(generator);
        std::cout << "Sample " << i + 1 << ": " << number << std::endl;
    }

    return 0;
}
