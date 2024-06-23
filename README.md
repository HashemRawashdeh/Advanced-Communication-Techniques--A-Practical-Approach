# Advanced Communication Techniques: A Practical Approach
This repository showcases a collection of advanced communication techniques, including AM communication, QAM modulation, and Huffman coding. Each short project demonstrates different aspects of digital and analog communication systems.

## Projects Overview
### GNU Radio AM Communication System Project Overview

#### Introduction
This section of the repository focuses on an AM (Amplitude Modulated) communication system designed using GNU Radio. The project demonstrates the effective transmission and demodulation of audio signals, highlighting the application of various signal processing techniques to maintain signal integrity and quality.

![System Flowgraph](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/AM_GNU%20Radio/SystemFlowgraph.png)

#### System Design and Key Parameters
- **Interpolation and Decimation**: The system employs an interpolation factor of 16 at the transmitter side to increase the sampling rate from the original 48 kHz of the input WAV file to 768 kHz. This upscaling is crucial for matching the higher sample rate required for the subsequent modulation and processing stages. Correspondingly, at the receiver, a decimation factor of 16 is used to bring the sample rate back down to 48 kHz, ensuring the output audio matches the original sampling characteristics.

- **Filtering Techniques**: 
  - **Band-pass Filter**: Customized with a low cutoff frequency of 1 kHz and a high cutoff frequency of 25 kHz, this filter is instrumental in limiting the bandwidth and removing unnecessary frequency components from the signal, which is critical for enhancing the quality of demodulation.
  - **Interpolating FIR Filter**: Utilizes taps defined in the taps block for precise filtering requirements during the interpolation process, aiding in the suppression of aliasing and preserving the integrity of the audio signal within the desired bandwidth.

#### Demonstrations
- **Short Demo**: A quick look at the key functionalities of the communication system:
  ![Short Demo GIF](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/AM_GNU%20Radio/ShortestPossibleDemo.gif)

- **Full Demonstration**: For a comprehensive demonstration, including detailed simulations with audio from diverse set of songs, and additional insights into system performance, visit the project's [YouTube video](https://www.youtube.com/watch?v=IMwchtWIwZs).
