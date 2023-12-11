# foldseek-bindings

Simple interface to use `easy-search` from [foldseek](https://github.com/steineggerlab/foldseek) from the great people below

> van Kempen, M., Kim, S.S., Tumescheit, C., Mirdita, M., Lee, J., Gilchrist, C.L.M., Söding, J., and Steinegger, M. Fast and accurate protein structure search with Foldseek. Nature Biotechnology, doi:10.1038/s41587-023-01773-0 (2023)

all credit for foldseek goes to them, this is just a python interface. 

The ideal implementation uses pybind and compiles their c++, but I'm too lazy and just called it via exec and read stdout. 

In other words, there is much room for improvement here.

## Running

First install the foldseek executable and make sure it's in your path as `foldseek`. 


For example, I can query my A.pdb with the the protein data bank proteins and find similar proteins like

```py
from foldseek import easy_search

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
 ['A.pdb', '7qcu.cif.gz_B', 1.0],
 ['A.pdb', '7wn3.cif.gz_F', 1.0],
 ['A.pdb', '7wpq.cif.gz_C', 1.0],
 ['A.pdb', '6s4c.cif.gz_A', 0.999],
 ['A.pdb', '7egb.cif.gz_2', 0.984],
 ['A.pdb', '7ml1.cif.gz_6', 0.981],
 ['A.pdb', '4d50.cif.gz_A', 0.967],
 ['A.pdb', '8t1o.cif.gz_A', 0.967],
 ['A.pdb', '5aff.cif.gz_A', 0.941],
 ['A.pdb', '4hqo.cif.gz_A', 0.933],
 ['A.pdb', '7z8r.cif.gz_D', 0.933],
 ['A.pdb', '5iy6.cif.gz_3', 0.912],
 ['A.pdb', '5h2w.cif.gz_C', 0.912],
 ['A.pdb', '3ea5.cif.gz_D', 0.912],
 ['A.pdb', '4evt.cif.gz_A', 0.855],
 ['A.pdb', '4djs.cif.gz_A', 0.855],
 ['A.pdb', '8sw0.cif.gz_A', 0.855],
 ['A.pdb', '7abi.cif.gz_u', 0.855],
 ['A.pdb', '5iz9.cif.gz_A', 0.837],
 ['A.pdb', '2yns.cif.gz_A', 0.837],
 ['A.pdb', '7nwl.cif.gz_B', 0.837],
 ['A.pdb', '6y50.cif.gz_u', 0.837],
 ['A.pdb', '3nmx.cif.gz_B', 0.795],
 ['A.pdb', '3zdz.cif.gz_B', 0.795],
 ['A.pdb', '7sqc.cif.gz_P2', 0.795],
 ['A.pdb', '4kzg.cif.gz_D', 0.772],
 ['A.pdb', '3nmx.cif.gz_C', 0.747],
 ['A.pdb', '4wz9.cif.gz_A', 0.747],
 ['A.pdb', '6tc0.cif.gz_F', 0.747],
 ['A.pdb', '4wz9.cif.gz_B', 0.72],
 ['A.pdb', '7n8j.cif.gz_A', 0.692],
 ['A.pdb', '8t2u.cif.gz_B', 0.663],
 ['A.pdb', '6tyl.cif.gz_F', 0.663],
 ['A.pdb', '2qna.cif.gz_A', 0.663],
 ['A.pdb', '6p6e.cif.gz_A', 0.632],
 ['A.pdb', '4wk4.cif.gz_B', 0.601],
 ['A.pdb', '6tc0.cif.gz_C', 0.601],
 ['A.pdb', '6nmg.cif.gz_A', 0.569],
 ['A.pdb', '8fl4.cif.gz_NT', 0.569],
 ['A.pdb', '4c0p.cif.gz_C', 0.569],
 ['A.pdb', '5me3.cif.gz_B', 0.569],
 ['A.pdb', '5z56.cif.gz_1', 0.569],
 ['A.pdb', '4wk0.cif.gz_B', 0.537],
 ['A.pdb', '7jtn.cif.gz_C', 0.537],
 ['A.pdb', '5f0o.cif.gz_A', 0.537],
 ['A.pdb', '3tjz.cif.gz_E', 0.505],
 ['A.pdb', '4kzg.cif.gz_G', 0.505],
 ['A.pdb', '3fey.cif.gz_C', 0.505],
 ['A.pdb', '4a3t.cif.gz_A', 0.505],
 ['A.pdb', '8eic.cif.gz_A', 0.473],
 ['A.pdb', '2h4m.cif.gz_B', 0.473],
 ['A.pdb', '3w5k.cif.gz_A', 0.473],
 ['A.pdb', '7z87.cif.gz_A', 0.473],
 ['A.pdb', '4wk2.cif.gz_B', 0.442],
 ['A.pdb', '8eok.cif.gz_D', 0.442],
 ['A.pdb', '4ok2.cif.gz_B', 0.442],
 ['A.pdb', '4nei.cif.gz_B', 0.411],
 ['A.pdb', '2bku.cif.gz_D', 0.411],
 ['A.pdb', '3zjy.cif.gz_B', 0.411],
 ['A.pdb', '6q84.cif.gz_D', 0.411],
 ['A.pdb', '3woz.cif.gz_D', 0.382],
 ['A.pdb', '3vi3.cif.gz_B', 0.382],
 ['A.pdb', '1ibr.cif.gz_D', 0.382],
 ['A.pdb', '2xwu.cif.gz_B', 0.382],
 ['A.pdb', '8eib.cif.gz_A', 0.353],
 ['A.pdb', '6oiu.cif.gz_B', 0.353],
 ['A.pdb', '7tyr.cif.gz_A', 0.353],
 ['A.pdb', '7jtq.cif.gz_A', 0.326],
 ['A.pdb', '5yo1.cif.gz_A', 0.301],
 ['A.pdb', '1gcj.cif.gz_B', 0.277],
 ['A.pdb', '7bm6.cif.gz_B', 0.277],
 ['A.pdb', '7t3r.cif.gz_D', 0.277],
 ['A.pdb', '4nz8.cif.gz_A', 0.254],
 ['A.pdb', '4xn4.cif.gz_A', 0.233],
 ['A.pdb', '3ibv.cif.gz_B', 0.233],
 ['A.pdb', '7w3a.cif.gz_f', 0.214],
 ['A.pdb', '7bjt.cif.gz_B', 0.196],
 ['A.pdb', '6vac.cif.gz_A', 0.196],
 ['A.pdb', '8bsh.cif.gz_C', 0.196],
 ['A.pdb', '7w7g.cif.gz_B', 0.196],
 ['A.pdb', '6u7f.cif.gz_B', 0.179],
 ['A.pdb', '6u7e.cif.gz_A', 0.179],
 ['A.pdb', '4naq.cif.gz_A', 0.179],
 ['A.pdb', '5wbl.cif.gz_A', 0.179],
 ['A.pdb', '6u62.cif.gz_A', 0.179],
 ['A.pdb', '3tj1.cif.gz_A', 0.164],
 ['A.pdb', '6zga.cif.gz_F', 0.164],
 ['A.pdb', '3zjy.cif.gz_G', 0.164],
 ['A.pdb', '8bt6.cif.gz_A', 0.164],
 ['A.pdb', '5frs.cif.gz_A', 0.15],
 ['A.pdb', '6atk.cif.gz_C', 0.15],
 ['A.pdb', '6tnf.cif.gz_A', 0.15],
 ['A.pdb', '5t87.cif.gz_B', 0.138],
 ['A.pdb', '4r7s.cif.gz_A', 0.138],
 ['A.pdb', '8e2h.cif.gz_A', 0.138],
 ['A.pdb', '7vpq.cif.gz_E', 0.138],
 ['A.pdb', '3q64.cif.gz_A', 0.126],
 ['A.pdb', '4i17.cif.gz_A', 0.126],
 ['A.pdb', '4abn.cif.gz_A', 0.126],
 ['A.pdb', '4ok4.cif.gz_B', 0.126],
 ['A.pdb', '3tj1.cif.gz_B', 0.116],
 ['A.pdb', '6ie1.cif.gz_A', 0.116],
 ['A.pdb', '4neh.cif.gz_B', 0.116],
 ['A.pdb', '8dth.cif.gz_B', 0.116],
 ['A.pdb', '7vpq.cif.gz_C', 0.116],
 ['A.pdb', '6s39.cif.gz_A', 0.106],
 ['A.pdb', '1ouv.cif.gz_A', 0.106],
 ['A.pdb', '5wbi.cif.gz_A', 0.106],
 ['A.pdb', '7mwc.cif.gz_A', 0.098],
 ['A.pdb', '1w3b.cif.gz_B', 0.09],
 ['A.pdb', '5fq6.cif.gz_B', 0.09],
 ['A.pdb', '5uwr.cif.gz_C', 0.09],
 ['A.pdb', '6u1s.cif.gz_A', 0.082],
 ['A.pdb', '6vnw.cif.gz_E', 0.082],
 ['A.pdb', '4abn.cif.gz_B', 0.082],
 ['A.pdb', '8c6j.cif.gz_H', 0.082],
 ['A.pdb', '7vpp.cif.gz_A', 0.082],
 ['A.pdb', '7d63.cif.gz_AE', 0.082],
 ['A.pdb', '6ntr.cif.gz_D', 0.076],
 ['A.pdb', '3efm.cif.gz_A', 0.076],
 ['A.pdb', '5fq8.cif.gz_D', 0.076],
 ['A.pdb', '5uwu.cif.gz_C', 0.076],
 ['A.pdb', '8tkd.cif.gz_A', 0.076],
 ['A.pdb', '7dtr.cif.gz_A', 0.069],
 ['A.pdb', '6ke6.cif.gz_AE', 0.069],
 ['A.pdb', '4f5c.cif.gz_B', 0.069],
 ['A.pdb', '6k9k.cif.gz_A', 0.069],
 ['A.pdb', '5qsu.cif.gz_A', 0.063],
 ['A.pdb', '2lbp.cif.gz_A', 0.063],
 ['A.pdb', '6fcq.cif.gz_A', 0.063],
 ['A.pdb', '4zle.cif.gz_A', 0.063],
 ['A.pdb', '3v89.cif.gz_A', 0.063],
 ['A.pdb', '5lds.cif.gz_B', 0.063],
 ['A.pdb', '6smq.cif.gz_E', 0.063],
 ['A.pdb', '1ywt.cif.gz_B', 0.057],
 ['A.pdb', '7nxw.cif.gz_A', 0.057],
 ['A.pdb', '4n9f.cif.gz_x', 0.057],
 ['A.pdb', '5lmg.cif.gz_A', 0.057],
 ['A.pdb', '7d5s.cif.gz_AE', 0.057],
 ['A.pdb', '8aa4.cif.gz_B', 0.057],
 ['A.pdb', '7dkh.cif.gz_E', 0.057],
 ['A.pdb', '7v7b.cif.gz_A', 0.057],
 ['A.pdb', '2m07.cif.gz_MODEL_1_A', 0.051],
 ['A.pdb', '6c9m.cif.gz_A', 0.051],
 ['A.pdb', '4f5c.cif.gz_A', 0.051],
 ['A.pdb', '6smq.cif.gz_B', 0.051],
 ['A.pdb', '5fq7.cif.gz_D', 0.051],
 ['A.pdb', '5b26.cif.gz_C', 0.045],
 ['A.pdb', '5o67.cif.gz_A', 0.045],
 ['A.pdb', '4grs.cif.gz_B', 0.045],
 ['A.pdb', '5hi8.cif.gz_B', 0.04],
 ['A.pdb', '8bnz.cif.gz_P', 0.04],
 ['A.pdb', '7qbg.cif.gz_C', 0.04],
 ['A.pdb', '5odw.cif.gz_B', 0.04],
 ['A.pdb', '2iah.cif.gz_A', 0.04],
 ['A.pdb', '3v8x.cif.gz_A', 0.04],
 ['A.pdb', '7qh3.cif.gz_B', 0.034],
 ['A.pdb', '2vdf.cif.gz_A', 0.034],
 ['A.pdb', '5om0.cif.gz_B', 0.034],
 ['A.pdb', '6ntr.cif.gz_B', 0.034],
 ['A.pdb', '7vcf.cif.gz_I', 0.034],
 ['A.pdb', '7shl.cif.gz_A', 0.034],
 ['A.pdb', '5t3r.cif.gz_D', 0.034],
 ['A.pdb', '6sli.cif.gz_J', 0.034],
 ['A.pdb', '7kzv.cif.gz_V', 0.034],
 ['A.pdb', '8ass.cif.gz_A', 0.029],
 ['A.pdb', '5ulo.cif.gz_B', 0.029],
 ['A.pdb', '5f2g.cif.gz_A', 0.029],
 ['A.pdb', '7wot.cif.gz_P', 0.029],
 ['A.pdb', '4rlc.cif.gz_A', 0.024],
 ['A.pdb', '1wub.cif.gz_A', 0.024],
 ['A.pdb', '6in9.cif.gz_A', 0.024],
 ['A.pdb', '1uyn.cif.gz_X', 0.024],
 ['A.pdb', '7vd2.cif.gz_B', 0.024],
 ['A.pdb', '2w77.cif.gz_B', 0.024],
 ['A.pdb', '5xqo.cif.gz_A', 0.024],
 ['A.pdb', '6tni.cif.gz_A', 0.024],
 ['A.pdb', '1p4t.cif.gz_A', 0.02],
 ['A.pdb', '6e5f.cif.gz_A', 0.02],
 ['A.pdb', '2x9k.cif.gz_A', 0.02],
 ['A.pdb', '3prn.cif.gz_A', 0.02],
 ['A.pdb', '5o65.cif.gz_B', 0.02],
 ['A.pdb', '3ohn.cif.gz_A', 0.02],
 ['A.pdb', '6h04.cif.gz_F', 0.02],
 ['A.pdb', '4epa.cif.gz_A', 0.02],
 ['A.pdb', '7mvw.cif.gz_A', 0.02],
 ['A.pdb', '2k0l.cif.gz_MODEL_11_A', 0.016],
 ['A.pdb', '5o68.cif.gz_I', 0.016],
 ['A.pdb', '5o68.cif.gz_D', 0.016],
 ['A.pdb', '4ozw.cif.gz_A', 0.016],
 ['A.pdb', '7xzj.cif.gz_9', 0.016],
 ['A.pdb', '6wil.cif.gz_A', 0.016],
 ['A.pdb', '2w78.cif.gz_A', 0.016],
 ['A.pdb', '1ug9.cif.gz_A', 0.016],
 ['A.pdb', '4ctd.cif.gz_B', 0.014],
 ['A.pdb', '4ctd.cif.gz_A', 0.014],
 ['A.pdb', '4bum.cif.gz_X', 0.014],
 ['A.pdb', '2prn.cif.gz_A', 0.014],
 ['A.pdb', '4n74.cif.gz_A', 0.014],
 ['A.pdb', '6z37.cif.gz_A', 0.014],
 ['A.pdb', '1t16.cif.gz_A', 0.014],
 ['A.pdb', '5z2c.cif.gz_D', 0.014],
 ['A.pdb', '8b0g.cif.gz_D', 0.014],
 ['A.pdb', '5fok.cif.gz_B', 0.014],
 ['A.pdb', '3s4b.cif.gz_A', 0.014],
 ['A.pdb', '3s4d.cif.gz_A', 0.014],
 ['A.pdb', '7bi2.cif.gz_A', 0.014],
 ['A.pdb', '4rl9.cif.gz_A', 0.011],
 ['A.pdb', '2zxk.cif.gz_A', 0.011],
 ['A.pdb', '6in9.cif.gz_B', 0.011],
 ['A.pdb', '3bry.cif.gz_B', 0.011],
 ['A.pdb', '3dwn.cif.gz_B', 0.011],
 ['A.pdb', '2vqi.cif.gz_B', 0.011],
 ['A.pdb', '2guf.cif.gz_A', 0.011],
 ['A.pdb', '7q3e.cif.gz_A', 0.011],
 ['A.pdb', '1xkh.cif.gz_C', 0.011],
 ['A.pdb', '6bpo.cif.gz_B', 0.011],
 ['A.pdb', '8h1r.cif.gz_D', 0.011],
 ['A.pdb', '5xq3.cif.gz_A', 0.011],
 ['A.pdb', '7tcv.cif.gz_XXX', 0.01],
 ['A.pdb', '2x4m.cif.gz_B', 0.01],
 ['A.pdb', '1bh3.cif.gz_A', 0.01],
 ['A.pdb', '4mee.cif.gz_A', 0.01],
 ['A.pdb', '3dwo.cif.gz_X', 0.01],
 ['A.pdb', '3ohn.cif.gz_B', 0.01],
 ['A.pdb', '8bmx.cif.gz_B', 0.01],
 ['A.pdb', '5fr8.cif.gz_B', 0.01],
 ['A.pdb', '6m5a.cif.gz_A', 0.01],
 ['A.pdb', '8a9y.cif.gz_I', 0.01],
 ['A.pdb', '3vd3.cif.gz_D', 0.01],
 ['A.pdb', '4fqe.cif.gz_A', 0.009],
 ['A.pdb', '2f1t.cif.gz_C', 0.009],
 ['A.pdb', '1qd5.cif.gz_A', 0.009],
 ['A.pdb', '3aga.cif.gz_A', 0.009],
 ['A.pdb', '4dcb.cif.gz_A', 0.009],
 ['A.pdb', '1prn.cif.gz_A', 0.009],
 ['A.pdb', '5prn.cif.gz_A', 0.009],
 ['A.pdb', '6prn.cif.gz_A', 0.009],
 ['A.pdb', '7prn.cif.gz_A', 0.009],
 ['A.pdb', '5o67.cif.gz_B', 0.009],
 ['A.pdb', '7vcf.cif.gz_F', 0.009],
 ['A.pdb', '3pf1.cif.gz_A', 0.009],
 ['A.pdb', '7s6h.cif.gz_D', 0.009],
 ['A.pdb', '5fp2.cif.gz_A', 0.009],
 ['A.pdb', '5iva.cif.gz_A', 0.009],
 ['A.pdb', '8p97.cif.gz_A', 0.009],
 ['A.pdb', '8bmx.cif.gz_A', 0.009],
 ['A.pdb', '6v81.cif.gz_A', 0.009],
 ['A.pdb', '5fok.cif.gz_A', 0.009],
 ['A.pdb', '6hcp.cif.gz_C', 0.009],
 ['A.pdb', '8a60.cif.gz_A', 0.009],
 ['A.pdb', '6r1f.cif.gz_A', 0.009],
 ['A.pdb', '3act.cif.gz_B', 0.009],
 ['A.pdb', '3qfz.cif.gz_B', 0.009],
 ['A.pdb', '8aa0.cif.gz_A', 0.009],
 ['A.pdb', '7x7z.cif.gz_B', 0.008],
 ['A.pdb', '2f1v.cif.gz_A', 0.008],
 ['A.pdb', '1fw3.cif.gz_B', 0.008],
 ['A.pdb', '1k24.cif.gz_A', 0.008],
 ['A.pdb', '7xw0.cif.gz_B', 0.008],
 ['A.pdb', '4yhd.cif.gz_C', 0.008],
 ['A.pdb', '5o67.cif.gz_C', 0.008],
 ['A.pdb', '7t82.cif.gz_B', 0.008],
 ['A.pdb', '8bo2.cif.gz_P', 0.008],
 ['A.pdb', '7xzi.cif.gz_9', 0.008],
 ['A.pdb', '7s6h.cif.gz_B', 0.008],
 ['A.pdb', '4v2t.cif.gz_A', 0.008],
 ['A.pdb', '4c00.cif.gz_A', 0.008],
 ['A.pdb', '1nqf.cif.gz_A', 0.008],
 ['A.pdb', '1nqg.cif.gz_A', 0.008],
 ['A.pdb', '8bmx.cif.gz_C', 0.008],
 ['A.pdb', '7qun.cif.gz_B', 0.008],
 ['A.pdb', '7omm.cif.gz_A', 0.008],
 ['A.pdb', '3acs.cif.gz_B', 0.008],
 ['A.pdb', '6se9.cif.gz_A', 0.008],
 ['A.pdb', '6ji8.cif.gz_A', 0.008],
 ['A.pdb', '1qd6.cif.gz_D', 0.007],
 ['A.pdb', '7ezz.cif.gz_A', 0.007],
 ['A.pdb', '7ezz.cif.gz_B', 0.007],
 ['A.pdb', '7xw0.cif.gz_A', 0.007],
 ['A.pdb', '5o68.cif.gz_H', 0.007],
 ['A.pdb', '5o68.cif.gz_E', 0.007],
 ['A.pdb', '4idj.cif.gz_A', 0.007],
 ['A.pdb', '5o65.cif.gz_A', 0.007],
 ['A.pdb', '4tw1.cif.gz_A', 0.007],
 ['A.pdb', '6b7l.cif.gz_A', 0.007],
 ['A.pdb', '4frt.cif.gz_B', 0.007],
 ['A.pdb', '6z38.cif.gz_A', 0.007],
 ['A.pdb', '5nec.cif.gz_A', 0.007],
 ['A.pdb', '4aip.cif.gz_B', 0.007],
 ['A.pdb', '3afj.cif.gz_A', 0.007],
 ['A.pdb', '7uft.cif.gz_A', 0.007],
 ['A.pdb', '4eis.cif.gz_B', 0.0],
 ['A.pdb', '1im0.cif.gz_A', 0.0],
 ['A.pdb', '4yhd.cif.gz_A', 0.0],
 ['A.pdb', '8prn.cif.gz_A', 0.0],
 ['A.pdb', '3njt.cif.gz_A', 0.0],
 ['A.pdb', '8a1d.cif.gz_D', 0.0],
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