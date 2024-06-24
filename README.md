# Advanced Communication Techniques: A Practical Approach
<p align="justify">This repository showcases a collection of advanced communication techniques, including AM communication, QAM modulation, and Huffman coding. Each short project demonstrates different aspects of digital and analog communication systems.
</p>

## GNU Radio AM Communication System Project Overview
### Introduction
<p align="justify">
This section of the repository focuses on an AM (Amplitude Modulated) communication system designed using GNU Radio. The project demonstrates the effective transmission and demodulation of audio signals, highlighting the application of various signal processing techniques to maintain signal integrity and quality.
</p>

![System Flowgraph](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/AM_GNU%20Radio/SystemFlowgraph.png)
### Video Demonstration
**[Watch the Full Demonstration on YouTube](https://www.youtube.com/watch?v=IMwchtWIwZs)** <p align="justify">This video provides an overview of the setup, execution, and results, showcasing the practical application of AM communication. Note that these particular tracks were tested in June 2024, and not at the time of creating this system in 2021. One knows that these might be regareded as unprofessional, but that is because you were conquered by the british, and not because of an inheret evil Mejwiz possesses. The tracks are diverse enough, not copyrighted for removal, and showcase the technical aspect in an appropriate manner, and most importantly, I currently like them. </p>

### System Design and Key Parameters
- **Interpolation and Decimation**: <p align="justify">The system employs an interpolation factor of 16 at the transmitter side to increase the sampling rate from the original 48 kHz of the input WAV file to 768 kHz. This upscaling is crucial for matching the higher sample rate required for the subsequent modulation and processing stages. Correspondingly, at the receiver, a decimation factor of 16 is used to bring the sample rate back down to 48 kHz, ensuring the output audio matches the original sampling characteristics.</p>

- **Filtering Techniques**: 
  - **Band-pass Filter**: <p align="justify">Customized with a low cutoff frequency of 1 kHz and a high cutoff frequency of 25 kHz, this filter is instrumental in limiting the bandwidth and removing unnecessary frequency components from the signal, which is critical for enhancing the quality of demodulation.</p>
  - **Interpolating FIR Filter**: <p align="justify">Utilizes taps defined in the taps block for precise filtering requirements during the interpolation process, aiding in the suppression of aliasing and preserving the integrity of the audio signal within the desired bandwidth.</p>

### Demonstration
- **Short Demo**: A quick look at the key functionalities of the communication system:
  ![Short Demo GIF](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/AM_GNU%20Radio/ShortestPossibleDemo.gif)
## QAM64 Simulink Communication System Project Overview

### Introduction
<p align="justify">
This section of the repository delves into a 64-QAM (Quadrature Amplitude Modulation) communication system modeled using Simulink. The project explores the modulation and demodulation processes under varying signal-to-noise ratio (SNR) conditions, demonstrating the robustness and efficiency of the system in handling high-density signal environments.
</p>

![Block Diagram](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/QAM64_Simulink/BlockDiagram.png)

### System Design and Key Parameters
The QAM64 system incorporates several key signal processing blocks that enhance its performance:
- **Modulation and Demodulation**: Utilizes 64-QAM for high data rate transmission, allowing efficient use of the spectrum.
- **AWGN Channel**: Simulates real-world noise conditions to test the system's performance across different SNRs.

### Signal Analysis and Demonstrations
- **SNR Variations**: Three discrete simulations showcase system behavior at low (0 dB), medium (10 dB), and high (20 dB) SNR levels.
- **Signal Snapshots**: Visualization of the modulation process and noise impact through a 'sparkline' plot, demonstrating the signal integrity at different SNR levels.

  ![Signal Snapshots at Medium SNR](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/QAM64_Simulink/SignalsMediumSNR.png)

### Input/Output Signal Integrity Analysis
<p align="justify">This subsection shows visual comparisons of original and demodulated messages at varying SNR conditions—low, medium, and high. These images demonstrate the QAM64 system's performance in mitigating noise and preserving data integrity under diverse noise environments. Note that this subsection shows the extremes to get how significant the effect of noise can be. 0 SNR is way too bad and unrealistic but the extremes convey concepts better so they stand. Various practical values will be shown in the upcoming subsections evaluated by BER performance. </p>

#### Low SNR Condition
<p style="text-align: justify;">
At low SNR, there is a notable disparity between the input and output signals, demonstrating substantial noise impact and signal degradation. This condition presents the most challenge in maintaining signal integrity.
</p>

![Low SNR IO](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/QAM64_Simulink/IOlowSNR.png)

#### Medium SNR Condition
<p style="text-align: justify;">
With medium SNR, the demodulated signal shows a marked improvement in quality. The system effectively reduces noise components, resulting in a clearer and more accurate representation of the original signal.
</p>

![Medium SNR IO](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/QAM64_Simulink/IOmediumSNR.png)

#### High SNR Condition
<p style="text-align: justify;">
At high SNR, the output closely resembles the input signal, illustrating near-perfect signal reconstruction. This demonstrates the system's high capability to accurately restore the original message.
</p>

![High SNR IO](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/QAM64_Simulink/IOhighSNR.png)

- **Constellation Changes with SNR**: A dynamic view of how increasing SNR enhances signal clarity, aligning the noisy constellation points closer to their ideal locations, which translates to lower BERs and higher performance.
  ![Constellation Changes GIF](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/QAM64_Simulink/ConstellationChange.gif)

<p align="justify">
  <strong>BER Analysis:</strong> The <code>BER.m</code> script evaluates the Bit Error Rate (BER) for a 64-QAM system over SNRs from -10 dB to 20 dB. It starts by determining the modulated signal's power to accurately configure the AWGN channel settings in Simulink. The script then simulates the QAM system across specified Eb/No values, calculating BER for each by comparing the number of errors detected to the total number of bits transmitted. Results from these simulations are plotted against theoretical BER values derived from the <code>berawgn</code> function, directly illustrating the impact of noise on system performance. This analysis provides a direct link between theoretical expectations and empirical data, highlighting the modulation scheme's robustness.
</p>

  ![BER Plot](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/QAM64_Simulink/BER.png)

## Designing and simulating an algorithm for n-gram Huffman source codes using MATLAB

### Introduction
This section of the repository introduces a Huffman coding algorithm, a source coding method used to perform efficient data compression. The algorithm's design facilitates the generation of a compact, variable-length code for each character of the input data, optimizing the overall size of the encoded data.

### Algorithm Design
The Huffman coding process utilized in this project is systematically broken down into a sequence of steps that generate the Huffman codes based on the probabilities of occurrence of input characters.

![Designed Algorithm Flowchart](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/Huffman/DesignedAlgorithm.png)

### Probabilities Index Tree Generator
The process starts by creating an index tree that helps in organizing the probabilities of the characters into a structured format that aids in subsequent code generation steps. This index tree is crucial for maintaining the hierarchical nature of Huffman coding.

![Probabilities Index Tree Generator](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/Huffman/IndexTreeGenerator.png)

### Huffman Code Generator
Once the index tree is established, the Huffman Code Generator algorithm assigns binary codes to each character. These codes are generated such that frequently occurring characters have shorter codes, thereby reducing the average code length and achieving compression.

![Huffman Code Generator](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/Huffman/HuffmanCodeGenerator.png)

### Huffman Coding Performance
The efficiency of the Huffman coding algorithm improves as the size of the n-grams increases, demonstrating its effectiveness in compressing data with increasing complexity.
![Efficiency VS gram number for Huffman algorithm](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/Huffman/EfficiencyVsGramNumber.png)

For detailed explanations of the algorithm's design, operational mechanics, and performance analysis, please refer to the [Project report](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/Huffman/DigitalCommunicationsProject.pdf) and review the  [`Huffman.mlx`](https://github.com/HashemRawashdeh/Advanced-Communication-Techniques--A-Practical-Approach/blob/main/Huffman/Huffman.mlx) MATLAB live editor file.
