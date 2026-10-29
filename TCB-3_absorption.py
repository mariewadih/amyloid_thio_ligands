import veloxchem as vlx

molecule = vlx.Molecule.read_xyz_file("TCB_conf1_opt.xyz")

molecule.set_charge(0)
molecule.set_multiplicity(1)

basis = vlx.MolecularBasis.read(molecule, "def2-svp")

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = "cam-b3lyp"
scf_drv.filename = "TCB_conf1_opt-td"
#scf_drv.solvation_model = "cpcm"
scf_drv.dispersion = True 
scf_results = scf_drv.compute(molecule, basis)

rsp_drv = vlx.LinearResponseEigenSolver()
rsp_drv.filename = "TCB_conf1_opt-td"
rsp_drv.nstates = 10
rsp_drv.nto = True
rsp_results = rsp_drv.compute(molecule, basis, scf_results)
