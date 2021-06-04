#!/bin/env python

import iris
import numpy as np
import datetime
import cf_units
import sys
import glob
from iris.experimental.equalise_cubes import equalise_attributes
import iris.coord_categorisation as cc

realisation = 'ssp126'

def unify_time_axes(cubes):

    units = []
    for cube in cubes:
        tc = cube.coord('time')
        units.append(tc.units)

    if len(set(units)) != 1:
        new_unit = sorted(units)[0]
        new_cubes = []
        for cube in cubes:
            cube.coord('time').convert_units(new_unit)
            new_cubes.append(cube)
    else:
        new_cubes = cubes

    return new_cubes

def rem_and_eq(cubes):
    equalise_attributes(cubes)
    for cube in cubes:
        if cube.aux_factories:
            cube.remove_aux_factory(cube.aux_factories[0])
        aux_coords = cube.aux_coords
        for coord in aux_coords:
            cube.remove_coord(coord)
    return

def concat_(cubes):
    # Function to concatenate all cubes

    for cube in cubes:
        cube.coord('latitude').var_name = None
        cube.coord('latitude').long_name = None
        cube.coord('latitude').var_name = None
        cube.coord('longitude').long_name = None
    rem_and_eq(cubes)
    cubes = unify_time_axes(cubes)
    concat_cube = iris.cube.CubeList(cubes).concatenate_cube()

    return concat_cube

def regrid_(cube):
# Regrid cube to 36 x 72
    # Make regrid cube
    lats = iris.coords.DimCoord(np.arange(-90 + 2.5,90, 180/36), standard_name='latitude', units='degrees')
    lons = iris.coords.DimCoord(np.arange(0 + 2.5,360, 360/72), standard_name='longitude', units='degrees')

    scheme = iris.analysis.AreaWeighted(mdtol=1)
    regrid_cube = iris.cube.Cube(np.zeros([36, 72]))
    regrid_cube.add_dim_coord(lats, 0)
    regrid_cube.add_dim_coord(lons, 1)
    regrid_cube.coord('latitude').guess_bounds()
    regrid_cube.coord('longitude').guess_bounds()
    regrid_cube.coord('longitude').circular = True

    if not cube.coord('latitude').has_bounds():
        cube.coord('latitude').guess_bounds()
    if not cube.coord('longitude').has_bounds():
        cube.coord('longitude').guess_bounds()

    # Make sure bounds span space
    if cube.coord('latitude').bounds[0][0] != -90.0:
        lat_bounds = cube.coord('latitude').bounds.copy()
        lat_bounds[0][0] = -90.0
        lat_bounds[-1][-1] = 90.0
        cube.coord('latitude').bounds = lat_bounds
    if cube.coord('longitude').bounds[0][0] != 0.0:
        if np.abs(cube.coord('longitude').bounds[0][0]) < 5.:
            lon_bounds = cube.coord('longitude').bounds.copy()
            lon_bounds[0][0] = 0.0
            lon_bounds[-1][-1] = 360.0
        elif np.abs(cube.coord('longitude').bounds[0][0]) > 5.:
            lon_bounds = cube.coord('longitude').bounds.copy()
            lon_bounds[0][0] = -180.0
            lon_bounds[-1][-1] = 180.0
        cube.coord('longitude').bounds = lon_bounds

    regridded_cube = cube.regrid(regrid_cube, scheme)
    return regridded_cube

def anomally_(cube):
    # find anomally to 1961-1990.
    cc.add_year(cube, 'time')
    cc.add_month_number(cube, 'time')
    t0_idx = np.where(cube.coord('year').points == 1861)[0][0]
    t1_idx = np.where(cube.coord('year').points == 1890)[-1][-1]

    if t1_idx - t0_idx + 1 != 360:
        raise ValueError('Missing years probably')

    clim_data = cube[t0_idx: t1_idx].aggregated_by('month_number', iris.analysis.MEAN).data
    clim_rep = np.concatenate([clim_data] * int(len(cube.coord('time').points) / 12), axis=0)

    return cube - cube.copy(clim_rep)


 # Main code
hist_dir = sys.argv[1]
ssp_dir = sys.argv[2]

model_real_files = glob.glob(hist_dir + '/*.nc') + glob.glob(ssp_dir + '/*.nc')
if len(model_real_files) == 1:
    cube = iris.load_cube(model_real_files[0], 'air_temperature')
else:
    cubes = iris.load(model_real_files, 'air_temperature')
    # Concatenate the cubes 
    cube = concat_(cubes)

cube = regrid_(cube)
anom_cube = anomally_(cube)

mdl_name = '_'.join(np.array(hist_dir.split('/'))[[6,7,9]])
iris.save(anom_cube, '/gws/pw/j05/cop26_hackathons/bristol/project08/hist+{}}/'.format(realisation) + mdl_name + '.nc')
