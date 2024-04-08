Lift1:
VERSION 01
State machine implementation of the if - else VHDL block.
Sensor input is considered only if the target floor sensors are active and rest are inactive.

Lift2:
VERSION 02
Sensor input of target floor is considered irrespective of whether the rest of the sensors are giving o/p logic-1 or logic-0.
PROBLEM DETECTED:
Motor inputs is in mealy form, i.e., changes with state input rather than changing with state as intended.
Arised due to configuring motor output based on the next states (A2, B2, C2) instead of (A, B, C).

Lift3:
VERSION 03
Simplifying the state equations of obtained from the VERSION 2.
Motor inputs problem rectified. The motor inputs now depends on the current state rather than the next state.
