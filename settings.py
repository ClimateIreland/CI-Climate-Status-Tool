ATMOSPHERE_COLOR='#009fe3'
OCEAN_COLOR='#00909e'
TERRESTRIAL_COLOR='#f39200'

ATMOSPHERE_BG_COLOR='#e6f5fc'
OCEAN_BG_COLOR='#e6f3f5'
TERRESTRIAL_BG_COLOR='#fef4e6'

CHAPTERS = [

        # Upper-air Atmoshere
        # {
        #  'id':'uaa-1',
        #  'name':'Lightning', 
        #  'href':'',
        #  'icon-src':'ico-uaa-lightning.png',
        #  'icon-hover-src':'ico-uaa-lightning_hover.png',
        #  'domain':'Atmosphere',
        #         },
        #     {
        #  'id':'uaa-2',
        #  'name':'Clouds', 
        #  'href':'',
        #  'icon-src':'ico-uaa-cloud-properties.png',
        #  'icon-hover-src':'ico-uaa-cloud-properties_hover.png',
        #  'domain':'Atmosphere',
        #         },
        #             {
        #  'id':'uaa-3',
        #  'name':'Earth Radiation Budget', 
        #  'href':'',
        #  'icon-src':'ico-uaa-earth-radiation-budget.png',
        #  'icon-hover-src':'ico-uaa-earth-radiation-budget_hover.png',
        #  'domain':'Atmosphere',
        #         },
        #             {
        #  'id':'uaa-4',
        #  'name':'Wind Speed', 
        #  'href':'',
        #  'icon-src':'ico-uaa-lightning.png',
        #  'icon-hover-src':'ico-uaa-windspeed_hover.png',
        #  'domain':'Atmosphere',
        #         },
        #             {
        #  'id':'uaa-5',
        #  'name':'Upper Air Atmosphere Temperature', 
        #  'href':'',
        #  'icon-src':'ico-uaa-temperature.png',
        #  'icon-hover-src':'ico-uaa-temperature_hover.png',
        #  'domain':'Atmosphere',
        #         },
        #             {
        #  'id':'uaa-6',
        #  'name':'Upper Air Atmosphere Water Vapour', 
        #  'href':'',
        #  'icon-src':'ico-uaa-watervapour.png',
        #  'icon-hover-src':'ico-uaa-watervapour_hover.png',
        #  'domain':'Atmosphere',
        #         },
            # Surface Atmoshere
        #             {
        #  'id':'sa-1',
        #  'name':'Surface Atmosphere Precipitation', 
        #  'href':'',
        #  'icon-src':'ico-sa-precipitation.png',
        #  'icon-hover-src':'ico-sa-precipitation_hover.png',
        #  'domain':'Atmosphere',
                # },
                {
        'chapter':2.1,
        'id':'sa-5',
        'name':'Surface Temperature', 
        'href':'/_2_1_SurfaceAirTemperature',
        'icon-src':'ico-sa-temperature.png',
        'icon-hover-src':'ico-sa-temperature_hover.png',
        'domain':'Atmosphere',
        'domain-color':ATMOSPHERE_COLOR,
        'domain-bg-color':ATMOSPHERE_BG_COLOR
   
                },
            # Atmoshperic Composition
            #    {
        #  'id':'ac-2',
        #  'name':'Carbon Dioxide, Methane and other Greenhouse gases', 
        #  'name':'Carbon Dioxide', 
        #  'href':'',
        #  'icon-src':'ico-ac-co2-ghgs.png',
        #  'icon-hover-src':'ico-ac-co2-ghgs_hover.png',
        #  'domain':'Atmosphere',
                # },
        #     {
        # 'id':'ac-4',
        #  'name':'Atmospheric Composition Precursors', 
        #  'name':'Methane', 
        #  'href':'',
        #  'icon-src':'ico-ac-precursors.png',
        #  'icon-hover-src':'ico-ac-precursors_hover.png',
        #  'domain':'Atmosphere',
        #         },
        # Biosphere
            {
        'chapter':4.6,
        'id':'bio-2',
        'name':'Land Cover', 
        'href':'/_4_6_LandCover',
        'icon-src':'ico-bio-land-cover.png',
        'icon-hover-src':'ico-bio-land-cover_hover.png',
        'domain':'Terrestrial',
        'domain-color':TERRESTRIAL_COLOR,
        'domain-bg-color':TERRESTRIAL_BG_COLOR
                },
                    {
        'chapter':4.7,
        'id':'bio-7',
        'name':'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR)', 
        'href':'/_4_7_FAPAR',
        'icon-src':'ico-bio-fapr.png',
        'icon-hover-src':'ico-bio-fapr_hover.png',
        'domain':'Terrestrial',
        'domain-color':TERRESTRIAL_COLOR,
        'domain-bg-color':TERRESTRIAL_BG_COLOR
                },

        # Ocean Biogeochemistry

                        {
        'chapter':3.7,
        'id':'obgc-2',
        'name':'Oxygen', 
        'href':'/_3_7_DissolvedOxygen',
        'icon-src':'ico-obgc-oxygen.png',
        'icon-hover-src':'ico-obgc-oxygen_hover.png',
        'domain':'Ocean',
        'domain-color':OCEAN_COLOR,
        'domain-bg-color':OCEAN_BG_COLOR
                }
                ]