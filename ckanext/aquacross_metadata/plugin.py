# encoding: utf-8

import ckan.plugins as p
import ckan.plugins.toolkit as tk
import ckan.lib.navl.dictization_functions as df

def before_validator(key, flattened_data, errors, context):

    # Metadata form workflow notes:
    # Form variables:
    #   md_bbox_north (north latitude, used to help build the geoJSON Polygon)
    #   md_bbox_south (south latitude, used to help build the geoJSON Polygon)
    #   md_bbox_east (east longitude, used to help build the geoJSON Polygon)
    #   md_bbox_west (west longitude, used to help build the geoJSON Polygon)

    # If the user did not select or enter a bounding box, then all variables are empty. 
    # As bounding box is not mandatory in the form, no validation required

    # Otherwise, we are checking if the 4 cordinates are valid (non-empty, valid number, in range) 
    # if valid, we create a geoJSON polygon, and populate the 'spatial' field in the metadata schema.

    # Note: We will have 2 duplicate bounding box information in the metadata schema.
    # 1) the 4 individual coordinate fields
    # 2) the spatial field in GeoJON format
   
    # get the spatial bounding box selected or input by the user via the HTML form
    north = flattened_data[('md_bbox_north',)]
    south = flattened_data[('md_bbox_south',)]
    east = flattened_data[('md_bbox_east',)]
    west = flattened_data[('md_bbox_west',)]

    # check if no bounding box
    if (not north or north is df.missing) and \
       (not south or south is df.missing) and \
       (not east or east is df.missing) and \
       (not west or west is df.missing):

        # all from input fields are empty, no bounding box, no validation required, return
        return

    # we have a bounding box (or attempted bounding box at least)... validate...
    no_errors = True

    # validate north
    north_valid = False
    if (not north or north is df.missing):
        errors[('md_bbox_north',)].append('Missing latitude value. Values must be between -90 and 90')
    else:
        north_float = 0.0
        try:
            north_float = float(north)
            if north_float < -90.0 or north_float > 90.0:
                errors[('md_bbox_north',)].append('Invalid latitude value. Values must be between -90 and 90')
            else:
                north_valid = True
        except (AttributeError, ValueError), e:
            errors[('md_bbox_north',)].append('Invalid latitude value. Values must be between -90 and 90')
    no_errors = north_valid

    # validate south
    south_valid = False
    if (not south or south is df.missing):
        errors[('md_bbox_south',)].append('Missing latitude value. Values must be between -90 and 90')
    else:
        south_float = 0.0
        try:
            south_float = float(south)
            if south_float < -90.0 or south_float > 90.0:
                errors[('md_bbox_south',)].append('Invalid latitude value. Values must be between -90 and 90')
            else:
                south_valid = True
        except (AttributeError, ValueError), e:
            errors[('md_bbox_south',)].append('Invalid latitude value. Values must be between -90 and 90')
    no_errors = no_errors and south_valid

    # validate north with south
    if north_valid and south_valid and south_float > north_float:
        errors[('md_bbox_north',)].append('Invalid latitude value. North must be greater or equal to South')
        errors[('md_bbox_south',)].append('Invalid latitude value. North must be greater or equal to South')
        no_errors = False

    # validate east
    east_valid = False
    if (not east or east is df.missing):
        errors[('md_bbox_east',)].append('Missing longitude value. Values must be between -180 and 180')
    else:
        east_float = 0.0
        try:
            east_float = float(east)
            if east_float < -180.0 or east_float > 180.0:
                errors[('md_bbox_east',)].append('Invalid longitude value. Values must be between -180 and 180')
            else:
                east_valid = True
        except (AttributeError, ValueError), e:
            errors[('md_bbox_east',)].append('Invalid longitude value. Values must be between -180 and 180')
    no_errors = no_errors and east_valid

    # validate west
    west_valid = False
    if (not west or west is df.missing):
        errors[('md_bbox_west',)].append('Missing longitude value. Values must be between -180 and 180')
    else:
        west_float = 0.0
        try:
            west_float = float(west)
            if west_float < -180.0 or west_float > 180.0:
                errors[('md_bbox_west',)].append('Invalid longitude value. Values must be between -180 and 180')
            else:
                west_valid = True
        except (AttributeError, ValueError), e:
            errors[('md_bbox_west',)].append('Invalid longitude value. Values must be between -180 and 180')
    no_errors = no_errors and west_valid

    # validate east with west
    if east_valid and west_valid and west_float > east_float:
        errors[('md_bbox_east',)].append('Invalid longitude value. East must be greater or equal to West')
        errors[('md_bbox_west',)].append('Invalid longitude value. East must be greater or equal to West')
        no_errors = False

    # create a geoJSON polygon, and populate the 'spatial' field in the metadatad schema 
    if no_errors:
        spatial_field = '{ "type": "Polygon", "coordinates": [[[' + east + "," + south + "], [" + east + "," + north + "], [" + west + ", " + north + "], [" + west + "," + south + "],[" + east + "," + south + "]]]}"
        flattened_data[('spatial',)] = spatial_field
    return


