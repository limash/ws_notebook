## "Seasonal alkalinity release from coastal area sediments, the case of the Wadden Sea" research article supplementary material

* 1_generate_the_Wadden_Sea.ipynb - is a jupyter notebook generating a NetCDF file for the [SPBM] transport model.
* 2_x_some_tests_and_estimations.ipynb - plots some data from a generated file, visualize some functions (for example different s-curves) which are used to construct a biogeochemica model; also contains some routines to calculate quantities described in the article, it requires model output data files [data].
* 3_biogeochemical_model_parameters_identification.ipynb - model parameters optimization, uses [LMFIT]; draws modelled chlorophyll a vs chlorophyll a from the World Ocean Database.
* 4_OM_production_validation.ipynb - calculates a total amount of OM generated by the model to ensure it matches exactly the amount of OM produced at the Wadden Sea.

[SPBM]:https://github.com/BottomRedoxModel/SPBM/tree/dev-sham
[data]:https://drive.google.com/drive/folders/1YtCpb_DLIqm6IXdTP62cm4VwFFqfCRuI?usp=sharing
[LMFIT]:https://lmfit.github.io/lmfit-py/intro.html
