import veloxchem as vlx

molecule = vlx.Molecule.read_xyz_file("TCB_conf1.xyz")
basis = vlx.MolecularBasis.read(molecule, "def2-svp")

molecule.set_charge(0)
molecule.set_multiplicity(1)

basis = vlx.MolecularBasis.read(molecule, "def2-svp")

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = "b3lyp"
scf_drv.filename = "TCB_conf1_opt"
#scf_drv.solvation_model = "cpcm"
scf_drv.dispersion = True 
scf_results = scf_drv.compute(molecule, basis)

opt_drv = vlx.OptimizationDriver(scf_drv)
opt_results = opt_drv.compute(molecule, basis, scf_results)