# Classification codes
def create_md_classification_codes():
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    print("create_md_classification_codes")
    try:
        data = {'id': 'md_classification_codes'}
        #tk.get_action('vocabulary_delete')(context, data)
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'md_classification_codes'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        for tag in ('   ', 
                    'Biota', 'Boundaries', 'Climatology', 'Meteorology', 'Atmosphere', 'Economy', 'Elevation', 'Environment', 'Farming', 'Geoscientific information', 'Health', 'Imagery base maps earth cover', 'Inland waters', 'Intelligence military', 'Oceans', 'Planning cadastre', 'Society', 'Structure', 'Transportation', 'Utilities communication'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)

def md_classification_codes():
    create_md_classification_codes()
    try:
        tag_list = tk.get_action('tag_list')
        md_classification_codes = tag_list(data_dict={'vocabulary_id': 'md_classification_codes'})
        return md_classification_codes
    except tk.ObjectNotFound:
        return None

# Spatial representation type
def create_md_spatial_representation_types():
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    print("create_md_spatial_representation_types")
    try:
        data = {'id': 'md_spatial_representation_types'}
        #tk.get_action('vocabulary_delete')(context, data)
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'md_spatial_representation_types'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        for tag in ('   ', 
                    'grid',
                    'stereoModel',
                    'textTable',
                    'tin',
                    'vector', 
                    'video'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)

def md_spatial_representation_types():
    create_md_spatial_representation_types()
    try:
        tag_list = tk.get_action('tag_list')
        md_spatial_representation_types = tag_list(data_dict={'vocabulary_id': 'md_spatial_representation_types'})
        return md_spatial_representation_types
    except tk.ObjectNotFound:
        return None

# INSPIRE themes
def create_md_inspire_themes():
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    print("create_md_inspire_themes")
    try:
        data = {'id': 'md_inspire_themes'}
        #tk.get_action('vocabulary_delete')(context, data)
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'md_inspire_themes'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        for tag in ('   ',
                    'Addresses',
                    'Administrative units',
                    'Agricultural and aquaculture facilities',
                    'Area management - restriction - regulation zones - reporting units', 
                    'Atmospheric conditions',
                    'Bio-geographical regions',
                    'Buildings',
                    'Cadastral parcels',
                    'Coordinate reference systems',
                    'Elevation',
                    'Energy resources',
                    'Environmental monitoring facilities',
                    'Geographical grid systems',
                    'Geographical names',
                    'Geology',
                    'Habitats and biotopes',
                    'Human health and safety',
                    'Hydrography',
                    'Land cover',
                    'Land use',
                    'Meteorological geographical features',
                    'Mineral resources',
                    'Natural risk zones',
                    'Oceanographic geographical features',
                    'Orthoimagery',
                    'Population distribution - demography',
                    'Production and industrial facilities',
                    'Protected sites',
                    'Sea regions',
                    'Soil',
                    'Species distribution',
                    'Statistical units',
                    'Transport networks',
                    'Utility and governmental services'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)

def md_inspire_themes():
    create_md_inspire_themes()
    try:
        tag_list = tk.get_action('tag_list')
        md_inspire_themes = tag_list(data_dict={'vocabulary_id': 'md_inspire_themes'})
        return md_inspire_themes
    except tk.ObjectNotFound:
        return None

