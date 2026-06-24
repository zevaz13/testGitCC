# Hue Sensor Data Logger: Results and Data Description

## Overview

This document summarizes the structure, meaning, and interpretation of the data collected using the hue sensor data logger implemented in the `GRIDHUESENSOR_10JUN26` experiment. The logger captures raw color-channel measurements from the Adafruit TCS34725 hue sensor, along with experiment state variables and LED stimulus parameters for a grid search experiment.

The goal is to provide a clear reference for how the data are generated, what each field represents, and how the results should be interpreted in downstream analysis.

## Dataset structures
Each folder in /raw contains folders with particular experiments. Each file in there corresponds to one condition of the experiment, represented by the file title. flash vs solid, G vs GY... etc.

## Data Frame Structure

Each measurement cycle produces a single row in the serial data stream with the following fields:

| Field | Description |
|---|---|
| `trCnt` | Trial counter incremented once per stimulus presentation or baseline sample. |
| `hue_r` | Raw red-channel reading from the TCS34725 (unitless ADC count). |
| `hue_g` | Raw green-channel reading from the TCS34725 (unitless ADC count). |
| `hue_b` | Raw blue-channel reading from the TCS34725 (unitless ADC count). |
| `hue_c` | Clear-channel reading (overall light intensity). |
| `hue_colorTemp` | Computed correlated color temperature (Kelvin). |
| `hue_lux` | Computed illuminance (lux). |
| `currentYellow` | PWM intensity value for the yellow LED during the stimulus. |
| `currentRed` | PWM intensity value for the red LED. |
| `currentGreen` | PWM intensity value for the green LED. |
| `triggerFlag` | Indicates whether a stimulus is active (1) or baseline (0). |

## Sensor Measurement Characteristics

### Raw Channels (R, G, B, C)

- These values come directly from the TCS34725 ADC.
- They are proportional to the amount of light in each spectral band.
- Units are raw counts, not calibrated reflectance.
- Integration time: 101 ms
- Data reported every 110 ms
- Gain: 16x

### Derived Quantities

- **Color Temperature (K):** computed using the Adafruit library's internal algorithm.
- **Lux:** estimated illuminance based on the clear channel and RGB balance.

These derived values are stable for relative comparisons but should not be treated as absolute photometric measurements.

## Experiment Context

The `GRIDHUESENSOR_10JUN26` experiment cycles through a grid of LED stimuli defined by combinations of red and green intensities. For each stimulus:

- The hue sensor samples at a fixed timer interval (Timer3 at 110000 us).
- A baseline sample is taken before and after each stimulus. Denoted by trCnt > 999
- The trigger flag marks stimulus vs intertrial waits.

This structure allows computation of:

- Mean hue response per stimulus
- Baseline-corrected hue differences
- Sensor response surfaces across the red-green stimulus grid

## Typical Analysis Outputs

### 1. Mean Channel Values per Stimulus

For each of the 100 grid stimuli and each baseline, we compute:

- `meanHueR`
- `meanHueG`
- `meanHueB`

These represent the average sensor response during the stimulus window. For doing this, we take trig == 1 for each independent trCnt. We also discard the first and 3 samples of each stim when trigger ==1 

### 2. Baseline-Corrected Differences

For each channel:

```
deltaR = |R_stimulus - R_baseline|
deltaG = |G_stimulus - G_baseline|
deltaB = |B_stimulus - B_baseline|
```

This highlights how strongly each stimulus deviates from the baseline illumination.

### 3. Distance Metrics

A combined distance metric can be computed:

```
d = sqrt(deltaR^2 + deltaG^2 + deltaB^2)
```

This is useful for ranking stimuli by perceptual or sensor-space separation.

## Example Visualization

Common plots include:

- RGB response curves across stimulus index
- Baseline vs stimulus comparisons for each channel
- 2D heatmaps of sensor response across the red-green grid

These visualizations help identify:

- Regions of high sensitivity
- Nonlinearities in sensor response
- Potential saturation or clipping


## Summary

The hue data logger provides a rich, structured dataset capturing:

- Raw spectral information (R, G, B, C)
- Derived photometric quantities (lux, color temperature)
- Experiment state (trial count, trigger flag)
- Stimulus parameters (LED intensities)

This dataset supports detailed analysis of sensor behavior, stimulus discrimination, and response mapping across the stimulus grid.
