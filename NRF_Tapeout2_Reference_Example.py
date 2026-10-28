"""
NRF Tapeout #2 — Reference GDSII & KLayout Layer Properties (.lyp) Generator
============================================================================
Generates:
  1. NRF_Tapeout2_Reference_Example.gds  (8 simple boxes showing each layer)
  2. NRF_Tapeout2.lyp                    (intuitive KLayout colors & stripes)

How to run:
  Option A (Standard Python):
      pip install klayout
      python NRF_Tapeout2_Reference_Example.py

  Option B (KLayout built-in batch mode):
      klayout -b -r NRF_Tapeout2_Reference_Example.py

  Output files are ALWAYS written next to this script (the
  NRF_Tapeout2_Layer_Guidelines folder), no matter which directory you run it from.

  Open the result with colors pre-applied:
      klayout -l NRF_Tapeout2.lyp NRF_Tapeout2_Reference_Example.gds
  or in the GUI: File -> Load Layer Properties -> select NRF_Tapeout2.lyp
  (If KLayout already had the file open, use File -> Reload, then press F2
   / View -> Zoom Fit to bring the shapes into view.)
"""

import os

try:
    import pya
except ImportError:
    import klayout.db as pya

# Folder containing this script -> all outputs land here
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def write_lyp_file(lyp_filename="NRF_Tapeout2.lyp"):
    """Writes the KLayout .lyp file with intuitive colors and stripe patterns."""
    lyp_xml = """<?xml version="1.0" encoding="utf-8"?>
<layer-properties>
 <properties>
  <frame-color>#334155</frame-color>
  <fill-color>#64748b</fill-color>
  <frame-brightness>0</frame-brightness>
  <fill-brightness>0</fill-brightness>
  <dither-pattern>I9</dither-pattern>
  <line-style/>
  <valid>true</valid>
  <visible>true</visible>
  <transparent>false</transparent>
  <width>2</width>
  <marked>false</marked>
  <xfill>false</xfill>
  <animation>0</animation>
  <name>1. SI_ETCH</name>
  <source>1/0</source>
 </properties>
 <properties>
  <frame-color>#15803d</frame-color>
  <fill-color>#22c55e</fill-color>
  <frame-brightness>0</frame-brightness>
  <fill-brightness>0</fill-brightness>
  <dither-pattern>I5</dither-pattern>
  <line-style/>
  <valid>true</valid>
  <visible>true</visible>
  <transparent>false</transparent>
  <width>2</width>
  <marked>false</marked>
  <xfill>false</xfill>
  <animation>0</animation>
  <name>2. NPLUS</name>
  <source>2/0</source>
 </properties>
 <properties>
  <frame-color>#b45309</frame-color>
  <fill-color>#f59e0b</fill-color>
  <frame-brightness>0</frame-brightness>
  <fill-brightness>0</fill-brightness>
  <dither-pattern>I9</dither-pattern>
  <line-style/>
  <valid>true</valid>
  <visible>true</visible>
  <transparent>false</transparent>
  <width>2</width>
  <marked>false</marked>
  <xfill>false</xfill>
  <animation>0</animation>
  <name>3. NWELL</name>
  <source>3/0</source>
 </properties>
 <properties>
  <frame-color>#0f766e</frame-color>
  <fill-color>#14b8a6</fill-color>
  <frame-brightness>0</frame-brightness>
  <fill-brightness>0</fill-brightness>
  <dither-pattern>I4</dither-pattern>
  <line-style/>
  <valid>true</valid>
  <visible>true</visible>
  <transparent>false</transparent>
  <width>2</width>
  <marked>false</marked>
  <xfill>false</xfill>
  <animation>0</animation>
  <name>4. THINOX</name>
  <source>4/0</source>
 </properties>
 <properties>
  <frame-color>#b91c1c</frame-color>
  <fill-color>#ef4444</fill-color>
  <frame-brightness>0</frame-brightness>
  <fill-brightness>0</fill-brightness>
  <dither-pattern>I2</dither-pattern>
  <line-style/>
  <valid>true</valid>
  <visible>true</visible>
  <transparent>false</transparent>
  <width>2</width>
  <marked>false</marked>
  <xfill>true</xfill>
  <animation>0</animation>
  <name>5. CONT</name>
  <source>5/0</source>
 </properties>
 <properties>
  <frame-color>#1d4ed8</frame-color>
  <fill-color>#3b82f6</fill-color>
  <frame-brightness>0</frame-brightness>
  <fill-brightness>0</fill-brightness>
  <dither-pattern>I5</dither-pattern>
  <line-style/>
  <valid>true</valid>
  <visible>true</visible>
  <transparent>false</transparent>
  <width>2</width>
  <marked>false</marked>
  <xfill>false</xfill>
  <animation>0</animation>
  <name>6. M1</name>
  <source>6/0</source>
 </properties>
 <properties>
  <frame-color>#6d28d9</frame-color>
  <fill-color>#8b5cf6</fill-color>
  <frame-brightness>0</frame-brightness>
  <fill-brightness>0</fill-brightness>
  <dither-pattern>I2</dither-pattern>
  <line-style/>
  <valid>true</valid>
  <visible>true</visible>
  <transparent>false</transparent>
  <width>2</width>
  <marked>false</marked>
  <xfill>true</xfill>
  <animation>0</animation>
  <name>7. VIA1</name>
  <source>7/0</source>
 </properties>
 <properties>
  <frame-color>#c2410c</frame-color>
  <fill-color>#f97316</fill-color>
  <frame-brightness>0</frame-brightness>
  <fill-brightness>0</fill-brightness>
  <dither-pattern>I9</dither-pattern>
  <line-style/>
  <valid>true</valid>
  <visible>true</visible>
  <transparent>false</transparent>
  <width>2</width>
  <marked>false</marked>
  <xfill>false</xfill>
  <animation>0</animation>
  <name>8. M2</name>
  <source>8/0</source>
 </properties>
</layer-properties>
"""
    with open(lyp_filename, "w", encoding="utf-8") as f:
        f.write(lyp_xml.strip() + "\n")
    print(f"[OK] Wrote KLayout Layer Properties file: {lyp_filename}")


