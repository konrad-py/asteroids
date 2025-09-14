#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 11:20:39 2025

@author: kg
"""

import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity*dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(random_angle)
            vel2 = self.velocity.rotate(-random_angle)
            smaller_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, smaller_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, smaller_radius)
            asteroid1.velocity = vel1 * 1.2
            asteroid2.velocity = vel2 * 1.2
                        