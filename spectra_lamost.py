'''
Sript to construct the Lamost spectra.
'''
from astroquery.simbad import Simbad
import astropy.coordinates as coord
import astropy.units as u
from astropy.io import ascii
from astropy.table import Table
from astropy.coordinates import SkyCoord 
from astroquery.sdss import SDSS
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import seaborn as sn
sn.set_context("poster")
import glob

def spectra(hduspectra):
    namefile = hduspectra.split("e/")[-1].split(".f")[0]
    hdu = fits.open(hduspectra)
    hdudata = hdu[0].data
    wl = hdudata[2]
    Flux = hdudata[0]
    n = np.linspace(1, len(wl), num=len(wl), dtype = int)

    fig, ax = plt.subplots(figsize=(11, 5))
    ax.set_title(namefile)
    ax.set(xlim=[3600,9000])
    #plt.ylim(ymin=0.0,ymax=500)
    ax.set(xlabel='Wavelength $(\AA)$')
    ax.set(ylabel='Flux')
    ax.plot(wl, Flux, linewidth=0.9, zorder=5)
    ax.axvline(6560.28, color='k', linewidth=0.5, linestyle='--', label=r"H$\alpha$")
    ax.axvline(5000.7, color='k', linewidth=0.5, linestyle='-', label="[O III]")
    ax.axvline(4686, color='r', linewidth=0.5, linestyle='-', label="He II")
    ax.axvline(7751, color='y', linewidth=0.4, linestyle='-.', label="[Ar III] 7751")
    ax.axvline(7135, color='k', linewidth=0.4, linestyle='-.', label="[Ar III] 7135")
    ax.legend()
    ra = hdu[0].header["RA"]
    dec = hdu[0].header["DEC"]
    print("Nome file:", namefile, "=>", "RA and DEC:", ra, dec)