# Responsible party roles
def create_md_responsible_party_roles():
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    print("create_md_responsible_party_roles")
    try:
        data = {'id': 'md_responsible_party_roles'}
        #tk.get_action('vocabulary_delete')(context, data)
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'md_responsible_party_roles'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        for tag in ('   ',
                    'Resource provider',
                    'Custodian',
                    'Owner',
                    'User',
                    'Distributor',
                    'Originator',
                    'Point of Contact',
                    'Principal Investigator',
                    'Processor',
                    'Publisher', 
                    'Author'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)

def md_responsible_party_roles():
    create_md_responsible_party_roles()
    try:
        tag_list = tk.get_action('tag_list')
        md_responsible_party_roles = tag_list(data_dict={'vocabulary_id': 'md_responsible_party_roles'})
        return md_responsible_party_roles
    except tk.ObjectNotFound:
        return None

def create_md_projections():
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    print("create_md_projections")
    try:
        data = {'id': 'md_projections'}
        #tk.get_action('vocabulary_delete')(context, data)
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'md_projections'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        for tag in ('   ',
                    'ETRS89 - ETRS-LAEA -- EPSG-3035',
                    'ETRS89 - ETRS-LCC  -- EPSG-3034',
                    'ETRS89 - ETRS-TM26 -- EPSG-3038',
                    'ETRS89 - ETRS-TM27 -- EPSG-3039',
                    'ETRS89 - ETRS-TM28 -- EPSG-3040',
                    'ETRS89 - ETRS-TM29 -- EPSG-3041',
                    'ETRS89 - ETRS-TM30 -- EPSG-3042',
                    'ETRS89 - ETRS-TM31 -- EPSG-3043',
                    'ETRS89 - ETRS-TM32 -- EPSG-3044',
                    'ETRS89 - ETRS-TM33 -- EPSG-3045',
                    'ETRS89 - ETRS-TM34 -- EPSG-3046',
                    'ETRS89 - ETRS-TM35 -- EPSG-3047',
                    'ETRS89 - ETRS-TM36 -- EPSG-3048',
                    'ETRS89 - ETRS-TM37 -- EPSG-3049',
                    'ETRS89 - ETRS-TM38 -- EPSG-3050',
                    'ETRS89 - ETRS-TM39 -- EPSG-3051',
                    'EPSG 2190 - Azores Oriental 1940 - UTM zone 26N',
                    'EPSG 2188 - Azores Occidental 1939 - UTM zone 25N',
                    'WGS 84 -- EPSG-4326'
                   ):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)
    else:

        data = {'id': 'md_projections'}
        vocab = tk.get_action('vocabulary_update')(context, data)

        tag_list = tk.get_action('tag_list')
        md_projections = tag_list(data_dict={'vocabulary_id': 'md_projections'})

        for tag in ('EPSG 2190 - Azores Oriental 1940 - UTM zone 26N',
                    'EPSG 2188 - Azores Occidental 1939 - UTM zone 25N'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            if (tag not in md_projections):
                tk.get_action('tag_create')(context, data)

def md_projections():

    create_md_projections()

    try:
        tag_list = tk.get_action('tag_list')
        md_projections = tag_list(data_dict={'vocabulary_id': 'md_projections'})
        return md_projections
        #return 'foo'
    except tk.ObjectNotFound:
        return None

# Resource type
def create_md_resource_types():
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    print("create_md_resource_types")
    try:
        data = {'id': 'md_resource_types'}
        #tk.get_action('vocabulary_delete')(context, data)
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'md_resource_types'}
        vocab = tk.get_action('vocabulary_create')(context, data)

        for tag in ('   ',
                    'Spatial dataset',
                    'Spatial dataset series',
                    'Spatial data service'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)

def md_resource_types():
    create_md_resource_types()
    try:
        tag_list = tk.get_action('tag_list')

        md_resource_types = tag_list(data_dict={'vocabulary_id': 'md_resource_types'})
        #print "ResourceTypes",md_resource_types
        return md_resource_types
    except tk.ObjectNotFound:
        return None

