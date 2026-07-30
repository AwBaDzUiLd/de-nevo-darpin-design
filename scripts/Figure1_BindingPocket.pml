load darpin_af3_seed5.pdb
select receptor, chain A
select darpin, chain B
bg_color white
show cartoon
set cartoon_fancy_helices,1
set ray_trace_mode,1
color grey70,receptor
color deepblue,darpin
show surface,receptor
set surface_quality,1
set transparency,0.40,receptor
select interface_res, darpin within 5 of receptor
show sticks,interface_res
color orange,interface_res
zoom interface_res
ray 2400,2400
png Figure1_BindingPocket.png,dpi=300
