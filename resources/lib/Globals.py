#   Copyright (C) 2011 Jason Anderson
#
#
# This file is part of PseudoTV.
#
# PseudoTV is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PseudoTV is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PseudoTV.  If not, see <http://www.gnu.org/licenses/>.

import os
import xbmcaddon, xbmc, xbmcgui, xbmcvfs
import Settings

from FileAccess import FileLock

def log(msg, level = xbmc.LOGDEBUG):
    try:
        xbmc.log(ADDON_ID + '-' + ascii(msg), level)
    except:
        pass


def uni(string, encoding = 'utf-8'):
    if isinstance(string, basestring):
        if not isinstance(string, unicode):
           string = unicode(string, encoding)

	return string

def ascii(string):
    if isinstance(string, basestring):
        if isinstance(string, unicode):
           string = string.encode('ascii', 'ignore')

	return string

ADDON_ID = 'script.pseudotv'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_INFO = REAL_SETTINGS.getAddonInfo('path')

VERSION = REAL_SETTINGS.getAddonInfo('version')

TIMEOUT = 15 * 1000
PREP_CHANNEL_TIME = 60 * 60 * 24 * 5
NOTIFICATION_CHECK_TIME = 5
NOTIFICATION_TIME_BEFORE_END = 90
NOTIFICATION_DISPLAY_TIME = 8

MODE_RESUME = 1
MODE_ALWAYSPAUSE = 2
MODE_ORDERAIRDATE = 4
MODE_RANDOM = 8
MODE_REALTIME = 16
MODE_STARTMODES = MODE_RANDOM | MODE_REALTIME | MODE_RESUME

SETTINGS_LOC = REAL_SETTINGS.getAddonInfo('profile')
CHANNEL_SHARING = False
LOCK_LOC = xbmc.translatePath(os.path.join(SETTINGS_LOC, 'cache' + '/'))

if REAL_SETTINGS.getSetting('ChannelSharing') == "true":
    CHANNEL_SHARING = True
    LOCK_LOC = xbmc.translatePath(os.path.join(REAL_SETTINGS.getSetting('SettingsFolder'), 'cache' + '/'))

IMAGES_LOC = xbmc.translatePath(os.path.join(ADDON_INFO, 'resources', 'images' + '/'))
LOGOS_LOC = xbmc.translatePath(os.path.join(ADDON_INFO, 'resources', 'logos' + '/'))
CHANNELS_LOC = os.path.join(SETTINGS_LOC, 'cache' + '/')
GEN_CHAN_LOC = os.path.join(CHANNELS_LOC, 'generated' + '/')
MADE_CHAN_LOC = os.path.join(CHANNELS_LOC, 'stored' + '/')
CHANNELBUG_LOC = xbmc.translatePath(os.path.join(CHANNELS_LOC, 'ChannelBug' + '/'))

SHORT_CLIP_ENUM = [15,30,60,90,120,180,240,300,360]

MEDIA_LIMIT = {}
MEDIA_LIMIT['0'] = 10            
MEDIA_LIMIT['1'] = 25           
MEDIA_LIMIT['2'] = 50            
MEDIA_LIMIT['3'] = 100
MEDIA_LIMIT['4'] = 250
MEDIA_LIMIT['5'] = 500
MEDIA_LIMIT['6'] = 1000
MEDIA_LIMIT['7'] = 0

NUM_COLOUR = {}
NUM_COLOUR['0'] = '0xFFFF0000'        
NUM_COLOUR['1'] = '0xFF00FF00'           
NUM_COLOUR['2'] = '0xFF0000FF'            
NUM_COLOUR['3'] = '0xFFFFFF00'
NUM_COLOUR['4'] = '0xFF00FFFF'
NUM_COLOUR['5'] = '0xFFFFA500'
NUM_COLOUR['6'] = '0xFFFF00FF'
NUM_COLOUR['7'] = '0xFF808080'
NUM_COLOUR['8'] = '0xFFFFFFFF'

GlobalFileLock = FileLock()
ADDON_SETTINGS = Settings.Settings()

TIME_BAR = 'pstvTimeBar.png'
BUTTON_NO_FOCUS = 'pstvButtonNoFocus.png'

if xbmc.getSkinDir() == "skin.aeon.nox.5":
    if xbmc.getInfoLabel('Skin.CurrentTheme') == "green":
        BUTTON_FOCUS = 'pstvButtonFocusGreen.png'
    elif xbmc.getInfoLabel('Skin.CurrentTheme') == "red":          
        BUTTON_FOCUS = 'pstvButtonFocusRed.png'
    elif xbmc.getInfoLabel('Skin.CurrentTheme') == "orange":
        BUTTON_FOCUS = 'pstvButtonFocusOrange.png'
    else:        
        BUTTON_FOCUS = 'pstvButtonFocus.png'
else:
    BUTTON_FOCUS = 'pstvButtonFocus.png'

RULES_ACTION_START = 1
RULES_ACTION_JSON = 2
RULES_ACTION_LIST = 4
RULES_ACTION_BEFORE_CLEAR = 8
RULES_ACTION_BEFORE_TIME = 16
RULES_ACTION_FINAL_MADE = 32
RULES_ACTION_FINAL_LOADED = 64
RULES_ACTION_OVERLAY_SET_CHANNEL = 128
RULES_ACTION_OVERLAY_SET_CHANNEL_END = 256

# Maximum is 10 for this
RULES_PER_PAGE = 7

ACTION_MOVE_LEFT = 1
ACTION_MOVE_RIGHT = 2
ACTION_MOVE_UP = 3
ACTION_MOVE_DOWN = 4
ACTION_PAGEUP = 5
ACTION_PAGEDOWN = 6
ACTION_SELECT_ITEM = 7
ACTION_PREVIOUS_MENU = (9, 10, 92, 216, 247, 257, 275, 61467, 61448,)
ACTION_SHOW_INFO = 11
ACTION_STOP = 13
ACTION_OSD = 122
ACTION_NUMBER_0 = 58
ACTION_NUMBER_9 = 67
ACTION_INVALID = 999