# Date types - md_keywords_vocab_date_type
def create_md_keywords_vocab_date_types():
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    print("create_md_keywords_vocab_date_types")
    try:
        data = {'id': 'md_keywords_vocab_date_types'}
        #tk.get_action('vocabulary_delete')(context, data)
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'md_keywords_vocab_date_types'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        for tag in ('   ',
                    'Date of creation',
                    'Date of revision',
                    'Date of publication'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)

def md_keywords_vocab_date_types():
    create_md_keywords_vocab_date_types()
    try:
        tag_list = tk.get_action('tag_list')
        md_keywords_vocab_date_types = tag_list(data_dict={'vocabulary_id': 'md_keywords_vocab_date_types'})
        return md_keywords_vocab_date_types
    except tk.ObjectNotFound:
        return None

# Metadata Plugin Class
class Aquacross_MetadataPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)
    p.implements(p.ITemplateHelpers)

    def get_helpers(self):
        return {'md_inspire_themes': md_inspire_themes,
                'md_classification_codes': md_classification_codes,
                'md_spatial_representation_types': md_spatial_representation_types,
                'md_responsible_party_roles': md_responsible_party_roles,
                'md_projections': md_projections,
                'md_resource_types': md_resource_types,
                'md_keywords_vocab_date_types': md_keywords_vocab_date_types}

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')
        # Register this plugin's fanstatic directory with CKAN.
        # Here, 'fanstatic' is the path to the fanstatic directory
        # (relative to this plugin.py file), and 'aquacross-metadata' is the name
        # that we'll use to refer to this fanstatic directory from CKAN
        # templates.
        tk.add_resource('fanstatic', 'aquacross-metadata')

    def _modify_package_schema(self, schema):
        schema.update({
            '__before': [before_validator, tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_email_address': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
#        schema.update({
#            'md_metadata_date': [tk.get_validator('ignore_missing'),
#                                 tk.get_converter('convert_to_extras')]
#        })
        schema.update({
            'md_language': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_resource_type': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_tags')('md_resource_types')
            ]
        })
        schema.update({
            'md_abstract': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_dataset_creation_date': [tk.get_validator('ignore_missing'),
                                         tk.get_converter('convert_to_extras')]
        })        
        schema.update({
            'md_dataset_publication_date': [tk.get_validator('ignore_missing'),
                                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_dataset_last_revision_date': [tk.get_validator('ignore_missing'),
                                              tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_classification_code': [tk.get_validator('ignore_missing'),
                                       tk.get_converter('convert_to_tags')('md_classification_codes')
            ]
        })
        schema.update({
            'md_inspire_theme': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_tags')('md_inspire_themes')
            ]
        })

        schema.update({
            'md_keywords': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_keywords_vocab_title': [tk.get_validator('ignore_missing'),
                                        tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_keywords_vocab_date': [tk.get_validator('ignore_missing'),
                                    tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_keywords_vocab_date_type': [tk.get_validator('ignore_missing'),
                                            tk.get_converter('convert_to_tags')('md_keywords_vocab_date_types')
            ]
        })

        schema.update({
            'md_bbox_north': [tk.get_validator('ignore_missing'),
                              tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_bbox_south': [tk.get_validator('ignore_missing'),
                              tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_bbox_east': [tk.get_validator('ignore_missing'),
                             tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_bbox_west': [tk.get_validator('ignore_missing'),
                             tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'spatial': [tk.get_validator('ignore_missing'),
                                       tk.get_converter('convert_to_extras')]
        })

        schema.update({
            'md_temporal_date': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_temporal_start_date': [tk.get_validator('ignore_missing'),
                                       tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_temporal_end_date': [tk.get_validator('ignore_missing'),
                                     tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_lineage': [tk.get_validator('ignore_missing'),
                           tk.get_converter('convert_to_extras')]
        })

        schema.update({
            'md_responsible_party_name': [tk.get_validator('ignore_missing'),
                                          tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_responsible_party_email': [tk.get_validator('ignore_missing'),
                                           tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_responsible_party_role': [tk.get_validator('ignore_missing'),
                                          tk.get_converter('convert_to_tags')('md_responsible_party_roles')
            ]
        })
        schema.update({
            'md_related_publications': [tk.get_validator('ignore_missing'),
                                          tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_spatial_representation_type': [tk.get_validator('ignore_missing'),
                                               tk.get_converter('convert_to_tags')('md_spatial_representation_types')
            ]
        })
        schema.update({
            'md_limitations_on_puclic_use': [tk.get_validator('ignore_missing'),
                                             tk.get_converter('convert_to_extras')]
        })

        schema.update({
            'md_projections': [tk.get_validator('ignore_missing'),
                                        tk.get_converter('convert_to_tags')('md_projections')
                                        ]
        })
        return schema

    def create_package_schema(self):
        schema = super(Aquacross_MetadataPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(Aquacross_MetadataPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(Aquacross_MetadataPlugin, self).show_package_schema()
        schema.update({
            'md_email_address': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')]
        })
#        schema.update({
#            'md_metadata_date': [tk.get_converter('convert_from_extras'),
#                                 tk.get_validator('ignore_missing')]
#        })
        schema.update({
            'md_language': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_resource_type': [
                tk.get_converter('convert_from_tags')('md_resource_types'),
                tk.get_validator('ignore_missing')]
            })
        schema.update({
            'md_abstract': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })

        schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))

        schema.update({
            'md_classification_code': [
                tk.get_converter('convert_from_tags')('md_classification_codes'),
                tk.get_validator('ignore_missing')]
            })

        schema.update({
            'md_dataset_creation_date': [tk.get_converter('convert_from_extras'),
                                         tk.get_validator('ignore_missing')]
        })

        schema.update({
            'md_dataset_publication_date': [tk.get_converter('convert_from_extras'),
                                            tk.get_validator('ignore_missing')]
        })

        schema.update({
            'md_dataset_last_revision_date': [tk.get_converter('convert_from_extras'),
                                              tk.get_validator('ignore_missing')]
        })

        schema.update({
            'md_inspire_theme': [
                tk.get_converter('convert_from_tags')('md_inspire_themes'),
                tk.get_validator('ignore_missing')]
            })

        schema.update({
            'md_keywords': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_keywords_vocab_title': [tk.get_converter('convert_from_extras'),
                                        tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_keywords_vocab_date': [tk.get_converter('convert_from_extras'),
                                       tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_keywords_vocab_date_type': [
                tk.get_converter('convert_from_tags')('md_keywords_vocab_date_types'),
                tk.get_validator('ignore_missing')]
            })

        schema.update({
            'md_bbox_north': [tk.get_converter('convert_from_extras'),
                              tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_bbox_south': [tk.get_converter('convert_from_extras'),
                              tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_bbox_east': [tk.get_converter('convert_from_extras'),
                             tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_bbox_west': [tk.get_converter('convert_from_extras'),
                             tk.get_validator('ignore_missing')]
        })
        schema.update({
            'spatial': [tk.get_converter('convert_from_extras'),
                             tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_temporal_date': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_temporal_start_date': [tk.get_converter('convert_from_extras'),
                                       tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_temporal_end_date': [tk.get_converter('convert_from_extras'),
                                     tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_lineage': [tk.get_converter('convert_from_extras'),
                           tk.get_validator('ignore_missing')]
        })

        schema.update({
            'md_responsible_party_name': [tk.get_converter('convert_from_extras'),
                                          tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_responsible_party_email': [tk.get_converter('convert_from_extras'),
                                           tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_responsible_party_role': [
                tk.get_converter('convert_from_tags')('md_responsible_party_roles'),
                tk.get_validator('ignore_missing')]
            })
        schema.update({
            'md_related_publications': [tk.get_converter('convert_from_extras'),
                                        tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_spatial_representation_type': [
                tk.get_converter('convert_from_tags')('md_spatial_representation_types'),
                tk.get_validator('ignore_missing')]
            })

        schema.update({
            'md_limitations_on_puclic_use': [tk.get_converter('convert_from_extras'),
                                             tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_projections': [
                tk.get_converter('convert_from_tags')('md_projections'),
                tk.get_validator('ignore_missing')]
        })
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
