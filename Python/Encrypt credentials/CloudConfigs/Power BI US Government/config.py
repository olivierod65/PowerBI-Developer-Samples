# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# Replace these configs with the one in the config.py file for sovereign cloud

class BaseConfig(object):

    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.usgovcloudapi.net/powerbi/api/.default']

    # URL used for initiating authorization request
    AUTHORITY_URL = 'https://login.microsoftonline.com/organizations'