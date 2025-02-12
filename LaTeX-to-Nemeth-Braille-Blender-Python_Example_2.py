# Copy the script below and paste it into the Blender Python scripting enviroment, then run the script to generate the Braille dots into 3D objects.

import bpy


# A *VERY* simplified dictionary mapping some LaTeX pieces
# to Nemeth Braille-like dots (placeholders, not fully accurate).
#################################################################
latex_to_nemeth = {
    "\\left[":          "⠐⠣",       # Opening bracket
    "\\right]":         "⠐⠜",       # Closing bracket
    "\\frac":           "⠣⠋⠗⠁⠉⠈⠜", # "frac" spelled out in Braille
    "\\hbar^2":         "⠓⠃⠁⠗⠔⠆", # h-bar squared
    "2":                "⠼⠃",       # Digit '2'
    "m^*":              "⠍⠔⠡",      # m star
    "\\nabla^2":        "⠝⠙⠇⠁⠔⠆", # nabla squared
    "+":                "⠐⠖",       # plus sign
    "U(\\vec{r})":      "⠠⠥⠐⠣⠗⠐⠜",  # U(r) (vector arrow ignored)
    "|\\psi(\\vec{r})>":"⠸⠏⠎⠊⠐⠣⠗⠐⠜", # |psi(r)>
    "=":                "⠨⠅",       # equals sign
    "E":                "⠠⠑",       # capital E
}


# 1) Convert the LaTeX string to a naive Braille transcription
#    (really just a dictionary lookup for recognized tokens).
#################################################################
def convert_to_nemeth(latex_str):
    """
    Converts a given LaTeX string to a (very rough) Nemeth Braille equivalent
    using the dictionary above. Unmapped symbols are replaced with ⠿.
    
    This is analogous to the original create_svg()'s conversion step.
    """
    parts = latex_str.split()
    nemeth_str = ""

    for part in parts:
        # If the dictionary has the token, map it
        if part in latex_to_nemeth:
            nemeth_str += latex_to_nemeth[part] + " "
        else:
            # Fallback: ⠿
            nemeth_str += "⠿ "
    
    return nemeth_str.strip()


# 2) Create a single Braille character in 3D.
#    By default, we assume 6-dot Braille in a 2×3 grid.
#################################################################
def create_braille_cell(braille_char, 
                        origin_x=0.0, origin_y=0.0, origin_z=0.0,
                        dot_radius=0.02,      # Cylinder radius
                        dot_depth=0.02,       # Cylinder height
                        vertical_spacing=0.05, 
                        horizontal_spacing=0.05,
                        cylinder_vertices=64):
    """
    Creates 3D geometry for a single Braille character (⠁ to ⣿) at the given origin.
    Each 'raised' dot is represented by a cylinder (like a short peg).
    
    This uses the standard 6-dot arrangement:
    
        bit0 -> dot1: top-left
        bit1 -> dot2: mid-left
        bit2 -> dot3: bottom-left
        bit3 -> dot4: top-right
        bit4 -> dot5: mid-right
        bit5 -> dot6: bottom-right
        
    You can expand for 8-dot Braille if needed.
    """
    braille_offset = ord(braille_char) - 0x2800

    # Dot positions relative to the cell origin
    dot_positions = [
        (0.0, 0.0, 0.0),                         # dot1
        (0.0, -vertical_spacing, 0.0),           # dot2
        (0.0, -2.0 * vertical_spacing, 0.0),     # dot3
        (horizontal_spacing, 0.0, 0.0),          # dot4
        (horizontal_spacing, -vertical_spacing, 0.0),      # dot5
        (horizontal_spacing, -2.0 * vertical_spacing, 0.0) # dot6
    ]

    for i in range(6):
        if braille_offset & (1 << i):
            # Dot i is 'raised'
            bpy.ops.mesh.primitive_cylinder_add(
                vertices=cylinder_vertices,
                radius=dot_radius,
                depth=dot_depth,
                end_fill_type='NGON',
                location=(
                    origin_x + dot_positions[i][0],
                    origin_y + dot_positions[i][1],
                    origin_z + dot_depth/2.0  # shift up so bottom sits at origin_z
                )
            )


# 3) Create a row of Braille cells for a multi-character string.
#################################################################
def create_braille_string(nemeth_str, 
                          start_x=0.0, start_y=0.0, start_z=0.0,
                          cell_spacing=0.15,
                          dot_radius=0.02,
                          dot_depth=0.02,
                          vertical_spacing=0.05,
                          horizontal_spacing=0.05,
                          cylinder_vertices=64):
    """
    Takes a string of Braille characters (which may contain spaces)
    and places them as a series of 6-dot cells in 3D.
    """
    x_offset = start_x
    
    for char in nemeth_str:
        # If it's a space or not in the Braille block, skip it
        if char == ' ' or not (0x2800 <= ord(char) <= 0x28FF):
            x_offset += cell_spacing
            continue
        
        create_braille_cell(
            braille_char=char,
            origin_x=x_offset,
            origin_y=start_y,
            origin_z=start_z,
            dot_radius=dot_radius,
            dot_depth=dot_depth,
            vertical_spacing=vertical_spacing,
            horizontal_spacing=horizontal_spacing,
            cylinder_vertices=cylinder_vertices
        )
        x_offset += cell_spacing

# 4) Example usage
#    Replaces the original create_svg() usage with Blender geometry.
#################################################################
def main():
    # The same example LaTeX input from your original code:
    latex_input = (
        "\\left[ -\\frac{\\hbar^2}{2 m^*} \\nabla^2 + U(\\vec{r}) \\right] |\\psi(\\vec{r})> = E |\\psi(\\vec{r})>"
    )
    
    description = (
        "Placeholder Nemeth Braille transcription of a time-independent Schrodinger equation. "
        "Bra-ket notation replaced by | and >."
    )
    
    print("LaTeX input:", latex_input)
    print("Description:", description)
    
    # 1) Convert to a naive Nemeth Braille string
    nemeth_str = convert_to_nemeth(latex_input)
    print("Naive Nemeth Braille:", nemeth_str)
    
    # 2) Create the corresponding Braille geometry in Blender
    create_braille_string(
        nemeth_str,
        start_x=0.0, 
        start_y=0.0, 
        start_z=0.0,
        cell_spacing=0.2,      # Horizontal spacing between Braille cells
        dot_radius=0.02,       # Cylinder radius
        dot_depth=0.02,        # Cylinder height
        vertical_spacing=0.05, # Vertical spacing between dot rows
        horizontal_spacing=0.05,
        cylinder_vertices=64    # Smoothness of the cylinder
    )
    
    print("Braille geometry created in Blender.")

# Execute the main function if this script is run
if __name__ == "__main__":
    main()
