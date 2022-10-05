# This is the map for LVL1

import os
import random

from levels.lvl_1.images_graph import *

#tile size

TILESIZE_L1 = 64

#the map

WORLD_MAP_L1 = [
    ["LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV",  "LTV", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LTV",  "LTV",  "PFT",  "PFT",  "PFT",  "LTV",  "LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",    "P", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LBV",  "LBV",  "PFT",  "PFT",  "PFT",  "LBV",  "LBV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LTV",  "LTV",  "PFT",  "PFT",  "PFT",  "LTV",  "LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LBV",  "LBV",  "PFT",  "PFT",  "PFT",  "LBV",  "LBV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LTV",  "LTV",  "PFT",  "PFT",  "PFT",  "LTV",  "LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LBV",  "LBV",  "PFT",  "PFT",  "PFT",  "LBV",  "LBV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LTV",  "LTV",  "PFT",  "PFT",  "PFT",  "LTV",  "LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LBV",  "LBV",  "PFT",  "PFT",  "PFT",  "LBV",  "LBV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LTV",  "LTV",  "PFT",  "PFT",  "PFT",  "LTV",  "LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LBV",  "LBV",  "PFT",  "PFT",  "PFT",  "LBV",  "LBV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LBV",  "PFT",  "PFT",  "PFT",  "LBV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",   "WC",  "PFT",  "PFT",  "PFT",   "WC",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT", "LTV"],
    ["LTV",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT", "LTV"],
    ["LTV",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",   "DC",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT", "LTV"],
    ["LTV",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT",  "PFT", "LTV"],
    ["LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",   "WC",  "PFT",  "PFT",  "PFT",   "WC",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT",  "LTV",  "LTV", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV",  "PFT",  "PFT",  "PFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT",  "LBV",  "LBV", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LTV",  "LTV",  "PFT",  "PFT",  "PFT",  "LTV",  "LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LBV",  "LBV",  "PFT",  "PFT",  "PFT",  "LBV",  "LBV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LTV",  "LTV",  "PFT",  "PFT",  "PFT",  "LTV",  "LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LBV",  "LBV",  "PFT",  "PFT",  "PFT",  "LBV",  "LBV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LTV",  "LTV",  "PFT",  "PFT",  "PFT",  "LTV",  "LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LBV",  "LBV",  "PFT",  "PFT",  "PFT",  "LBV",  "LBV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LTV",  "LTV",  "PFT",  "PFT",  "PFT",  "LTV",  "LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LBV",  "LBV",  "PFT",  "PFT",  "PFT",  "LBV",  "LBV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LTV",  "LTV",  "PFT",  "PFT",  "PFT",  "LTV",  "LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LBV",  "LBV",  "PFT",  "PFT",  "PFT",  "LBV",  "LBV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LTV",  "LTV",  "PFT",  "PFT",  "PFT",  "LTV",  "LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "LBV",  "LBV",  "PFT",  "PFT",  "PFT",  "LBV",  "LBV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LTV", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT",  "PFT",  "PFT",  "PFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "CPFT", "LTV"],
    ["LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV",  "LBV", "LBV"],
]


# ITEMS


GEMS = {
    1 : (enduri_coin(), "enduri_coin"),
    2 : (rahdul_coin(), "rahdul_coin"),
    3 : (sardul_coin(), "sardul_coin"),
    4 : (thrail_coin(), "thrail_coin")
}


# colours

blue = (0, 0, 255)
black = (0,0,0)

# generating the map -------------------------------------

blocks_coords = []
blocks_col_dec = [] 
respawn_point = []

# generating chests inventory ------------------------------

the_chests = {}

def stone_block_dis(screen, WORLD_MAP, TILESIZE, change_x, change_y):

    # FLOOR TILES
    stone_floor_tile = stone_floor()
    purple_floor_tile = purple_tile()
    clean_purple_floor_tile = clean_purple()
    

    # LAVA
    lava_floor_tile = lava_floor_1()
    lava_an_floor_tile_1 = lava_floor_2()
    lava_an_floor_tile_2 = lava_floor_3()

    # BORDERS -- COSTUM BLOCKS
    dark_stone = dark_stone_wall()
    light_tile_tv = top_view_light_tile()
    light_tile_bv = bottom_view_light_tile()

    # BORDERS - SET

    top_right_c = top_right_corner()
    bottom_right_c = bottom_right_corner()

    top_left_c = top_left_corner()
    bottom_left_c = bottom_left_corner()

    upward_wall_ = upward_wall()
    upward_left_wall_ = upward_left_wall()
    upward_right_wall_ = upward_right_wall()
    upsidedown_wall = upside_down_wall()

    # ----------- BLOCKS -------------- #

    #             CHESTS                #

    wooden_chest_dis = wooden_chest()
    diamond_chest_dis = diamond_chest()

    #          VALUES FOR CHESTS

    value_nr = 0

    for row_index, row in enumerate(WORLD_MAP):
           for col_index, col in enumerate(row):
               x = (col_index * TILESIZE) + change_x
               y = (row_index * TILESIZE) + change_y

               blocks_col_dec.append(pygame.Rect(x, y, 64, 64))

               # FLOOR TILES

               if col == 'B':
                  blocks_coords.append(['B', x, y])
                  respawn_point.append(['B', x, y])

                  screen.blit(dark_stone, (x, y))

               if col == 'F':
                   blocks_coords.append(['F', x, y])
                   respawn_point.append(['F', x, y])

                   screen.blit(stone_floor_tile, (x, y))
                
               if col == 'PFT':
                   blocks_coords.append(['PFT', x, y])
                   respawn_point.append(['PFT', x, y])

                   screen.blit(purple_floor_tile, (x, y))
               
               if col == 'CPFT' or col == 'P':
                   blocks_coords.append(['CPFT', x, y])
                   respawn_point.append(['CPFT', x, y])

                   screen.blit(clean_purple_floor_tile, (x, y))
                
               # BORDER #2

               if col == 'LTV':
                   blocks_coords.append(['LTV', x, y])
                   respawn_point.append(['LTV', x, y])

                   screen.blit(light_tile_tv, (x, y))
                
               if col == 'LBV':
                   blocks_coords.append(['LBV', x, y])
                   respawn_point.append(['LBV', x, y])

                   screen.blit(light_tile_bv, (x, y))
               
               # LIQUIDS -- TERRAIN
               
               if col == 'L':
                   blocks_coords.append(['L', x, y])
                   respawn_point.append(['L', x, y])

                   screen.blit(lava_floor_tile, (x, y))
               
               # BORDERS - SET -- ALL OF THESE ARE BORDERS, THUS COLLISION

               if col == 'TRC':
                   blocks_coords.append(['TRC', x, y])
                   respawn_point.append(['TRC', x, y])

                   screen.blit(top_right_c, (x, y))

               if col == 'BRC':
                   blocks_coords.append(['BRC', x, y])
                   respawn_point.append(['BRC', x, y])

                   screen.blit(bottom_right_c, (x, y))
                
               if col == 'TLC':
                   blocks_coords.append(['TLC', x, y])
                   respawn_point.append(['TLC', x, y])

                   screen.blit(top_left_c, (x, y))
               
               if col == 'BLC':
                   blocks_coords.append(['BLC', x, y])
                   respawn_point.append(['BLC', x, y])

                   screen.blit(bottom_left_c, (x, y))
               
               if col == 'UW':
                   blocks_coords.append(['UW', x, y])
                   respawn_point.append(['UW', x, y])

                   screen.blit(upward_wall_, (x, y))
                
               if col == 'ULW':
                   blocks_coords.append(['ULW', x, y])
                   respawn_point.append(['ULW', x, y])

                   screen.blit(upward_left_wall_, (x, y))
               
               if col == 'URW':
                   blocks_coords.append(['URW', x, y])
                   respawn_point.append(['URW', x, y])

                   screen.blit(upward_right_wall_, (x, y))
               
               if col == 'DW':
                   blocks_coords.append(['DW', x, y])
                   respawn_point.append(['DW', x, y])

                   screen.blit(upsidedown_wall, (x, y))

               #    -------  Blocks -------   #

               #             CHESTS           #

               if col == 'WC':

                   value_nr += 1

                   blocks_coords.append(['WC', x, y, value_nr])
                   respawn_point.append(['WC', x, y, value_nr])

                   file_name = str(value_nr) + '.txt'
                   path = 'levels/lvl_1/graphics/terrain/blocks/chests/chests_created'

                   with open(os.path.join(path, file_name), 'w') as f:
                       
                       # item id

                       item = random.randint(1, 4)
                       
                       f.write(str(item) + "\n")

                   with open(os.path.join(path, file_name), 'a+') as f:
                        
                        # number of items

                        f.seek(0)
                        nr_items = random.randint(1, 10)

                        f.write(str(nr_items) + "\n")

                        # position of items in the chests

                        f.seek(0)
                        position_items = random.randint(0, 60)

                        f.write(str(position_items) + "\n")

                   the_chests[(x, y)] = value_nr

                   screen.blit(wooden_chest_dis[0], (x, y))

               if col == 'DC':

                   value_nr += 1

                   blocks_coords.append(['DC', x, y, value_nr])
                   respawn_point.append(['DC', x, y, value_nr])

                   path = 'levels/lvl_1/graphics/terrain/blocks/chests/chests_created'

                   file_name = str(value_nr) + '.txt'

                  # item id

                   with open(os.path.join(path, file_name), 'w') as f:
                       
                       item = random.randint(1, 4)

                       f.write(str(item) + "\n")
                    
                   with open(os.path.join(path, file_name), 'a+') as f:

                       # number of items
                        
                        f.seek(0)
                        nr_items = random.randint(1, 10)

                        f.write(str(nr_items) + "\n")

                        # position of items in chests

                        f.seek(0)
                        position_items = random.randint(0, 60)

                        f.write(str(position_items) + "\n")

                   the_chests[(x, y)] = value_nr

                   screen.blit(diamond_chest_dis[0], (x, y))


# --- this is used to catch the initial coords of the player ---
def player_init_dis(screen, WORLD_MAP, TILESIZE):

    player1down = player_1_down()
    player1down = player1down[0]

    for row_index, row in enumerate(WORLD_MAP):
           for col_index, col in enumerate(row):
               x = col_index * TILESIZE + 38
               y = row_index * TILESIZE + 38

               if col == 'P':
                  screen.blit(player1down, (x, y))

                  return [x, y]

# player ----------------------------------------------

def player_dis(screen, x, y, state, ind):

    # old design (the spaceman)
    player = main_player()

    # new animation (not made by me)
    player1up = player_1_up()
    player1down = player_1_down()
    player1left = player_1_left()
    player1right = player_1_right()

    #idle states for the new character
    player1up_idle = player_1_up_idle()
    player1down_idle = player_1_down_idle()
    player1left_idle = player_1_left_idle()
    player1right_idle = player_1_right_idle()

    if state == 'a':
        screen.blit(player1left[ind], (x, y))

    elif state == 'aw':
        screen.blit(player1left[ind], (x, y))

    elif state == 'as':
        screen.blit(player1left[ind], (x, y))

    elif state == 'd':
        screen.blit(player1right[ind], (x, y))

    elif state == 'dw':
        screen.blit(player1right[ind], (x, y))

    elif state == 'ds':
        screen.blit(player1right[ind], (x, y))

    elif state == 'w':
        screen.blit(player1up[ind], (x, y))

    elif state == 's':
        screen.blit(player1down[ind], (x, y))
    
    elif state == 'n':
        screen.blit(player1down[0], (x, y))

# blocks ----------------------------------------------

def border_lim(poz, player_poz, block_poz):

    state = False

    for i, x in enumerate(poz):

        collide = pygame.Rect.colliderect(player_poz, block_poz[i])

        if collide and (x[0] == 'B'):
            state  = True

         # BORDERS - SET -- ALL OF THESE ARE BORDERS, THUS COLLISION

        if x[0] == 'TRC' and collide:
            state  = True

        if x[0] == 'BRC' and collide:
            state  = True

        if x[0] == 'TLC' and collide:
            state  = True

        if x[0] == 'BLC' and collide:
            state  = True

        if x[0] == 'UW' and collide:
            state  = True

        if x[0] == 'ULW' and collide:
            state  = True

        if x[0] == 'URW' and collide:
            state  = True

        if x[0] == 'DW' and collide:
            state  = True

        # WALLS #2

        if collide and (x[0] == 'LBV' or x[0] == 'LTV'):
            state = True

        # ---- BLOCKS ---- #
        #      CHESTS      #

        if collide and (x[0] == 'DC' or x[0] == 'WC'):
            state = True

    return state

#  -------  CHESTS ---------

def open_chest_mouse(poz, mouse_poz, chest_poz, the_chests):

    state = False
    which_chest = 0

    for i, x in enumerate(poz):

        collide = pygame.Rect.colliderect(mouse_poz, chest_poz[i])

        # ---- BLOCKS ---- #

        #      CHESTS      #

        if collide and (x[0] == 'DC' or x[0] == 'WC'):

            which_chest = x[3]

            state = True

    return [state, which_chest]


def player_chest_inter( mouse_poz, chest_id ):
    
    print(chest_id)


# ---------- MAPPING AROUND BLOCKS -----------

def map_around(screen, poz):

    # BORDERS - SET

    top_right_c = top_right_corner()
    bottom_right_c = bottom_right_corner()

    top_left_c = top_left_corner()
    bottom_left_c = bottom_left_corner()

    upward_wall_ = upward_wall()
    upward_left_wall_ = upward_left_wall()
    upward_right_wall_ = upward_right_wall()
    upsidedown_wall = upside_down_wall()

    # WALLS #2

    light_tile_tv = top_view_light_tile()
    light_tile_bv = bottom_view_light_tile()
    dark_stone = dark_stone_wall()

    for x in poz:

        if x[0] == 'B':
            screen.blit(dark_stone, (x[1], x[2]))
        
         # BORDERS - SET -- ALL OF THESE ARE BORDERS, THUS COLLISION

        if x[0] == 'TRC':
            screen.blit(top_right_c, (x[1], x[2]))

        if x[0] == 'BRC':
            screen.blit(bottom_right_c, (x[1], x[2]))

        if x[0] == 'TLC':
            screen.blit(top_left_c, (x[1], x[2]))
        
        if x[0] == 'BLC':
            screen.blit(bottom_left_c, (x[1], x[2]))
        
        if x[0] == 'UW':
            screen.blit(upward_wall_, (x[1], x[2]))
        
        if x[0] == 'ULW':
            screen.blit(upward_left_wall_, (x[1], x[2]))
        
        if x[0] == 'URW':
            screen.blit(upward_right_wall_, (x[1], x[2]))
        
        if x[0] == 'DW':
            screen.blit(upsidedown_wall, (x[1], x[2]))
        
        # WALLS #2

        if x[0] == 'LTV':
            screen.blit(light_tile_tv, (x[1], x[2]))
        
        if x[0] == 'LBV':
            screen.blit(light_tile_bv, (x[1], x[2]))

def map_around_floor(screen, poz):

    # LIQ Tiles
    lava_floor_tile = lava_floor_1()

    # Floor Tiles
    clean_purple_floor_tile = clean_purple()
    stone_floor_tile = stone_floor()
    purple_floor_tile = purple_tile()

    # ------ BLOCKS ------- #

    #        CHESTS         #

    wooden_chest_dis = wooden_chest()
    diamond_chest_dis = diamond_chest()

    for x in poz:

        # ----- FLOOR TILES ------ #

        if x[0] == 'F':
            screen.blit(stone_floor_tile, (x[1], x[2]))
        
        if x[0] == 'L':
            screen.blit(lava_floor_tile, (x[1], x[2]))
        
        if x[0] == 'CPFT':
            screen.blit(clean_purple_floor_tile, (x[1], x[2]))
        
        if x[0] == 'PFT':
            screen.blit(purple_floor_tile, (x[1], x[2]))
        
        # ---- BLOCKS ----- #

        #       CHESTS      #

        if x[0] == 'DC':
            screen.blit(diamond_chest_dis[0], (x[1], x[2]))

        if x[0] == 'WC':
            screen.blit(wooden_chest_dis[0], (x[1], x[2]))

# Health reduction collision dec

def lava_dm(poz, player_poz, block_poz):

    state = False

    for i, x in enumerate(poz):

        collide = pygame.Rect.colliderect(player_poz, block_poz[i])

        if collide and (x[0] == 'L'):
            state = True

    return state
