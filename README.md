# Digital Audio Board - Darren Aleja

## Table of Contents

- [Project Overview](#project-overview)
- [Project Description](#project-description)
- [PCB Design Highlights](#pcb-design-highlights)
- [Branch Information](#branch-information)
- [Theoretical Background](#theoretical-background)
- [Build Process](#build-process)
- [Future Improvements](#future-improvements)
- [Contact Information](#contact-information)
- [Acknowledgments](#acknowledgments)

## Project Overview

I developed this digital audio board to handle and playback digital audio through various transformations and interfaces. This repository contains the circuit design, PCB project, datasheets, and detailed documentation needed to understand the digital audio processing workflow implemented.

## Project Description

This board processes AES3 differential audio signals using a comprehensive suite of components that ensure high-quality audio output:

1. **Receiving AES3 Signal**: Captures AES3 differential audio known for its high reliability and quality in professional audio transmission.
2. **Signal Buffering**: Utilizes a THS4522 buffer op-amp to maintain signal integrity as it feeds into the decoding stage.
3. **Digital Audio Decoding**: The CS8416 digital audio interface receiver decodes the buffered AES3 signal into an I2S digital audio format, supporting various digital audio formats with flexible interfacing.
4. **Microcontroller Processing**: A Raspberry Pi Pico microcontroller converts the I2S signal into a PWM output suitable for driving a speaker and manages I2C control signals for dynamic decoder control.
5. **Audio Output**: Outputs audio through a speaker using the PWM signal generated by the Raspberry Pi Pico.
6. **Signal Passing**: Outputs a single-ended signal from the CS8416 back into the THS4522 for onward transmission, enhancing system flexibility.

## PCB Design Highlights

- **Decoupling and Bulk Capacitors**: Incorporates 100nF ceramic decoupling capacitors near IC pins to eliminate high-frequency noise and 10uF aluminum electrolytic capacitors to stabilize supply voltage, critical for high-gain op-amp operations.
- **Symmetry and DNF Resistors**: Features a symmetrical op-amp layout to equalize signal path lengths, reducing phase shifts and susceptibility to EMI.
- **Power and Ground Plane**: Uses continuous planes to reduce impedance and stabilize a low-noise environment, with strategic cutouts under the op-amp to prevent unwanted capacitance effects.
- **Differential Pair Traces**: Aligns traces meticulously for differential signals to maintain signal integrity and minimize phase errors and external noise susceptibility.

## Branch Information

- **initial-design**: This branch hosts the original PCB files that were submitted for manufacturing. It represents the first complete design iteration of the audio board.
- **design-revisions**: Ongoing updates and enhancements to the initial PCB design are made in this branch. It includes comprehensive revisions in terms of circuit design and layout optimizations.

## Theoretical Background

*Work in Progress*
Explanation of the underlying theories and principles behind the audio processing implemented in the project.

## Build Process

*Work in Progress*
Detailed steps and considerations taken during the assembly and testing of the PCB.

## Future Improvements

*Work in Progress*
Potential upgrades and optimizations for future versions of the PCB.

## Contact Information

For any inquiries or further discussion regarding the project, please contact me at [email].

## Acknowledgments

- **Professor Patrick Palmer**: For his invaluable guidance and oversight throughout the project.
- **TA Jordan Hughes**: For his assistance in PCB design and troubleshooting.
