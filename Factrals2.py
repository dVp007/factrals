import pygame,math

#intialize pygame
pygame.init()

#creating a new surface and window 
surface_height, surface_width = 800,600
main_surface = pygame.display.set_mode((surface_height,surface_width))

#captioning the window
pygame.display.set_caption("Factrals")

def draw_tree(order,theta,sz,posn,heading,color, depth):
    trunk_ratio = 0.29

    trunk = sz *trunk_ratio
    delta_x = trunk*math.cos(heading)
    delta_y = trunk*math.sin(heading)
    (u,v) = posn
    newpos = (u+delta_x,v+delta_y)
    pygame.draw.line(main_surface,color,posn,newpos)
    if order>0:
        if depth == 0:
            color1=(255,0,0)
            color2=(0,0,255)
        else:
            color1=color
            color2=color
        newsz = sz*(1-trunk_ratio)
        draw_tree(order-1, theta, newsz, newpos, heading-theta, color1, depth+1) 
        draw_tree(order-1, theta, newsz, newpos, heading+theta, color2, depth+1) 
        pass
def main():
    theta = 0
  
    while True: 
  
        # Update the angle 
        theta += 0.01
  
        # This little part lets us draw the stuffs  
        # in the screen everything 
        main_surface.fill((255, 255, 0)) 
        draw_tree(9, theta, surface_height*0.9, (surface_width//2, surface_width-50), -math.pi/2,(0,0,0),0) 
        pygame.display.flip()

main()
pygame.quit()