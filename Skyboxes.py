import string

from module_info import *

from process_common import *
#from process_operations import *

sf_day        = 0x00000000
sf_dawn       = 0x00000001
sf_night      = 0x00000002
sf_mask      = 0x00000003

sf_clouds_0   = 0x00000000
sf_clouds_1   = 0x00000010
sf_clouds_2   = 0x00000020
sf_clouds_3   = 0x00000030

sf_no_shadows = 0x10000000
sf_HDR        = 0x20000000  # this will generate HDR-shaded skyboxes, you should make a LDR version of your skybox for compatibility

# mesh_name, flags, sun_heading, sun_altitude, flare_strength, postfx, sun_color, hemi_color, ambient_color, (fog_start, fog_color),

# to generate new skybox textures with hdr option:
# hdr images are required to generate our RGBE coded skybox images


# To add a skybox, you should first edit this file and put new skyboxes.txt file into the "Data/" folder of your module. 
# The first "mesh_name" parameter is the name of the skybox mesh to be used for that entry. 
# You can check our meshes from the "skyboxes.brf" file with OpenBRF and copy them, 
# just replace the material's textures with yours. And you will also have to change the 
# specular color parameters for correct hdr rendering. of course specular color does not 
# corresponds to specular lighting, those parameters are used as compression values 
# for RGBE decoding and should be generated while you generate RGBE textures. 
# (specular.red = Scale component, specular.green = Bias component) 
# You can check our materials for the instances of this usage. 
#
# For skybox textures, we are using uncompressed *.hdr files to generate *_rgb.dds and *_exp.dds files. 
# its just a RGBE encoding of the skybox for hdr lighting. here is an example: 
# "skybox.dds" -> simple non-hdr (LDR) image, used when you dont use hdr (DXT1 format is good)
# "skybox_rgb.dds" -> RGB components of the HDR image (DXT1 format is preffered)
# "skybox_exp.dds" -> E (exponent) component of the HDR image (L16 format is good, you can use half resolution for this texture)
# We are using our own command line tool to generete those files from "skybox.hdr" image. 
# But you can generate them with some of the hdr-image editors too. The images should be gamma corrected and should not have mipmaps. 
# You can use Photoshop with DDS plug-ins or DirectX Texture Viewer to see the contents of our dds images. 
# 
# ..visit Taleworlds Forums for more information..


