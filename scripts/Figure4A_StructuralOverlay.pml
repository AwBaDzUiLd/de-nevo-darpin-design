load darpin_af3_seed5.pdb,af3_model
load darpin_boltz1.pdb,boltz_model
align boltz_model and chain A, af3_model and chain A
bg_color white
hide surface
show cartoon
set cartoon_fancy_helices,1
color lightgrey,af3_model and chain A
color grey30,boltz_model and chain A
color deepblue,af3_model and chain B
color salmon,boltz_model and chain B
zoom chain B
ray 2400,2400
png Figure4A_Structural_Overlay.png,dpi=300
