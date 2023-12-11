# foldseek-bindings

Simple interface to use `easy-search` from [foldseek](https://github.com/steineggerlab/foldseek) from the great people below

> van Kempen, M., Kim, S.S., Tumescheit, C., Mirdita, M., Lee, J., Gilchrist, C.L.M., Söding, J., and Steinegger, M. Fast and accurate protein structure search with Foldseek. Nature Biotechnology, doi:10.1038/s41587-023-01773-0 (2023)

all credit for foldseek goes to them, this is just a python interface. 

The ideal implementation uses pybind and compiles their c++, but I'm too lazy and just called it via exec and read stdout. 

In other words, there is much room for improvement here.

## Running

First install the foldseek executable and make sure it's in your path as `foldseek`. 

For a concrete example check out the [`example.ipynb`](./example.ipynb).

Or just look here: I can query my A.pdb with the the protein data bank proteins and find similar proteins like

```py
from foldseek import easy_search, create_db

db = create_db(dir="PDB", db_name="pdb")
output = easy_search(
	query="test_examples/A.pdb",
	target=db,
	out_format=["query", "target", "prob"],
)
```

where output now is the following array formatted as you specified [query, target, output] for each hit/similar protein:

```py
[['A.pdb', '1lsh.cif.gz_A', 1.0],
 ['A.pdb', '6i7s.cif.gz_G', 1.0],
 ['A.pdb', '6i7s.cif.gz_H', 1.0],
 ['A.pdb', '8eoj.cif.gz_B', 1.0],
 ['A.pdb', '7a5o.cif.gz_B', 1.0],
 ['A.pdb', '7a5o.cif.gz_G', 1.0],
 ['A.pdb', '8d3c.cif.gz_A', 1.0],
 ['A.pdb', '7a5o.cif.gz_A', 1.0],
 ['A.pdb', '7zwh.cif.gz_E', 1.0],
 ['A.pdb', '7pp6.cif.gz_D', 1.0],
 ['A.pdb', '7pov.cif.gz_A', 1.0],
 ['A.pdb', '7wn3.cif.gz_A', 1.0],
 ['A.pdb', '7pmv.cif.gz_E', 1.0],
 ['A.pdb', '6rbf.cif.gz_D', 1.0],
 ['A.pdb', '7pov.cif.gz_C', 1.0],
 ['A.pdb', '6rbf.cif.gz_C', 1.0],
 ['A.pdb', '6rbf.cif.gz_B', 1.0],
 ['A.pdb', '6tm2.cif.gz_C', 1.0],
 ['A.pdb', '7a5o.cif.gz_D', 1.0],
 ['A.pdb', '7prl.cif.gz_A', 1.0],
 ['A.pdb', '6rbf.cif.gz_A', 1.0],
 ['A.pdb', '6n29.cif.gz_B', 1.0],
 ['A.pdb', '8d3d.cif.gz_A', 1.0],
 			...
 ['A.pdb', '1nqh.cif.gz_A', 0.0],
 ['A.pdb', '5nec.cif.gz_B', 0.0],
 ['A.pdb', '4b7o.cif.gz_A', 0.0],
 ['A.pdb', '6zjq.cif.gz_A', 0.0],
 ['A.pdb', '2x56.cif.gz_A', 0.0],
 ['A.pdb', '4izl.cif.gz_D', 0.0],
 ['A.pdb', '8p98.cif.gz_A', 0.0],
 ['A.pdb', '1fep.cif.gz_A', 0.0],
 ['A.pdb', '2grx.cif.gz_A', 0.0],
 ['A.pdb', '8b0g.cif.gz_B', 0.0],
 ['A.pdb', '7lhh.cif.gz_C', 0.0],
 ['A.pdb', '8acq.cif.gz_A', 0.0],
 ['A.pdb', '4izl.cif.gz_B', 0.0],
 ['A.pdb', '8agd.cif.gz_A', 0.0],
 ['A.pdb', '4e1t.cif.gz_A', 0.0],
 ['A.pdb', '4tw1.cif.gz_C', 0.0]]
```