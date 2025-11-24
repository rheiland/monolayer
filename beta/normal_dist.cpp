//  g++-14 normal_dist.cpp -o normal_dist
#include <iostream>
#include <random>
#include <iomanip> // For std::fixed and std::setprecision

thread_local std::mt19937_64 physicell_PRNG_generator; 

double NormalRandom( double mean, double standard_deviation )
{
	std::normal_distribution<double> d(mean,standard_deviation);
	return d(physicell_PRNG_generator); 
}

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

    int max_draws = 2.e7;
    // 3. Generate and print some random numbers
    std::cout << std::fixed << std::setprecision(4);
    std::cout << "Generating "<< max_draws <<" draws from N(" << mean << ", " << stddev << "^2):" << std::endl;
    double draw;
    std::cout << "------- using distribution";
    for (int i = 0; i < max_draws; ++i) {
        draw = distribution(generator);
        if (draw < 0.0)
            std::cout << "Sample " << i + 1 << ": " << draw << std::endl;
    }

    std::cout << "------- using NormalRandom";
    for (int i = 0; i < max_draws; ++i) {
        // draw = NormalRandom(2.0, 0.25) * 523.6;
        draw = NormalRandom(2.0, 0.4);
        if (draw < 0.0)
            std::cout << "Sample " << i + 1 << ": " << draw << std::endl;
    }

    return 0;
}