def generate_reference_gds(gds_filename="NRF_Tapeout2_Reference_Example.gds"):
    # =========================================================================
    # STEP 1: KEEP THIS SETUP BLOCK (DO NOT DELETE)
    # Initializes the GDSII layout and registers all 8 required NRF layers
    # so that even unused layers are still saved in your final .gds file.
    # =========================================================================
    layout = pya.Layout()
    layout.dbu = 0.001  # 1 nm database unit (DBox coordinates below are in um)

    # Change "NRF_Team_ReferenceExample" to "<YourName>_<DeviceName>"
    top = layout.create_cell("NRF_Team_ReferenceExample")

    # All 8 mandatory layers registered in exact order (1/0 through 8/0)
    l_sietch = layout.layer(1, 0, "SI_ETCH")
    l_nplus  = layout.layer(2, 0, "NPLUS")
    l_nwell  = layout.layer(3, 0, "NWELL")
    l_thinox = layout.layer(4, 0, "THINOX")
    l_cont   = layout.layer(5, 0, "CONT")
    l_m1     = layout.layer(6, 0, "M1")
    l_via1   = layout.layer(7, 0, "VIA1")
    l_m2     = layout.layer(8, 0, "M2")

    # =========================================================================
    # ✂️ DELETE FROM HERE: DEMO LAYER SWATCH BOXES (FOR REFERENCE ONLY)
    # Delete the block between "DELETE FROM HERE" and "STOP DELETING HERE"
    # when you are ready to draw your own device.
    # =========================================================================
    demo_layers = [
        # Top Row (Layers 1 to 4)
        (l_sietch, "1. SI_ETCH (1/0)",   0.0,  50.0),
        (l_nplus,  "2. NPLUS (2/0)",    70.0,  50.0),
        (l_nwell,  "3. NWELL (3/0)",   140.0,  50.0),
        (l_thinox, "4. THINOX (4/0)",  210.0,  50.0),
        # Bottom Row (Layers 5 to 8)
        (l_cont,   "5. CONT (5/0)",      0.0,   0.0),
        (l_m1,     "6. M1 (6/0)",       70.0,   0.0),
        (l_via1,   "7. VIA1 (7/0)",    140.0,   0.0),
        (l_m2,     "8. M2 (8/0)",      210.0,   0.0),
    ]

    box_w = 45.0  # Box width in micrometers (um)
    box_h = 28.0  # Box height in micrometers (um)

    for layer_id, label, x0, y0 in demo_layers:
        # Draw a simple rectangle on this layer: DBox(left, bottom, right, top)
        top.shapes(layer_id).insert(pya.DBox(x0, y0, x0 + box_w, y0 + box_h))
        # Place a label right above the box
        top.shapes(layer_id).insert(pya.DText(label, pya.DTrans(x0, y0 + box_h + 4.0)))
    # =========================================================================
    # ✂️ STOP DELETING HERE
    # =========================================================================

    # =========================================================================
    # 🚀 START YOUR DEVICE CODE HERE
    # How to draw rectangles on any layer (coordinates in micrometers, um):
    #   top.shapes(l_nwell).insert(pya.DBox(x_min, y_min, x_max, y_max))
    #
    # Examples (uncomment to use):
    #   top.shapes(l_nplus).insert(pya.DBox(0.0, 0.0, 20.0, 40.0))
    #   top.shapes(l_thinox).insert(pya.DBox(15.0, 5.0, 35.0, 35.0))
    #   top.shapes(l_cont).insert(pya.DBox(5.0, 10.0, 12.0, 30.0))
    #   top.shapes(l_m1).insert(pya.DBox(-5.0, 5.0, 15.0, 35.0))
    # =========================================================================


    # =========================================================================
    # STEP 3: KEEP THIS SAVE BLOCK (DO NOT DELETE)
    # Writes the final GDSII file while preserving all 8 layer definitions.
    # =========================================================================
    save_opts = pya.SaveLayoutOptions()
    save_opts.write_context_info = True
    layout.write(gds_filename, save_opts)
    print(f"[OK] Wrote GDSII file: {gds_filename}")

    verify_gds(gds_filename)


def verify_gds(gds_filename):
    """Reads the GDS back and reports shapes per layer, so an empty file is caught immediately."""
    check = pya.Layout()
    check.read(gds_filename)
    top_cell = check.top_cell()
    total = 0
    print(f"[CHECK] Top cell: {top_cell.name}   bbox (um): {top_cell.dbbox()}")
    for li in check.layer_indexes():
        n = top_cell.shapes(li).size()
        total += n
        print(f"        layer {check.get_info(li)}: {n} shape(s)")
    if total == 0:
        print("[WARN] GDS contains NO shapes - did you delete the demo block without adding your own device?")


if __name__ == "__main__":
    write_lyp_file(os.path.join(SCRIPT_DIR, "NRF_Tapeout2.lyp"))
    generate_reference_gds(os.path.join(SCRIPT_DIR, "NRF_Tapeout2_Reference_Example.gds"))