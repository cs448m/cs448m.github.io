import pyembroidery as emb

def h_straight(pattern, x, y, dx, nx):
    pattern.add_stitch_absolute(emb.JUMP,x,y)
    for x in range(x,x_nx,dx):
        pattern.add_stitch_absolute(emb.STITCH, x,y)
    if x != x+nx:
        pattern.add_stitch_absolute(emb.STITCH, x+nx,y)
    pattern.add_command(emb.STOP)

def v_straight(pattern, x, y, dy, ny):
    pattern.add_stitch_absolute(emb.JUMP,x,y)
    for y in range(y,y+ny,dy):
        pattern.add_stitch_absolute(emb.STITCH, x,y)
    if y != y+ny:
        pattern.add_stitch_absolute(emb.STITCH, x,y+ny)
    pattern.add_command(emb.STOP)

def squares(pattern,del):
    for inset in range(10,50):
        square(inset, inset) 
    pattern.add_command(emb.END)
    return pattern

pattern = squares()
emb.write(pattern, "squares.pes")
