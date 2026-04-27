# Horizontal-to-Vertical Spectral Ratio

The Horizontal-to-Vertical Spectral Ratio (HVSR) method uses the Fourier spectra of horizontal and vertical components of seismic noise. It's widely applied to estimate the thickness of unconsolidated sediments above bedrock in sedimentary basins and to identify the site's fundamental frequency ($f_0$). This method requires only a single seismometer and a relatively short recording time, typically ranging from minutes to hours. HVSR, including derivative analyses such as the Rayleigh wave ellipticity curve, can be inverted to estimate the vertical S-wave velocity profile.

We will use Geopsy software for HVSR processing. The software can be downloaded [here](https://www.geopsy.org/download.php). Make sure to select the version that matches your operating system. Installation tutorials are also provided on the website.

## 1. Import Signals
After converting the raw recorded signals into MiniSEED format, we import the data into Geopsy. When you open Geopsy, a pop up window will appear. In this window, you can set the allocated memory for running the Geopsy software. In this example, about 12 GiB of memory is allocated. After setting the memory, click OK to close the pop up window.

![allocated_memory](./img/allocated_memory.png)

There are two ways to import signals into Geopsy: <br>
(a) open `File > Import Signals > File`, or <br>
(b) drag and drop the data directly from the file explorer.
![input_mseed](./img/input_mseed.png)

The imported files will appear in the `Files` tab in Geopsy. 

## 2. H/V Spectral Ratio
