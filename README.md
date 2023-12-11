# foldseek-bindings

Simple interface to use `easy-search` from [foldseek](https://github.com/steineggerlab/foldseek). 

The ideal implementation uses pybind and compiles their c++, but I'm too lazy and just called it via exec and read stdout. 

In other words, there is much room for improvement here.

## Running

First install the foldseek executable and make sure it's in your path as `foldseek`. 