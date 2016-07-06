# encoding: utf-8

import ckan.plugins as p
import ckan.plugins.toolkit as tk

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
        for tag in ('Biota', 'Boundaries', 'Climatology', 'Meteorology', 'Atmosphere', 'Economy', 'Elevation', 'Environment', 'Farming', 'Geoscientific information', 'Health', 'Imagery base maps earth cover', 'Inland waters', 'Intelligence military', 'Oceans', 'Planning cadastre', 'Society', 'Structure', 'Transportation', 'Utilities communication'):
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
        for tag in ('Addresses',
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
        for tag in ('Resource provider',
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

class Aquacross_MetadataPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)
    p.implements(p.ITemplateHelpers)

    def get_helpers(self):
        return {'md_inspire_themes': md_inspire_themes,
                'md_classification_codes': md_classification_codes,
                'md_responsible_party_roles': md_responsible_party_roles}

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')

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
                                               tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'md_limitations_on_puclic_use': [tk.get_validator('ignore_missing'),
                                             tk.get_converter('convert_to_extras')]
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
            'md_spatial_representation_type': [tk.get_converter('convert_from_extras'),
                                               tk.get_validator('ignore_missing')]
        })
        schema.update({
            'md_limitations_on_puclic_use': [tk.get_converter('convert_from_extras'),
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
