import pathlib

PATH = pathlib.Path(__file__).parent

DATA_PATH='/Users/dan/OneDrive - University College Cork/Status_Tool/'
IMAGES_PATH='assets/images/'

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
                {
        'chapter':2.1,
        'id':'sa-1',
        'name':'Surface Temperature', 
        'href':'/_2_1_SurfaceAirTemperature',
        'icon-lg-src':'surface-temperature.png',
        'icon-src':'ico-sa-temperature.png',
        'icon-hover-src':'ico-sa-temperature_hover.png',
        'domain':'Atmosphere',
        'subdomain':'Surface',
        'scientific-area':'Energy and Temperature',
        'authors':'Walther C.A. Cámaro García, Ned Dwyer, Keith Lambkin',
        'domain-color':ATMOSPHERE_COLOR,
        'domain-bg-color':ATMOSPHERE_BG_COLOR
   
                },
                               {
        'chapter':2.5,
        'id':'sa-2',
        'name':'Precipitation', 
        'href':'/_2_5_Precipitation',
        'icon-lg-src':'precipitation.png',
        'icon-src':'ico-sa-precipitation.png',
        'icon-hover-src':'ico-sa-precipitation_hover.png',
        'domain':'Atmosphere',
        'subdomain':'',
        'scientific-area':'',
        'authors':'',
        'domain-color':ATMOSPHERE_COLOR,
        'domain-bg-color':ATMOSPHERE_BG_COLOR
   
                },
                                               {
        'chapter':2.10,
        'id':'ac-1',
        'name':'Carbon Dioxide', 
        'href':'/_2_10_CarbonDioxide',
        'icon-lg-src':'greenhouse-gases.png',
        'icon-src':'ico-ac-co2-ghgs.png',
        'icon-hover-src':'ico-ac-co2-ghgs_hover.png',
        'domain':'Atmosphere',
        'subdomain':'',
        'scientific-area':'',
        'authors':'',
        'domain-color':ATMOSPHERE_COLOR,
        'domain-bg-color':ATMOSPHERE_BG_COLOR
   
                },
                {
        'chapter':2.11,
        'id':'ac-2',
        'name':'Methane', 
        'href':'/_2_11_Methane',
        'icon-lg-src':'precursors_0.png',
        'icon-src':'ico-ac-precursors.png',
        'icon-hover-src':'ico-ac-precursors_hover.png',
        'domain':'Atmosphere',
        'subdomain':'',
        'scientific-area':'',
        'authors':'',
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

        # Ocean Biogeochemistry
                        {
        'chapter':3.1,
        'id':'sop-1',
        'name':'Surface Temperature', 
        'href':'/_3_1_SurfaceTemperature',
        'icon-lg-src':'sea-surface-temperature.png',
        'icon-src':'ico-sop-sea-surface-temp.png',
        'icon-hover-src':'ico-sop-sea-surface-temp_hover.png',
        'domain':'Ocean',
        'subdomain':'',
        'scientific-area':'',
        'authors':'',
        'domain-color':OCEAN_COLOR,
        'domain-bg-color':OCEAN_BG_COLOR
                },
                                        {
        'chapter':3.1,
        'id':'ssop-1',
        'name':'Sub-surface Temperature', 
        'href':'/_3_1_SubsurfaceTemperature',
        'icon-lg-src':'subsurface-temperature.png',
        'icon-src':'ico-ssop-subsurface-temp.png',
        'icon-hover-src':'ico-ssop-subsurface-temp_hover.png',
        'domain':'Ocean',
        'subdomain':'',
        'scientific-area':'',
        'authors':'',
        'domain-color':OCEAN_COLOR,
        'domain-bg-color':OCEAN_BG_COLOR
                },
                                                       {
        'chapter':3.4,
        'id':'sop-2',
        'name':'Sea Level', 
        'href':'/_3_4_SeaLevel',
        'icon-lg-src':'sea-level.png',
        'icon-src':'ico-sop-sea-level.png',
        'icon-hover-src':'ico-sop-sea-level_hover.png',
        'domain':'Ocean',
        'subdomain':'',
        'scientific-area':'',
        'authors':'',
        'domain-color':OCEAN_COLOR,
        'domain-bg-color':OCEAN_BG_COLOR
                },
                                                                       {
        'chapter':3.6,
        'id':'obgc-1',
        'name':'Inorganic Carbon', 
        'href':'/_3_6_InorganicCarbon',
        'icon-lg-src':'inorganic-carbon.png',
        'icon-src':'ico-obgc-inorganic-carbon.png',
        'icon-hover-src':'ico-obgc-inorganic-carbon_hover.png',
        'domain':'Ocean',
        'subdomain':'',
        'scientific-area':'',
        'authors':'',
        'domain-color':OCEAN_COLOR,
        'domain-bg-color':OCEAN_BG_COLOR
                },
                        {
        'chapter':3.7,
        'id':'obgc-2',
        'name':'Oxygen', 
        'href':'/_3_7_DissolvedOxygen',
        'icon-lg-src':'oxygen.png',
        'icon-src':'ico-obgc-oxygen.png',
        'icon-hover-src':'ico-obgc-oxygen_hover.png',
        'domain':'Ocean',
        'subdomain':'Biogeochemistry',
        'scientific-area':'Biosphere',
        'authors':'Walther C.A. Cámaro García, Ned Dwyer, Robert Wilkes, Rob Thomas, Evin McGovern',
        'domain-color':OCEAN_COLOR,
        'domain-bg-color':OCEAN_BG_COLOR
                },

        # Biosphere
            {
        'chapter':4.6,
        'id':'bio-1',
        'name':'Land Cover', 
        'href':'/_4_6_LandCover',
        'icon-lg-src':'land-cover.png',
        'icon-src':'ico-bio-land-cover.png',
        'icon-hover-src':'ico-bio-land-cover_hover.png',
        'domain':'Terrestrial',
        'subdomain':'Biology',
        'scientific-area':'Biosphere',
        'authors':'Walther C.A. Cámaro García, Ned Dwyer',
        'domain-color':TERRESTRIAL_COLOR,
        'domain-bg-color':TERRESTRIAL_BG_COLOR
                },
                    {
        'chapter':4.7,
        'id':'bio-2',
        'name':'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR)', 
        'href':'/_4_7_FAPAR',
        'icon-lg-src':'fapar.png',
        'icon-src':'ico-bio-fapr.png',
        'icon-hover-src':'ico-bio-fapr_hover.png',
        'domain':'Terrestrial',
        'subdomain':'Biology',
        'scientific-area':'Biosphere',
        'authors':'Walther C.A. Cámaro García, Ned Dwyer',
        'domain-color':TERRESTRIAL_COLOR,
        'domain-bg-color':TERRESTRIAL_BG_COLOR
                },
                                  {
        'chapter':4.1,
        'id':'hyd-1',
        'name':'River Discharge', 
        'href':'/_4_1_RiverDischarge',
        'icon-lg-src':'river-discharge.png',
        'icon-src':'ico-hyd-river-discharge.png',
        'icon-hover-src':'ico-hyd-river-discharge_hover.png',
        'domain':'Terrestrial',
        'subdomain':'',
        'scientific-area':'',
        'authors':'',
        'domain-color':TERRESTRIAL_COLOR,
        'domain-bg-color':TERRESTRIAL_BG_COLOR
                },
                                              {
        'chapter':4.11,
        'id':'bio-3',
        'name':'Fire', 
        'href':'/_4_11_Fire',
        'icon-lg-src':'fire_0.png',
        'icon-src':'ico-bio-fire.png',
        'icon-hover-src':'ico-bio-fire_hover.png',
        'domain':'Terrestrial',
        'subdomain':'',
        'scientific-area':'',
        'authors':'',
        'domain-color':TERRESTRIAL_COLOR,
        'domain-bg-color':TERRESTRIAL_BG_COLOR
                },
                {
        'chapter':4.14,
        'id':'ant-1',
        'name':'Anthropogenic Greenhouse Gas Emissions ', 
        'href':'/_4_14_AnthropogenicGreenhouseGasEmissions ',
        'icon-lg-src':'anthropogenic-ghg-fluxes.png',
        'icon-src':'ico-ant-ghg-fluxes.png',
        'icon-hover-src':'ico-ant-ghg-fluxes_hover.png',
        'domain':'Terrestrial',
        'subdomain':'',
        'scientific-area':'',
        'authors':'',
        'domain-color':TERRESTRIAL_COLOR,
        'domain-bg-color':TERRESTRIAL_BG_COLOR
                },

  
                ]