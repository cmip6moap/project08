import iris
import glob
import numpy as np

realisation = 'ssp585'
var = 'MMM_{}_anomaly_surface_temperature'.format(realisation)

files = glob.glob('/gws/pw/j05/cop26_hackathons/bristol/project08/hist+{}/*.nc'.format(realisation))

mdls = np.unique([file.split('/')[-1].split('_')[1] for file in files])

# Group model files together

mdl_dict = {}
for file in files:
	mdl = file.split('/')[-1].split('_')[1]
	if mdl not in mdl_dict.keys():
		mdl_dict[mdl] = [file]
	else:
		mdl_dict[mdl] = mdl_dict[mdl] + [file]

MMM_cube = iris.load_cube(files[0])
mean_model_cube_data = []
for mdl in mdl_dict.keys():
	cubes_data = np.asarray([iris.load_cube(file).data for file in mdl_dict[mdl]])
	padded_cubes_data = [np.pad(c, pad_width=((0, 3012 - c.shape[0]),(0,0),(0,0)), mode='constant', constant_values=np.nan) for c in cubes_data]
	mean_model_cube_data.append(np.nanmean(padded_cubes_data, axis=0))


MMM_cube = MMM_cube.copy(np.nanmean(np.asarray(mean_model_cube_data), axis=0))

iris.save(MMM_cube, '/gws/pw/j05/cop26_hackathons/bristol/project08/hist+{}/'.format(realisation) + var + '.nc')


import iris.coord_categorisation

MMM_cube_file = '/gws/pw/j05/cop26_hackathons/bristol/project08/hist+{}/MMM_{}_anomaly_surface_temperature.nc'.format(realisation, realisation)

cube = iris.load_cube(MMM_cube_file)

def global_annual_mean(cube):
    # Global area weighted mean
    if not cube.coord('latitude').has_bounds():
        cube.coord('latitude').guess_bounds()
    if not cube.coord('longitude').has_bounds():
        cube.coord('longitude').guess_bounds()
    grid_areas = iris.analysis.cartography.area_weights(cube)
    cube = cube.collapsed(['longitude', 'latitude'], iris.analysis.MEAN, weights=grid_areas)
    
    # Get annual mean
   	if 'year' not in [c.name() for c in cube.coords()]:
   	    iris.coord_categorisation.add_year(cube, cube.coord('time'))
    cube = cube.aggregated_by(cube.coord('year'), iris.analysis.MEAN)
    
    return cube

GMST = global_annual_mean(cube)
iris.save(GMST, '/gws/pw/j05/cop26_hackathons/bristol/project08/hist+{}/MMM_{}_anomaly_annual_GMST.nc'.format(realisation, realisation))