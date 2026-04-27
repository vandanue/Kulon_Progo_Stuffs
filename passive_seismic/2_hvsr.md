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
### 2.1. Opening the H/V tool box
Use H/V toolbox to computing HVSR. You can click and drag the signal into the `H/V Toolbox`.

![mseed_hv_tool](./img/mseed_hv_tool.png)

The H/V tool box is divided into three parts: the processing, windowing tabs, and H/V plot result. 

![open_hv](./img/open_hv.png)

In the "Processing" tab, you can set the parameters for process the H/V computation (window length, the smoothing function, the frequency range, etc ...). In the "Windowing" tab you have several tools to define the windows selection.

### 2.2. Windowing

The three seismic components, north-south (NS), east-west (EW), and vertical (V), are commonly divided into several time windows. Each window should be at least 10 times longer than the estimated fundamental site period, or longer than 10/$f_0$, as recommended by SESAME ([2004](https://sesame.geopsy.org/Delivrables/Del-D23-HV_User_Guidelines.pdf)). For example, if the estimated fundamental frequency is 3 Hz (period ≈ 0.3 s), the recommended window length is about at least 30 s. HVSR curves are computed as the ratio of the Fourier amplitude spectra of the horizontal and vertical components within each time window. Therefore, it is important to select the most stationary signals and avoid transient signals that are commonly associated with specific sources such as footsteps or nearby traffic.

- Window length: 30 s (or at least 30 - 50 s)
- Overlap: 5%

![window](./img/window.png)

In Geopsy, windowing can be performed automatically using the STA/LTA algorithm. This algorithm works in contrast to the commonly used trigger algorithm in seismology, and is therefore referred to as an anti-trigger method. In this case, the goal is to select time windows that do not contain energetic transients. This condition is achieved when the STA/LTA ratio remains below a small threshold value, called the "max STA/LTA" (typically around 1.5 to 2), over a sufficient duration. At the same time, windows with anomalously low amplitudes should also be avoided. For this reason, a minimum threshold called "min STA/LTA" is introduced, which should not be reached during the selected noise window. The program automatically searches for time windows that satisfy these criteria, and once one window is selected, the program continues to search for the next valid window.

![sta_lta](./img/sta_lta.png)

### 2.3. Processing parameters
After selecting the appropriate time windows, the HVSR value is calculated from the horizontal and vertical spectral amplitudes within each window. In this study, the horizontal component is represented using the quadratic mean/squared average of the NS and EW components, which is expressed as:

$$
HVSR = \frac{\sqrt{(NS^2 + EW^2)/2}}{V}
$$

