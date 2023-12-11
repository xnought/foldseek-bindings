# foldseek-bindings

Simple interface to use `easy-search` from [foldseek](https://github.com/steineggerlab/foldseek) from the great people below

> van Kempen, M., Kim, S.S., Tumescheit, C., Mirdita, M., Lee, J., Gilchrist, C.L.M., Söding, J., and Steinegger, M. Fast and accurate protein structure search with Foldseek. Nature Biotechnology, doi:10.1038/s41587-023-01773-0 (2023)

all credit for foldseek goes to them, this is just a python interface. 

The ideal implementation uses pybind and compiles their c++, but I'm too lazy and just called it via exec and read stdout. 

In other words, there is much room for improvement here.

## Running

First install the foldseek executable and make sure it's in your path as `foldseek`. 

