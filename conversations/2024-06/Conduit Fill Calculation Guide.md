---
type: Conversation
title: "Conduit Fill Calculation Guide"
description: "Yo how do I account for 18/2 shielded cables when calculating conduit fill?"
resource: "7502c270-0a73-416d-b9bc-38406f5b52c2"
timestamp: "2024-06-12T10:27:18.184Z"
tags: ["gpt-4o"]
---

# Conduit Fill Calculation Guide

## User

Yo how do I account for 18/2 shielded cables when calculating conduit fill?

## Assistant



## Assistant

To account for 18/2 shielded cables when calculating conduit fill, you'll need to determine the cross-sectional area of the cable and compare it to the allowable fill capacity of the conduit. Here's a step-by-step guide:

1. **Determine the cross-sectional area of the 18/2 shielded cable**:
   - Check the manufacturer's datasheet for the cable. It should provide the cross-sectional area in square inches or square millimeters.
   - If the cross-sectional area is not listed, you may use standard tables provided by NEC (National Electrical Code) or other relevant codes which often list typical areas for common cables.

2. **Convert the cross-sectional area to match the units used in conduit fill tables** (if necessary):
   - 1 square inch = 645.16 square millimeters.
   - Make sure your cable area and conduit fill table are in the same units.

3. **Consult NEC Chapter 9, Table 1**:
   - This table provides guidelines for the maximum fill percentage for conduits based on the number of conductors:
     - 1 conductor: 53% fill
     - 2 conductors: 31% fill
     - More than 2 conductors: 40% fill

4. **Find the cross-sectional area of the conduit**:
   - Use NEC Chapter 9, Table 4 for rigid metal conduit (RMC), intermediate metal conduit (IMC), or electrical metallic tubing (EMT).
   - Look up the size of the conduit you plan to use and note its total cross-sectional area.

5. **Calculate the allowable fill area**:
   - Multiply the conduit’s total cross-sectional area by the appropriate fill percentage (from step 3).

6. **Calculate the total cross-sectional area of all cables**:
   - Multiply the cross-sectional area of one 18/2 shielded cable by the number of such cables you plan to install in the conduit.

7. **Compare the total cable area to the allowable fill area**:
   - Ensure the total cross-sectional area of all cables does not exceed the allowable fill area of the conduit.

### Example Calculation

1. **Cross-sectional area of 18/2 shielded cable**: Suppose the datasheet indicates an area of 0.012 square inches per cable.

2. **Conduit selection**: Assume you are using a 3/4-inch EMT conduit.
   - NEC Chapter 9, Table 4 lists the total area for 3/4-inch EMT as 0.213 square inches.

3. **Allowable fill**:
   - If you have more than two cables, use 40% fill: \(0.213 \times 0.40 = 0.0852 \) square inches.

4. **Total cable area**:
   - For example, if you plan to run 5 cables: \(0.012 \times 5 = 0.060\) square inches.

5. **Comparison**:
   - The total cable area (0.060 square inches) is less than the allowable fill area (0.0852 square inches), so this configuration is acceptable.

By following these steps, you can ensure that you comply with NEC guidelines and safely fill your conduit.