#     mesh_name          flags,      heading, altitude, flare, postfx,           sun_color,             hemi_color,           ambient_color,        (fog_start, fog_color),
skyboxes = [
## First skybox is used for world map ##
### mordor clouds - ("sky_day_3d",   sf_day|sf_clouds_0,   0.0, 56.0, 1.0, "pfx_sunny",    (140.0/62,160.0/62,100.0/62), (0.0, 0.0, 0.0), (020.0/255,030.0/255,050.0/255), (100, 0xFF8CA2AD)),#
### heavy clouds, sun small spot - ("sky_day_3b",   sf_day|sf_clouds_0,   0.0, 56.0, 1.0, "pfx_sunny",    (140.0/62,160.0/62,100.0/62), (0.0, 0.0, 0.0), (020.0/255,030.0/255,050.0/255), (100, 0xFF8CA2AD)),#
### cloudy + sun nice blue - ("sky_day_1b",   sf_day|sf_clouds_0,   0.0, 56.0, 1.0, "pfx_sunny",    (140.0/62,160.0/62,100.0/62), (0.0, 0.0, 0.0), (020.0/255,030.0/255,050.0/255), (100, 0xFF8CA2AD)),#
### night and rainbow rays - ("sky_night_1a",   sf_day|sf_clouds_0,   0.0, 56.0, 1.0, "pfx_sunny",    (140.0/62,160.0/62,100.0/62), (0.0, 0.0, 0.0), (020.0/255,030.0/255,050.0/255), (100, 0xFF8CA2AD)),#
  ("sky_day_0c",   sf_day|sf_clouds_0,   0.0, 56.0, 1.0, "pfx_sunny",    (140.0/62,160.0/62,100.0/62), (0.0, 0.0, 0.0), (020.0/255,030.0/255,050.0/255), (100, 0xFF8CA2AD)),#
## First skybox is used for world map ##

  ("sky_day_0a",   sf_day|sf_clouds_0,   0.0, 56.0, 1.0, "pfx_sunny",    (140.0/62,160.0/62,100.0/62), (0.0, 0.0, 0.0), (020.0/255,030.0/255,050.0/255), (100, 0xFF8CA2AD)),#
  ("sky_day_0b",   sf_day|sf_clouds_0,   0.0, 42.0, 0.7, "pfx_sunny",    (240.0/62,220.0/62,110.0/62), (0.0, 0.0, 0.0), (040.0/255,060.0/255,100.0/255), (100, 0xFF8CA2AD)),#
  ("sky_day_0c",   sf_day|sf_clouds_0,   0.0, 55.0, 1.0, "pfx_sunny",    (204.0/62,202.0/62,115.0/62), (0.0, 0.0, 0.0), (010.0/255,035.0/255,070.0/255), (100, 0xFF8CA2AD)),#

  ("sky_day_1a",   sf_day|sf_clouds_1,   0.0, 44.0, 1.0, "pfx_sunny",    (170.0/62,140.0/62,090.0/62), (0.0, 0.0, 0.0), (030.0/255,050.0/255,050.0/255), (100, 0xFF7B94A2)),#
  ("sky_day_1b",   sf_day|sf_clouds_1,   0.0, 48.0, 1.0, "pfx_sunny",    (204.0/62,202.0/62,115.0/62), (0.0, 0.0, 0.0), (020.0/255,035.0/255,045.0/255), (100, 0xFF8CA2AD)),#
  ("sky_day_1c",   sf_day|sf_clouds_1,   0.0, 55.0, 0.7, "pfx_sunny",    (216.0/62,185.0/62,117.0/62), (0.0, 0.0, 0.0), (091.0/255,105.0/255,115.0/255), (100, 0xFF8CA2AD)),#
  ("sky_day_1d",   sf_day|sf_clouds_1,   0.0, 58.0, 1.0, "pfx_sunny",    (190.0/62,170.0/62,130.0/62), (0.0, 0.0, 0.0), (015.0/255,030.0/255,040.0/255), (100, 0xFF52849E)),#

  ("sky_day_2a",   sf_day|sf_clouds_2,   0.0, 42.5, 0.5, "pfx_cloudy",   (170.0/62,150.0/62,100.0/62), (0.0, 0.0, 0.0), (020.0/255,030.0/255,035.0/255), (005, 0xFF78828C)),#
  ("sky_day_2b",   sf_day|sf_clouds_2,   0.0, 35.0, 0.4, "pfx_cloudy",   (100.0/62,090.0/62,070.0/62), (0.0, 0.0, 0.0), (040.0/255,040.0/255,040.0/255), (050, 0xFF9BA087)),#
  ("sky_day_2c",   sf_day|sf_clouds_2,   0.0, 30.0, 0.9, "pfx_cloudy",   (200.0/62,175.0/62,150.0/62), (0.0, 0.0, 0.0), (020.0/255,025.0/255,030.0/255), (300, 0xFF6E7882)),#
  ("sky_day_2d",   sf_day|sf_clouds_2,   0.0, 32.5, 0.3, "pfx_cloudy",   (160.0/62,140.0/62,110.0/62), (0.0, 0.0, 0.0), (015.0/255,020.0/255,030.0/255), (900, 0xFF8CA2AD)),#

  ("sky_day_3a",   sf_day|sf_clouds_3,   0.0, 17.0, 0.3, "pfx_overcast", (090.0/62,115.0/62,115.0/62), (0.0, 0.0, 0.0), (010.0/255,030.0/255,030.0/255), (300, 0xFF3C4646)),#
  ("sky_day_3b",   sf_day|sf_clouds_3,   0.0, 42.5, 0.2, "pfx_overcast", (070.0/62,110.0/62,130.0/62), (0.0, 0.0, 0.0), (008.0/255,035.0/255,084.0/255), (300, 0xFF788C96)),#
  ("sky_day_3c",   sf_day|sf_clouds_3,   0.0, 70.0, 0.0, "pfx_overcast", (090.0/62,110.0/62,110.0/62), (0.0, 0.0, 0.0), (008.0/255,008.0/255,008.0/255), (300, 0xFF464646)),#
  ("sky_day_3d",   sf_day|sf_clouds_3,   0.0, 80.0, 0.0, "pfx_overcast", (180.0/62,170.0/62,150.0/62), (0.0, 0.0, 0.0), (025.0/255,030.0/255,030.0/255), (300, 0xFF8C8778)),#
  ("sky_day_4a",   sf_day|sf_clouds_3,   0.0, 80.0, 0.0, "pfx_overcast", (180.0/62,170.0/62,150.0/62), (0.0, 0.0, 0.0), (025.0/255,030.0/255,030.0/255), (300, 0xFF8C8778)),#
  ("sky_day_4b",   sf_day|sf_clouds_3,   0.0, 80.0, 0.0, "pfx_overcast", (090.0/62,115.0/62,115.0/62), (0.0, 0.0, 0.0), (010.0/255,030.0/255,030.0/255), (300, 0xFF3C4646)),#
   
  
  ("sky_night_0a", sf_night|sf_clouds_0, 0.0, 35.0, 0.2, "pfx_night",    (000.0/62,010.0/62,040.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#
  ("sky_night_1a", sf_night|sf_clouds_1, 0.0, 35.0, 0.2, "pfx_night",    (000.0/62,008.0/62,030.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#
  ("sky_night_2a", sf_night|sf_clouds_2, 0.0, 51.0, 0.3, "pfx_night",    (001.0/62,003.0/62,007.0/62), (0.0, 0.0, 0.0), (000.0/255,001.0/255,004.0/255), (400, 0xFF00040A)),#
  ("sky_night_1a", sf_night|sf_clouds_3, 0.0, 51.0, 0.1, "pfx_night",    (000.0/62,005.0/62,015.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#
  ("sky_night_3b", sf_night|sf_clouds_3, 0.0, 40.0, 0.1, "pfx_night",    (000.0/62,005.0/62,015.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#
  ("sky_night_3c",  sf_dawn|sf_clouds_3,  0.0, 05, 0.3,  "pfx_night",   (150.0/62,035.0/62,008.0/62), (0.0, 0.0, 0.0), (005.0/255,005.0/255,005.0/255), (50, 0xFF5B3C3E)),#

  ("sky_dawn_0a",  sf_dawn|sf_clouds_0,  0.0, 04, 0.6,   "pfx_sunset",   (150.0/62,020.0/62,000.0/62), (0.0, 0.0, 0.0), (020.0/255,010.0/255,025.0/255), (50, 0xFF5B3C3E)),#
  ("sky_dawn_0b",  sf_dawn|sf_clouds_0,  0.0, 05, 0.6,   "pfx_sunset",   (240.0/62,090.0/62,040.0/62), (0.0, 0.0, 0.0), (035.0/255,015.0/255,040.0/255), (50, 0xFF5B3C3E)),#
  ("sky_dawn_1a",  sf_dawn|sf_clouds_1,  0.0, 10, 0.3,   "pfx_sunset",   (215.0/62,070.0/62,006.0/62), (0.0, 0.0, 0.0), (018.0/255,025.0/255,045.0/255), (50, 0xFF5D5B65)),#
  ("sky_dawn_1b",  sf_dawn|sf_clouds_1,  0.0, 24, 0.9,   "pfx_sunset",   (130.0/62,035.0/62,010.0/62), (0.0, 0.0, 0.0), (018.0/255,012.0/255,021.0/255), (50, 0xFF462323)),#
  ("sky_dawn_2a",  sf_dawn|sf_clouds_2,  0.0, 10, 0.1,   "pfx_sunset",   (172.0/62,059.0/62,026.0/62), (0.0, 0.0, 0.0), (037.0/255,018.0/255,047.0/255), (50, 0xFF5B3C3E)),#	
  ("sky_dawn_3a",  sf_dawn|sf_clouds_3,  0.0, 07, 0.1,   "pfx_sunset",   (080.0/62,020.0/62,000.0/62), (0.0, 0.0, 0.0), (010.0/255,005.0/255,005.0/255), (50, 0xFFA08C5F)),#
  ("sky_dawn_3b",  sf_dawn|sf_clouds_3,  0.0, 05, 0.3,   "pfx_sunset",   (150.0/62,035.0/62,008.0/62), (0.0, 0.0, 0.0), (005.0/255,005.0/255,005.0/255), (50, 0xFF5B3C3E)),#
  #("sky_dawn_3c",  sf_dawn|sf_clouds_3,  0.0, 05, 0.3,   "pfx_sunset",   (150.0/62,035.0/62,008.0/62), (0.0, 0.0, 0.0), (005.0/255,005.0/255,005.0/255), (50, 0xFF5B3C3E)),#

  
  ("cult_dawn_1a",   sf_day|sf_mask|sf_clouds_3,   0.0, 80.0, 0.0, "pfx_overcast", (180.0/62,170.0/62,150.0/62), (0.0, 0.0, 0.0), (025.0/255,030.0/255,030.0/255), (300, 0xFF8c4940)),#
  ("cult_night_1a",  sf_night|sf_mask|sf_clouds_0, 0.0, 35.0, 0.2, "pfx_night",    (000.0/62,010.0/62,040.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF8c2a1d)),#
  ("cult_day_1a",    sf_day|sf_mask|sf_clouds_1,   0.0, 48.0, 1.0, "pfx_sunny",    (204.0/62,202.0/62,115.0/62), (0.0, 0.0, 0.0), (020.0/255,035.0/255,045.0/255), (100, 0xFF8CA2AD)),#
#############################################################HDR-copy#############################################################################################################
## First skybox is used for world map ##
  ("sky_day_0c",   sf_day|sf_clouds_0|sf_HDR,   0.0, 56.0, 1.0, "pfx_sunny",    (140.0/62,160.0/62,100.0/62), (0.0, 0.0, 0.0), (020.0/255,030.0/255,050.0/255), (100, 0xFF8CA2AD)),#
## First skybox is used for world map ##

  ("sky_day_0a",   sf_day|sf_clouds_0|sf_HDR,   0.0, 56.0, 1.0, "pfx_sunny",    (140.0/62,160.0/62,100.0/62), (0.0, 0.0, 0.0), (020.0/255,030.0/255,050.0/255), (100, 0xFF8CA2AD)),#
  ("sky_day_0b",   sf_day|sf_clouds_0|sf_HDR,   0.0, 42.0, 0.7, "pfx_sunny",    (240.0/62,220.0/62,110.0/62), (0.0, 0.0, 0.0), (040.0/255,060.0/255,100.0/255), (100, 0xFF8CA2AD)),#
  ("sky_day_0c",   sf_day|sf_clouds_0|sf_HDR,   0.0, 55.0, 1.0, "pfx_sunny",    (204.0/62,202.0/62,115.0/62), (0.0, 0.0, 0.0), (010.0/255,035.0/255,070.0/255), (100, 0xFF8CA2AD)),#

  ("sky_day_1a",   sf_day|sf_clouds_1|sf_HDR,   0.0, 44.0, 1.0, "pfx_sunny",    (170.0/62,140.0/62,090.0/62), (0.0, 0.0, 0.0), (030.0/255,050.0/255,050.0/255), (000, 0xFF7B94A2)),#
  ("sky_day_1b",   sf_day|sf_clouds_1|sf_HDR,   0.0, 48.0, 1.0, "pfx_sunny",    (204.0/62,202.0/62,115.0/62), (0.0, 0.0, 0.0), (020.0/255,035.0/255,045.0/255), (100, 0xFF8CA2AD)),#
  ("sky_day_1c",   sf_day|sf_clouds_1|sf_HDR,   0.0, 55.0, 0.7, "pfx_sunny",    (216.0/62,185.0/62,117.0/62), (0.0, 0.0, 0.0), (091.0/255,105.0/255,115.0/255), (400, 0xFF8CA2AD)),#
  ("sky_day_1d",   sf_day|sf_clouds_1|sf_HDR,   0.0, 58.0, 1.0, "pfx_sunny",    (190.0/62,170.0/62,130.0/62), (0.0, 0.0, 0.0), (015.0/255,030.0/255,040.0/255), (999, 0xFF52849E)),#

  ("sky_day_2a",   sf_day|sf_clouds_2|sf_HDR,   0.0, 42.5, 0.5, "pfx_cloudy",   (170.0/62,150.0/62,100.0/62), (0.0, 0.0, 0.0), (020.0/255,030.0/255,035.0/255), (005, 0xFF78828C)),#
  ("sky_day_2b",   sf_day|sf_clouds_2|sf_HDR,   0.0, 35.0, 0.4, "pfx_cloudy",   (100.0/62,090.0/62,070.0/62), (0.0, 0.0, 0.0), (040.0/255,040.0/255,040.0/255), (050, 0xFF9BA087)),#
  ("sky_day_2c",   sf_day|sf_clouds_2|sf_HDR,   0.0, 30.0, 0.9, "pfx_cloudy",   (200.0/62,175.0/62,150.0/62), (0.0, 0.0, 0.0), (020.0/255,025.0/255,030.0/255), (300, 0xFF6E7882)),#
  ("sky_day_2d",   sf_day|sf_clouds_2|sf_HDR,   0.0, 32.5, 0.3, "pfx_cloudy",   (160.0/62,140.0/62,110.0/62), (0.0, 0.0, 0.0), (015.0/255,020.0/255,030.0/255), (900, 0xFF8CA2AD)),#

  ("sky_day_3a",   sf_day|sf_clouds_3|sf_HDR,   0.0, 17.0, 0.3, "pfx_overcast", (090.0/62,115.0/62,115.0/62), (0.0, 0.0, 0.0), (010.0/255,030.0/255,030.0/255), (300, 0xFF3C4646)),#
  ("sky_day_3b",   sf_day|sf_clouds_3|sf_HDR,   0.0, 42.5, 0.2, "pfx_overcast", (070.0/62,110.0/62,130.0/62), (0.0, 0.0, 0.0), (008.0/255,035.0/255,084.0/255), (300, 0xFF788C96)),#
  ("sky_day_3c",   sf_day|sf_clouds_3|sf_HDR,   0.0, 70.0, 0.0, "pfx_overcast", (090.0/62,110.0/62,110.0/62), (0.0, 0.0, 0.0), (008.0/255,008.0/255,008.0/255), (300, 0xFF464646)),#
  ("sky_day_3d",   sf_day|sf_clouds_3|sf_HDR,   0.0, 80.0, 0.0, "pfx_overcast", (180.0/62,170.0/62,150.0/62), (0.0, 0.0, 0.0), (025.0/255,030.0/255,030.0/255), (300, 0xFF8C8778)),#
  ("sky_day_4a",   sf_day|sf_clouds_3|sf_HDR,   0.0, 80.0, 0.0, "pfx_overcast", (180.0/62,170.0/62,150.0/62), (0.0, 0.0, 0.0), (025.0/255,030.0/255,030.0/255), (300, 0xFF8C8778)),#
  ("sky_day_4b",   sf_day|sf_clouds_3|sf_HDR,   0.0, 17.0, 0.3, "pfx_overcast", (090.0/62,115.0/62,115.0/62), (0.0, 0.0, 0.0), (010.0/255,030.0/255,030.0/255), (300, 0xFF3C4646)),#

  
  ("sky_night_0a", sf_night|sf_clouds_0|sf_HDR, 0.0, 35.0, 0.2, "pfx_night",    (000.0/62,010.0/62,040.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#
  ("sky_night_1a", sf_night|sf_clouds_1|sf_HDR, 0.0, 35.0, 0.2, "pfx_night",    (000.0/62,008.0/62,030.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#
  ("sky_night_2a", sf_night|sf_clouds_2|sf_HDR, 0.0, 51.0, 0.3, "pfx_night",    (001.0/62,003.0/62,007.0/62), (0.0, 0.0, 0.0), (000.0/255,001.0/255,004.0/255), (400, 0xFF00040A)),#
  ("sky_night_1a", sf_night|sf_clouds_3|sf_HDR, 0.0, 51.0, 0.1, "pfx_night",    (000.0/62,005.0/62,015.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#
  ("sky_night_3b", sf_night|sf_clouds_3|sf_HDR, 0.0, 40.0, 0.1, "pfx_night",    (000.0/62,005.0/62,015.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#
  ("sky_night_3c", sf_night|sf_clouds_3|sf_HDR, 0.0, 40.0, 0.1, "pfx_night",    (000.0/62,005.0/62,015.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#

  ("sky_dawn_0a",  sf_dawn|sf_clouds_0|sf_HDR,  0.0, 4, 0.6,    "pfx_sunset",   (150.0/62,020.0/62,000.0/62), (0.0, 0.0, 0.0), (020.0/255,010.0/255,025.0/255), (50, 0xFF5B3C3E)),#
  ("sky_dawn_0b",  sf_dawn|sf_clouds_0|sf_HDR,  0.0, 5, 0.6,    "pfx_sunset",   (240.0/62,090.0/62,040.0/62), (0.0, 0.0, 0.0), (035.0/255,015.0/255,040.0/255), (50, 0xFF5B3C3E)),#
  ("sky_dawn_1a",  sf_dawn|sf_clouds_1|sf_HDR,  0.0, 10, 0.3,   "pfx_sunset",   (215.0/62,070.0/62,006.0/62), (0.0, 0.0, 0.0), (018.0/255,025.0/255,045.0/255), (50, 0xFF5D5B65)),#
  ("sky_dawn_1b",  sf_dawn|sf_clouds_1|sf_HDR,  0.0, 24, 0.9,   "pfx_sunset",   (130.0/62,035.0/62,010.0/62), (0.0, 0.0, 0.0), (018.0/255,012.0/255,021.0/255), (50, 0xFF462323)),#
  ("sky_dawn_2a",  sf_dawn|sf_clouds_2|sf_HDR,  0.0, 10, 0.1,   "pfx_sunset",   (172.0/62,059.0/62,026.0/62), (0.0, 0.0, 0.0), (037.0/255,018.0/255,047.0/255), (50, 0xFF5B3C3E)),#	
  ("sky_dawn_3a",  sf_dawn|sf_clouds_3|sf_HDR,  0.0, 7, 0.1,    "pfx_sunset",   (080.0/62,020.0/62,000.0/62), (0.0, 0.0, 0.0), (010.0/255,005.0/255,005.0/255), (50, 0xFFA08C5F)),#
  ("sky_dawn_3b",  sf_dawn|sf_clouds_3|sf_HDR,  0.0, 5, 0.3,    "pfx_sunset",   (150.0/62,035.0/62,008.0/62), (0.0, 0.0, 0.0), (005.0/255,005.0/255,005.0/255), (50, 0xFF5B3C3E)),#
  #("sky_dawn_3c",  sf_dawn|sf_clouds_3|sf_HDR,  0.0, 5, 0.3,    "pfx_sunset",   (150.0/62,035.0/62,008.0/62), (0.0, 0.0, 0.0), (005.0/255,005.0/255,005.0/255), (50, 0xFF5B3C3E)),#

  ("cult_dawn_1a",   sf_day|sf_HDR,   0.0, 80.0, 0.0, "pfx_overcast", (180.0/62,170.0/62,150.0/62), (0.0, 0.0, 0.0), (025.0/255,030.0/255,030.0/255), (300, 0xFF8c4940)),#
  ("cult_night_1a",  sf_night|sf_HDR, 0.0, 35.0, 0.2, "pfx_night",    (000.0/62,010.0/62,040.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF8c2a1d)),#
  ("cult_day_1a",    sf_day|sf_HDR,   0.0, 48.0, 1.0, "pfx_sunny",    (204.0/62,202.0/62,115.0/62), (0.0, 0.0, 0.0), (020.0/255,035.0/255,045.0/255), (100, 0xFF8CA2AD)),#
]



def save_python_header():
  file = open("./ID_skyboxes.py","w")
  for i_item in xrange(len(skyboxes)):
    file.write("sky_%s = %d\n"%(convert_to_identifier(skyboxes[i_item][0]),i_item))
  file.close()

def save_skyboxes():
  file = open(export_dir + "/data/skyboxes.txt","w")
  file.write("%d\n"%len(skyboxes))
  for skybox in  skyboxes:
    file.write("%s %d %f %f %f %s\n"%(skybox[0],skybox[1],skybox[2],skybox[3],skybox[4],skybox[5]))
    file.write(" %f %f %f "%skybox[6])
    file.write(" %f %f %f "%skybox[7])
    file.write(" %f %f %f "%skybox[8])
    file.write(" %f %d\n"%skybox[9])
  file.close()

print "Exporting skyboxes..."
save_python_header()
save_skyboxes()
