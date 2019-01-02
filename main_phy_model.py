import numpy as np
import pandas as pd
import xarray as xr
import brom_functions as bf
import plot_functions as pf
import linear_fit_functions as lff

ds = xr.open_dataset('wadden_sea_out.nc')
df = ds.to_dataframe()
levelcntr = df.groupby('levelcntr').get_group(0.625)
levelface = levelcntr.groupby('levelface').get_group(0)

par = levelface['par'].values.astype(np.float64)
temperature = levelface['temperature'].values.astype(np.float64)
nh4_data = levelface['ammonium'].values.astype(np.float64)
no3_data = levelface['nitrate'].values.astype(np.float64)
po4_data = levelface['phosphate'].values.astype(np.float64)
si_data = levelface['silicate'].values.astype(np.float64)
o2_data = levelface['oxygen'].values.astype(np.float64)
chl_a_data = levelface['chl_a'].values.astype(np.float64)

#initial data
#some common variables
depth = 0.625; k=0; latitude=54.88; days = np.arange(0,364,1)
#nutrients
nh4 = np.zeros(365); nh4[0] = 2 
no2 = np.zeros(365); no2[0] = 1.5
no3 = np.zeros(365); no3[0] = no3_data[0] 
si = np.zeros(365); si[0] = si_data[0] 
po4 = np.zeros(365); po4[0] = po4_data[0] 
o2 = np.zeros(365); o2[0] = o2_data[0] 
#phy
phy = np.zeros(365); phy[0] = 90
# daily irradiance, convertion microM per second to M per day
irradiance = par*86400/1000000
#het
het = np.zeros(365); het[0] = 90
#om
poml = np.zeros(365); poml[0] = 100; pomr = np.zeros(365); pomr[0] = 100
doml = np.zeros(365); doml[0] = 50; domr = np.zeros(365); domr[0] = 50

#initial parameters values
#horizontal advection
k_mix=0.1
#phy
knh4_lim=0.1; knox_lim=0.1; ksi_lim=0.1; kpo4_lim=0.1; pbm=8; alpha=0.04; kexc=0.015; kmortality=0.0001
#het
k_het_phy_gro=0.2; k_het_phy_lim=0.4; k_het_pom_gro=k_het_phy_gro; k_het_pom_lim=k_het_phy_lim
k_het_res=0.015; k_het_mort=0.1; uz=0.5; hz=0.5
#nitrification
k_nfix = 0.4; k_nitrif1=0.1; k_nitrif2=0.1; o2s_nf=5; k_anammox=0.8; o2s_dn=10
#om respiration
k_poml_doml=0.15; k_pomr_domr=0.00001; k_omox_o2=1; tref=0
k_doml_ox=0.1; k_poml_ox=0.02; k_domr_ox=0.1; k_pomr_ox=0.002

chl_a, phy_dgrate, rations = bf.calculate(
   depth, k, k_mix, latitude,
   days, temperature,
   nh4, no2, no3, si, po4, o2,
   nh4_data, no3_data, si_data, po4_data,
   phy, par, irradiance,
   knh4_lim, knox_lim, ksi_lim, kpo4_lim, pbm, alpha, kexc, kmortality,
   het, k_het_phy_gro, k_het_phy_lim, k_het_pom_gro, k_het_pom_lim, k_het_res, k_het_mort, uz, hz,
   k_nfix, k_nitrif1, k_nitrif2, o2s_nf, k_anammox, o2s_dn,
   poml, doml, pomr, domr,
   k_poml_doml, k_pomr_domr, k_omox_o2, tref, k_doml_ox, k_poml_ox, k_domr_ox, k_pomr_ox)

#foo = lff.run_least_squares(lff.construct_least_squares(depth, k, latitude,
#        days, temperature,
#        nh4, no2, no3, si, po4, o2,
#        phy, par, irradiance,
#        het, uz, hz,
#        k_nfix, k_nitrif1, k_nitrif2, o2s_nf, k_anammox, o2s_dn,
#        poml, doml, pomr, domr,
#        k_poml_doml, k_pomr_domr, k_omox_o2, tref, k_doml_ox, k_poml_ox, k_domr_ox, k_pomr_ox,
#        chl_a_data))
