load darpin_af3_seed5.pdb
bg_color white
show cartoon
hide surface
hide sticks,all
color lightgrey,chain A
color cyan,chain B
select receptor_hbonds, chain A and resi 82+83+108+154+156+157+160
select darpin_hbonds, chain B and resi 12+13+35+37+42+46+66+67+68+76+127+128
show sticks,receptor_hbonds
show sticks,darpin_hbonds
color orange,darpin_hbonds and not name C+N+O
distance hbonds_pisa,receptor_hbonds,darpin_hbonds,mode=2,cutoff=4.0
color yellow,hbonds_pisa
set dash_width,3.5
set dash_gap,0.15
set dash_radius,0.07
label (name CA and (receptor_hbonds or darpin_hbonds)), "%s%s" % (resn, resi)
set label_color,black
set label_size,16
set label_font_id,7
zoom receptor_hbonds or darpin_hbonds,buffer=2.0
ray 3000,2400
png Figure2_PISA_Hydrogen_Bonds.png,dpi=300
