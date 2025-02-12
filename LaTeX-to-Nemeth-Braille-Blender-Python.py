# Copy the script below and paste it into the Blender Python scripting enviroment, then run the script to generate the Braille dots into 3D objects.

import bpy

# Dictionary: LaTeX symbol -> Nemeth Braille dots #
###################################################
latex_to_nemeth = {
    "\\alpha": "⠁⠇⠋⠁",  # Example mapping
    "\\beta":  "⠃⠢⠞⠕⠅",  # Example mapping
    "x^2":     "⠭⠔⠆",    # Example mapping for x squared
    # Add more mappings as needed
}

# 1) Convert LaTeX-like string to Nemeth Braille dots  #
########################################################
def convert_to_nemeth(latex_str):
    """
    Converts a LaTeX-style math expression into 
    the Nemeth Braille string (Unicode).
    """
    nemeth_str = []
    for symbol in latex_str.split():
        if symbol in latex_to_nemeth:
            nemeth_str.append(latex_to_nemeth[symbol])
        else:
            # Fallback for unmapped symbols
            nemeth_str.append("⠿")
    # Join them with a space or directly concatenate
    return " ".join(nemeth_str)

# 2) Create a single Braille cell: six (or potentially eight) dots
#    We'll assume 6-dot Braille as: 
#     dot 1: top-left,    dot 4: top-right
#     dot 2: middle-left, dot 5: middle-right
#     dot 3: bottom-left, dot 6: bottom-right
##################################################################

def create_braille_cell(braille_char, 
                        origin_x=0.0, origin_y=0.0, origin_z=0.0,
                        dot_radius=0.02,        # Cylinder radius
                        dot_depth=0.02,         # Cylinder height
                        vertical_spacing=0.05, 
                        horizontal_spacing=0.05,
                        cylinder_vertices=150):
    """
    Creates 3D geometry for a single 6-dot Braille character at 
    the given origin. Each 'raised' dot is represented by a cylinder.

    :param braille_char: A single Unicode Braille character (⠁ to ⣿).
    :param origin_x, origin_y, origin_z: Starting coordinates.
    :param dot_radius: The radius of each cylinder used as a dot.
    :param dot_depth: The height (depth) of each cylinder.
    :param vertical_spacing: Vertical distance between dot rows.
    :param horizontal_spacing: Horizontal distance between dot columns.
    :param cylinder_vertices: Number of vertices for the cylinder (smoothness).
    """
    # Convert Braille char to integer offset from U+2800
    braille_offset = ord(braille_char) - 0x2800
    # Braille bit pattern (for 6-dot, bits 0..5 matter)
    # A typical mapping of bits to dot positions is:
    #  bit0 -> dot1, bit1 -> dot2, bit2 -> dot3, bit3 -> dot4, bit4 -> dot5, bit5 -> dot6
    
    # Dot positions relative to the origin, if raised:
    # dot1: (0, 0)                dot4: (horizontal_spacing, 0)
    # dot2: (0, -vertical_spacing)       dot5: (horizontal_spacing, -vertical_spacing)
    # dot3: (0, -2*vertical_spacing)     dot6: (horizontal_spacing, -2*vertical_spacing)
    dot_positions = [
        (0.0, 0.0, 0.0),  # dot1
        (0.0, -vertical_spacing, 0.0),   # dot2
        (0.0, -2.0 * vertical_spacing, 0.0), # dot3
        (horizontal_spacing, 0.0, 0.0),      # dot4
        (horizontal_spacing, -vertical_spacing, 0.0),   # dot5
        (horizontal_spacing, -2.0 * vertical_spacing, 0.0) # dot6
    ]
    
    for i in range(6):
        # Check if bit i is set (i.e., if the dot is 'raised')
        if braille_offset & (1 << i):
            # If it's set, create a cylinder (dot)
            bpy.ops.mesh.primitive_cylinder_add(
                vertices=cylinder_vertices,
                radius=dot_radius,
                depth=dot_depth,
                end_fill_type='NGON',  # or 'TRIFAN' based on preference
                location=(origin_x + dot_positions[i][0],
                          origin_y + dot_positions[i][1],
                          origin_z + dot_positions[i][2] + dot_depth/2.0) 
                # ^ shift up by half the depth so the "bottom" of the cylinder sits on Z=origin
            )
            # Optional: rename or group the object here

########################################################################################
# 3) Create an entire row of Braille cells from a Nemeth Braille string (multiple chars)
########################################################################################
def create_braille_string(nemeth_str, 
                          start_x=0.0, start_y=0.0, start_z=0.0,
                          cell_spacing=0.15, **kwargs):
    """
    Given a Nemeth Braille string (which may contain spaces 
    or multiple characters), create a series of Braille cells in 3D.

    :param nemeth_str: A string of Braille characters (possibly containing spaces).
    :param start_x, start_y, start_z: Starting position for the row.
    :param cell_spacing: Horizontal distance between each Braille cell.
    :param kwargs: Additional keyword arguments passed to create_braille_cell().
    """
    x_offset = start_x
    # Iterate char by char, skipping spaces or invalid chars
    for char in nemeth_str:
        if char == ' ' or not (0x2800 <= ord(char) <= 0x28FF):
            x_offset += cell_spacing
            continue
        
        # Create the Braille cell
        create_braille_cell(char, origin_x=x_offset, origin_y=start_y, origin_z=start_z, **kwargs)
        # Move over for the next cell
        x_offset += cell_spacing


# 4) Example usage: Generating Braille from LaTeX input #
#########################################################
def main():
    # Example LaTeX input
    latex_input = "\\alpha x^2 \\beta"
    
    # Convert to Nemeth Braille
    nemeth_str = convert_to_nemeth(latex_input)
    print("Nemeth Braille for '{}': {}".format(latex_input, nemeth_str))
    
    # Create the Braille row in Blender using cylinders
    create_braille_string(nemeth_str, 
                          start_x=0.0, 
                          start_y=0.0,
                          cell_spacing=0.2,  # spacing between cells horizontally
                          dot_radius=0.02,   # cylinder radius
                          dot_depth=0.02,    # cylinder height
                          vertical_spacing=0.05,
                          cylinder_vertices=150)  # number of vertices to smooth the cylinder

# Run the main function when script is executed
if __name__ == "__main__":
    main()
