# encoding: utf-8

import ckan.plugins as p
import ckan.plugins.toolkit as tk

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

# AQUACROSS WP
def create_md_aquacross_wps():
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    print("create_md_aquacross_wps")
    try:
        data = {'id': 'md_aquacross_wps'}
        #tk.get_action('vocabulary_delete')(context, data)
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'md_aquacross_wps'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        for tag in ('   ',
                    'WP1',
                    'WP2',
                    'WP3',
                    'WP4',
                    'WP5',
                    'WP6',
                    'WP7',
                    'WP8'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)

def md_aquacross_wps():
    create_md_aquacross_wps()
    try:
        tag_list = tk.get_action('tag_list')
        md_aquacross_wps = tag_list(data_dict={'vocabulary_id': 'md_aquacross_wps'})
        return md_aquacross_wps
    except tk.ObjectNotFound:
        return None

# AQUACROSS Case Study
def create_md_aquacross_case_studies():
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    print("create_md_aquacross_case_studies")
    try:
        data = {'id': 'md_aquacross_case_studies'}
        #tk.get_action('vocabulary_delete')(context, data)
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'md_aquacross_case_studies'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        for tag in ('   ',
                    'Case Study 1 - North Sea',
                    'Case Study 2 - Mediterranean - Andalusia Spain and Morocco',
                    'Case Study 3 - Danube River Basin',
                    'Case Study 4 - Lough Erne - Ireland',
                    'Case Study 5 - Vouga River - Portugal',
                    'Case Study 6 - Ronne a - Sweden',
                    'Case Study 7 - Swiss Plateau',
                    'Case Study 8 - The Azores'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)

def md_aquacross_case_studies():

    create_md_aquacross_case_studies()
    try:
        tag_list = tk.get_action('tag_list')
        md_aquacross_case_studies = tag_list(data_dict={'vocabulary_id': 'md_aquacross_case_studies'})
        return md_aquacross_case_studies
        #return 'foo'
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
                'md_aquacross_wps': md_aquacross_wps,
                'md_aquacross_case_studies': md_aquacross_case_studies,
                'md_projections': md_projections,
                'md_resource_types': md_resource_types,
                'md_keywords_vocab_date_types': md_keywords_vocab_date_types}

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')
        # Register this plugin's fanstatic directory with CKAN.
        # Here, 'fanstatic' is the path to the fanstatic directory
        # (relative to this plugin.py file), and 'my_fanstatic' is the name
        # that we'll use to refer to this fanstatic directory from CKAN
        # templates.
        tk.add_resource('fanstatic', 'my_fanstatic')

    def _modify_package_schema(self, schema):
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
            'md_aquacross_wp': [tk.get_validator('ignore_missing'),
                                tk.get_converter('convert_to_tags')('md_aquacross_wps')
            ]
        })
        schema.update({
            'md_aquacross_case_study': [tk.get_validator('ignore_missing'),
                                        tk.get_converter('convert_to_tags')('md_aquacross_case_studies')
            ]
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
            'md_aquacross_wp': [
                tk.get_converter('convert_from_tags')('md_aquacross_wps'),
                tk.get_validator('ignore_missing')]
            })
        schema.update({
            'md_aquacross_case_study': [
                tk.get_converter('convert_from_tags')('md_aquacross_case_studies'),
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
